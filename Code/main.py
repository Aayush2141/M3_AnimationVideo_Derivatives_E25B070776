"""
main.py – Render all scenes and concatenate into the final video.

Usage:
    # Render all scenes individually
    python main.py

    # Or render one scene at a time (useful for debugging):
    manim -pqh scenes/scene1_intro.py Scene1Intro
"""

import subprocess
import sys
import os

VENV_MANIM = os.path.join(os.path.dirname(__file__), "venv", "bin", "manim")
MANIM_CMD  = VENV_MANIM if os.path.exists(VENV_MANIM) else "manim"

SCENES = [
    ("scene1_intro.py",          "Scene1Intro"),
    ("scene2_concept.py",        "Scene2Concept"),
    ("scene3_secant_tangent.py", "Scene3SecantTangent"),
    ("scene4_derivation.py",     "Scene4Derivation"),
    ("scene5_interpretation.py", "Scene5Interpretation"),
    ("scene6_summary.py",        "Scene6Summary"),
]

QUALITY = "-qh"   # high quality 1080p; use -ql for fast preview

def run_manim(scene_file, scene_class):
    cmd = [MANIM_CMD, QUALITY, scene_file, scene_class]
    print(f"\n{'='*60}")
    print(f"Rendering: {scene_class}")
    print(f"Command  : {' '.join(cmd)}")
    print('='*60)
    result = subprocess.run(cmd, capture_output=False)
    if result.returncode != 0:
        print(f"[ERROR] Rendering {scene_class} failed.")
        sys.exit(result.returncode)
    print(f"[OK] {scene_class} rendered successfully.")


def find_rendered_file(scene_class, quality="1080p60"):
    """Find the rendered mp4 file for a scene."""
    base = os.path.join("media", "videos")
    for root, dirs, files in os.walk(base):
        for f in files:
            if scene_class in f and f.endswith(".mp4"):
                return os.path.join(root, f)
    return None


def concatenate_videos():
    """Use ffmpeg to concatenate all rendered scenes."""
    video_files = []
    for _, scene_class in SCENES:
        path = find_rendered_file(scene_class)
        if path:
            video_files.append(path)
            print(f"  Found: {path}")
        else:
            print(f"  [WARNING] Could not find rendered file for {scene_class}")

    if not video_files:
        print("[ERROR] No rendered files found. Run rendering first.")
        return

    list_file = "renders/concat_list.txt"
    os.makedirs("renders", exist_ok=True)
    with open(list_file, "w") as f:
        for vf in video_files:
            abs_path = os.path.abspath(vf)
            f.write(f"file '{abs_path}'\n")

    output = "renders/M3_Derivatives_And_Rate_Of_Change_FINAL.mp4"
    cmd = [
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", list_file,
        "-c:v", "libx264", "-crf", "18",
        "-preset", "slow",
        "-pix_fmt", "yuv420p",
        output,
    ]
    print(f"\nConcatenating {len(video_files)} scenes → {output}")
    result = subprocess.run(cmd, capture_output=False)
    if result.returncode == 0:
        size_mb = os.path.getsize(output) / (1024*1024)
        print(f"\n✅ Final video saved: {output}  ({size_mb:.1f} MB)")
    else:
        print("[ERROR] ffmpeg concatenation failed.")


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    for scene_file, scene_class in SCENES:
        run_manim(scene_file, scene_class)

    concatenate_videos()
    print("\nDone! Check the renders/ folder for the final MP4.")
