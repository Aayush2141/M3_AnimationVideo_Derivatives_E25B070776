"""
Align the generated TTS narration segments to each rendered scene's exact beat timings,
concatenate all six scenes and audio tracks, and export:
renders/M3_Derivatives_And_Rate_Of_Change_WITH_VOICEOVER.mp4
"""

import os
import subprocess
from pydub import AudioSegment

VOICEOVER_DIR = "voiceover"
OUTPUT_AUDIO = "voiceover/full_voiceover.wav"
OUTPUT_VIDEO = "renders/M3_Derivatives_And_Rate_Of_Change_WITH_VOICEOVER.mp4"

SCENE_VIDEOS = [
    "media/videos/scene1_intro/1080p60/Scene1Intro.mp4",
    "media/videos/scene2_concept/1080p60/Scene2Concept.mp4",
    "media/videos/scene3_secant_tangent/1080p60/Scene3SecantTangent.mp4",
    "media/videos/scene4_derivation/1080p60/Scene4Derivation.mp4",
    "media/videos/scene5_interpretation/1080p60/Scene5Interpretation.mp4",
    "media/videos/scene6_summary/1080p60/Scene6Summary.mp4",
]

# Exact beat durations (seconds) matching the visual beats in each scene.
# Each spoken part is placed 0.35s into its beat (0.50s for Beat 1).
SCENE_BEATS = {
    1: [10.93, 16.44, 17.02, 11.51],
    2: [13.95,  9.60, 17.36, 20.94],
    3: [20.67, 24.51, 15.17, 16.62],
    4: [27.35, 20.04, 10.44,  9.05,  7.64,  9.82,  7.59, 12.34, 19.50],
    5: [15.01, 24.05, 11.67, 23.08],
    6: [ 5.00,  7.18,  6.96, 16.16, 15.20],
}


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


def build_aligned_scene_audio(scene_num: int, video_dur: float) -> AudioSegment:
    beats = SCENE_BEATS[scene_num]
    target_ms = int(round(video_dur * 1000))
    canvas = AudioSegment.silent(duration=target_ms, frame_rate=44100).set_channels(2)

    cursor_ms = 0
    for idx, beat_dur in enumerate(beats, start=1):
        part_path = os.path.join(VOICEOVER_DIR, f"scene{scene_num}_part{idx}.mp3")
        seg = AudioSegment.from_mp3(part_path).set_frame_rate(44100).set_channels(2)

        lead_ms = 500 if idx == 1 else 350
        start_ms = cursor_ms + lead_ms

        # Safety clamp so audio never spills past scene end
        if start_ms + len(seg) > target_ms:
            start_ms = max(0, target_ms - len(seg) - 50)

        canvas = canvas.overlay(seg, position=start_ms)
        print(
            f"  Scene {scene_num} Part {idx}: start={start_ms/1000:.2f}s, "
            f"end={(start_ms+len(seg))/1000:.2f}s (beat={beat_dur:.2f}s, speech={len(seg)/1000:.2f}s)"
        )
        cursor_ms += int(round(beat_dur * 1000))

    return canvas


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    os.makedirs("renders", exist_ok=True)
    os.makedirs(VOICEOVER_DIR, exist_ok=True)

    full_audio = AudioSegment.empty()
    list_file = "renders/concat_list_vo.txt"
    with open(list_file, "w") as f:
        for s_idx, vid_path in enumerate(SCENE_VIDEOS, start=1):
            vid_dur = get_media_duration(vid_path)
            print(f"\nAligning Scene {s_idx} (video={vid_dur:.2f}s):")
            scene_audio = build_aligned_scene_audio(s_idx, vid_dur)
            scene_wav = os.path.join(VOICEOVER_DIR, f"scene{s_idx}_aligned.wav")
            scene_audio.export(scene_wav, format="wav")
            full_audio += scene_audio
            f.write(f"file '{os.path.abspath(vid_path)}'\n")

    # Gentle peak normalization (-1.5 dBFS) for clean, consistent presentation volume
    peak_gain = -1.5 - full_audio.max_dBFS
    full_audio = full_audio.apply_gain(peak_gain)
    full_audio.export(OUTPUT_AUDIO, format="wav")
    print(f"\nCombined voiceover WAV: {OUTPUT_AUDIO} ({len(full_audio)/1000:.2f}s)")

    cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0", "-i", list_file,
        "-i", OUTPUT_AUDIO,
        "-c:v", "libx264", "-crf", "18", "-preset", "slow", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-ac", "2",
        "-shortest",
        OUTPUT_VIDEO,
    ]
    print(f"\nMuxing video + voiceover → {OUTPUT_VIDEO}")
    subprocess.run(cmd, check=True)
    size_mb = os.path.getsize(OUTPUT_VIDEO) / (1024 * 1024)
    print(f"\n✅ Final video with voiceover saved: {OUTPUT_VIDEO} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
