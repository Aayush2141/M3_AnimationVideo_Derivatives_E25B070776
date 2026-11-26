# Technical Notes – Derivatives and Rate of Change

## Visual & Colour System
- **Resolution & Frame Rate:** 1920 × 1080 (16:9), 60 FPS (`h264`, `yuv420p`)
- **Background:** `#0A0E1A` (Deep Navy)
- **Primary Accents:**
  - `#FFD700` (Gold) — Section headers, tangent lines, key derivative results
  - `#00D4FF` (Cyan) — Coordinate axes, definitions, intermediate values
  - `#39FF14` (Green) — Function curve `f(x) = x²`, simplified steps
  - `#FF6B9D` (Pink) — Secant lines, moving point `B`, `0/0` warning
  - `#E8EEF4` (Soft White) — Body text and labels

## Voiceover & Synchronization Pipeline
1. `generate_voiceover.py` parses `narration_script.md` (30 spoken segments across 6 scenes) and synthesizes Indian English male narration (`en-IN-PrabhatNeural`) using `edge-tts`.
2. `build_voiceover_video.py` aligns each spoken segment with its corresponding visual beat in the rendered Manim scenes.
3. `optimize_6min.py` trims leading/trailing TTS silence, applies pitch-preserved `atempo=1.10`, proportionally aligns each 1080p60 scene video, peak-normalizes audio to `-1.5 dBFS`, and muxes stereo AAC audio (`44100 Hz`, `192 kbps`) into `Derivatives_RateOfChange_Video.mp4` (`364.16 s`, `~19.6 MB`).
