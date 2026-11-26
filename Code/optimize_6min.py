"""
Optimize the existing 7:23 video + voiceover down to ~6:00 (360s) by:
1. Reusing existing voiceover/scene{s}_part{p}.mp3 clips.
2. Trimming hidden leading/trailing Edge-TTS silence (keeping 40ms padding so no word clips).
3. Applying a gentle, natural 1.10x pitch-preserved pace (atempo=1.10).
4. Using crisp natural pauses (0.30s lead-in, 0.35s inter-part gap, 0.35s tail-out; 2.8s tail in Scene 6).
5. Proportionally time-aligning the existing 1080p60 rendered scene videos to match each scene's
   exact new audio duration, keeping 1920x1080 @ 60 FPS and full beat synchronization.
6. Exporting to renders/M3_Derivatives_And_Rate_Of_Change_6MIN_FINAL.mp4.
"""

import os
import subprocess
from pydub import AudioSegment, silence

ATEMPO = 1.10
LEAD_MS = 300
GAP_MS = 350
TAIL_MS = 350
SCENE6_TAIL_MS = 2800

VOICEOVER_DIR = "voiceover"
OPT_DIR = "voiceover/6min"
OUTPUT_VIDEO = "renders/M3_Derivatives_And_Rate_Of_Change_6MIN_FINAL.mp4"

SCENE_VIDEOS = [
    "media/videos/scene1_intro/1080p60/Scene1Intro.mp4",
    "media/videos/scene2_concept/1080p60/Scene2Concept.mp4",
    "media/videos/scene3_secant_tangent/1080p60/Scene3SecantTangent.mp4",
    "media/videos/scene4_derivation/1080p60/Scene4Derivation.mp4",
    "media/videos/scene5_interpretation/1080p60/Scene5Interpretation.mp4",
    "media/videos/scene6_summary/1080p60/Scene6Summary.mp4",
]


def get_media_duration(path: str) -> float:
    out = subprocess.check_output(
        [
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "csv=p=0", path,
        ],
        text=True,
    ).strip()
    return float(out)


def trim_and_pace_part(src_mp3: str, dst_wav: str) -> AudioSegment:
    seg = AudioSegment.from_mp3(src_mp3).set_frame_rate(44100).set_channels(2)
    nonsil = silence.detect_nonsilent(seg, min_silence_len=80, silence_thresh=-45)
    if nonsil:
        start_ms = max(0, nonsil[0][0] - 40)
        end_ms = min(len(seg), nonsil[-1][1] + 40)
        seg = seg[start_ms:end_ms]

    tmp_wav = dst_wav + ".tmp.wav"
    seg.export(tmp_wav, format="wav")
    subprocess.run(
        [
            "ffmpeg", "-y", "-i", tmp_wav,
            "-af", f"atempo={ATEMPO}",
            "-ar", "44100", "-ac", "2",
            dst_wav,
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    os.remove(tmp_wav)
    return AudioSegment.from_wav(dst_wav)


def build_scene_audio(scene_num: int) -> tuple[AudioSegment, float]:
    parts: list[AudioSegment] = []
    p = 1
    while True:
        src = os.path.join(VOICEOVER_DIR, f"scene{scene_num}_part{p}.mp3")
        if not os.path.exists(src):
            break
        dst = os.path.join(OPT_DIR, f"scene{scene_num}_part{p}_fast.wav")
        parts.append(trim_and_pace_part(src, dst))
        p += 1

    tail_ms = SCENE6_TAIL_MS if scene_num == 6 else TAIL_MS
    scene_audio = AudioSegment.silent(duration=LEAD_MS, frame_rate=44100).set_channels(2)
    for idx, seg in enumerate(parts):
        if idx > 0:
            scene_audio += AudioSegment.silent(duration=GAP_MS, frame_rate=44100).set_channels(2)
        scene_audio += seg
    scene_audio += AudioSegment.silent(duration=tail_ms, frame_rate=44100).set_channels(2)

    scene_wav = os.path.join(OPT_DIR, f"scene{scene_num}_6min.wav")
    scene_audio.export(scene_wav, format="wav")
    return scene_audio, len(scene_audio) / 1000.0


def scale_scene_video(src_vid: str, dst_vid: str, target_dur: float):
    orig_dur = get_media_duration(src_vid)
    pts_factor = target_dur / orig_dur
    subprocess.run(
        [
            "ffmpeg", "-y", "-i", src_vid,
            "-vf", f"setpts={pts_factor:.6f}*PTS",
            "-r", "60",
            "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p",
            "-an",
            dst_vid,
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.makedirs(OPT_DIR, exist_ok=True)
    os.makedirs("renders", exist_ok=True)

    full_audio = AudioSegment.empty()
    scaled_videos = []

    for s_idx, src_vid in enumerate(SCENE_VIDEOS, start=1):
        orig_dur = get_media_duration(src_vid)
        scene_audio, new_dur = build_scene_audio(s_idx)
        scaled_vid = os.path.join(OPT_DIR, f"scene{s_idx}_6min.mp4")
        scale_scene_video(src_vid, scaled_vid, new_dur)
        actual_vid_dur = get_media_duration(scaled_vid)

        print(
            f"Scene {s_idx}: orig={orig_dur:.2f}s -> target_audio={new_dur:.2f}s, "
            f"scaled_video={actual_vid_dur:.2f}s (ratio={new_dur/orig_dur:.3f}x)"
        )
        full_audio += scene_audio
        scaled_videos.append(scaled_vid)

    # Peak-normalize combined audio to -1.5 dBFS
    peak_gain = -1.5 - full_audio.max_dBFS
    full_audio = full_audio.apply_gain(peak_gain)
    full_wav = os.path.join(OPT_DIR, "full_voiceover_6min.wav")
    full_audio.export(full_wav, format="wav")
    print(f"\nCombined 6-min voiceover: {full_wav} ({len(full_audio)/1000:.2f}s)")

    list_file = os.path.join(OPT_DIR, "concat_list_6min.txt")
    with open(list_file, "w") as f:
        for sv in scaled_videos:
            f.write(f"file '{os.path.abspath(sv)}'\n")

    subprocess.run(
        [
            "ffmpeg", "-y",
            "-f", "concat", "-safe", "0", "-i", list_file,
            "-i", full_wav,
            "-c:v", "copy",
            "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-ac", "2",
            "-shortest",
            OUTPUT_VIDEO,
        ],
        check=True,
    )
    size_mb = os.path.getsize(OUTPUT_VIDEO) / (1024 * 1024)
    print(f"\n✅ 6-minute final video saved: {OUTPUT_VIDEO} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
