"""
Generate AI voiceover segments from narration_script.md using edge-tts (en-IN-PrabhatNeural),
measure exact durations, and build per-scene synchronized audio tracks.
"""

import asyncio
import os
import re
import subprocess
import edge_tts
from pydub import AudioSegment

VOICE = "en-IN-PrabhatNeural"
RATE = "+12%"  # Clear, confident, moderate ~145 WPM university presentation pace

SCRIPT_PATH = "narration_script.md"
VOICEOVER_DIR = "voiceover"

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


def parse_narration_script(path: str) -> dict[int, list[str]]:
    """
    Parse narration_script.md into {scene_num: [spoken_paragraph_1, ...]}.
    Extracts only quoted spoken lines; ignores headings, timestamps, stage directions, notes.
    """
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    scenes: dict[int, list[str]] = {}
    current_scene = None

    for raw in lines:
        line = raw.strip()
        m = re.match(r"^##\s+SCENE\s+(\d+)\b", line)
        if m:
            current_scene = int(m.group(1))
            scenes[current_scene] = []
            continue

        if current_scene is None:
            continue

        # Only extract lines that are spoken dialogue (wrapped in double quotes)
        if line.startswith('"') and line.endswith('"'):
            text = line[1:-1]
            # Remove markdown bold markers without altering any words
            text = text.replace("**", "")
            scenes[current_scene].append(text)

    return scenes


async def synth_part(text: str, out_path: str):
    communicate = edge_tts.Communicate(text, VOICE, rate=RATE)
    await communicate.save(out_path)


async def generate_all_parts(scenes: dict[int, list[str]]):
    os.makedirs(VOICEOVER_DIR, exist_ok=True)
    for scene_num in sorted(scenes.keys()):
        parts = scenes[scene_num]
        for idx, text in enumerate(parts, start=1):
            out_path = os.path.join(VOICEOVER_DIR, f"scene{scene_num}_part{idx}.mp3")
            await synth_part(text, out_path)


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    scenes = parse_narration_script(SCRIPT_PATH)

    print("Parsed scenes from narration_script.md:")
    for s in sorted(scenes.keys()):
        print(f"  Scene {s}: {len(scenes[s])} spoken blocks")

    asyncio.run(generate_all_parts(scenes))

    print("\nGenerated audio durations vs Scene video durations:")
    for s in sorted(scenes.keys()):
        vid_dur = get_media_duration(SCENE_VIDEOS[s - 1])
        part_durs = []
        for idx in range(1, len(scenes[s]) + 1):
            p = os.path.join(VOICEOVER_DIR, f"scene{s}_part{idx}.mp3")
            seg = AudioSegment.from_mp3(p)
            part_durs.append(len(seg) / 1000.0)
        total_speech = sum(part_durs)
        print(
            f"  Scene {s}: video={vid_dur:.2f}s | speech={total_speech:.2f}s "
            f"| slack={vid_dur - total_speech:+.2f}s | parts={[round(d, 2) for d in part_durs]}"
        )


if __name__ == "__main__":
    main()
