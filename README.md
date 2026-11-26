# Derivatives and Rate of Change — M3 Mathematics Animation Project

An educational animated mathematics video built with **Manim Community Edition** explaining how the average rate of change between two points on a curve transitions into the instantaneous rate of change (the derivative), demonstrated visually and algebraically on $f(x) = x^2$.

---

## Student & Course Information

| Field | Details |
|-------|---------|
| **Student Name** | Aayush Singh |
| **Student ID** | E25B070776 |
| **Course** | Linear Algebra and Calculus (M3) |
| **Assessment** | M3 Internal Assessment — Animation Video Project |
| **Topic** | Derivatives and Rate of Change |

---

## Learning Objective

To build intuitive geometric and algebraic understanding of:
- How **average rate of change** over an interval corresponds to the **slope of a secant line**.
- How shrinking the interval ($h \to 0$) causes the secant line to rotate into the **tangent line**, representing the **instantaneous rate of change**.
- How to derive $f'(x) = 2x$ from **first principles** and evaluate tangent slopes and equations at specific points ($f'(2) = 4$, $f'(3) = 6$).

---

## Mathematical Concepts Explained

1. **Function Mapping:** $f(x) = x^2$ mapping inputs $x$ to outputs $y$.
2. **Average Rate of Change:** $\dfrac{f(b) - f(a)}{b - a} = \dfrac{\text{Rise}}{\text{Run}}$ (slope of the secant line).
3. **Limit & Tangent Line:** $f'(a) = \lim_{h \to 0} \dfrac{f(a+h) - f(a)}{h}$ as $B \to A$.
4. **Indeterminate Form $0/0$:** Why direct substitution of $h = 0$ fails and why algebraic simplification is required while $h \neq 0$.
5. **First-Principles Derivation:** Step-by-step expansion, cancellation of $x^2$, factoring $h$, cancelling $h/h$, and evaluating $h \to 0$ to obtain $f'(x) = 2x$.
6. **Geometric & Physical Interpretation:** Tangent slope $f'(2) = 4$, tangent line equation $y = 4x - 4$, connection to instantaneous car speed, and comparison with $f'(3) = 6$ ($y = 6x - 9$).

---

## Six-Scene Breakdown

| Scene | Duration | Title & Content |
|-------|----------|-----------------|
| **Scene 1** | `0:00 – 0:46` (`46.3 s`) | **Opening Hook:** Core calculus question, car & speedometer animation comparing average vs. instantaneous speed, parabola preview, and title card. |
| **Scene 2** | `0:46 – 1:38` (`52.0 s`) | **Understanding the Concept:** Plotting $f(x) = x^2$, rise/run triangle, secant line definition, and numerical average rate example on $[1, 3]$. |
| **Scene 3** | `1:38 – 2:44` (`65.8 s`) | **Secant to Tangent:** Live animation of $B$ approaching $A=(2,4)$ across 8 steps ($h = 1.50 \to 0$), live slope convergence ($6 \to 4$), golden tangent line, and average vs. instantaneous comparison. |
| **Scene 4** | `2:44 – 4:27` (`102.8 s`) | **First Principles Derivation:** Difference quotient setup, why $h = 0$ yields $0/0$, step-by-step algebraic derivation of $f'(x) = 2x$, and slope evaluations at $x=1,2,3$. |
| **Scene 5** | `4:27 – 5:30` (`62.9 s`) | **Interpretation & Worked Examples:** Computing $f'(2) = 4$, deriving $y = 4x - 4$, connecting to speedometer speed, and comparing with $f'(3) = 6$ ($y = 6x - 9$). |
| **Scene 6** | `5:30 – 6:04` (`34.5 s`) | **Summary & Credits:** Three core takeaways, formula recap, student details, academic reference, AI disclosure, and closing screen. |

---

## Repository Structure

```text
M3_AnimationVideo_Derivatives_E25B070776/
├── README.md
├── Derivatives_RateOfChange_Video.mp4     # Final 1080p60 video with synchronized voiceover (6m 04s)
├── storyboard.pdf                         # Complete visual storyboard (PDF)
├── Code/
│   ├── main.py                            # Master render and video concatenation script
│   ├── scene1_intro.py                    # Scene 1: Opening Hook
│   ├── scene2_concept.py                  # Scene 2: Understanding the Concept
│   ├── scene3_secant_tangent.py           # Scene 3: Secant to Tangent
│   ├── scene4_derivation.py               # Scene 4: First Principles Derivation
│   ├── scene5_interpretation.py           # Scene 5: Interpretation & Worked Examples
│   ├── scene6_summary.py                  # Scene 6: Summary & Credits
│   ├── generate_voiceover.py              # Script to synthesize narration from narration_script.md
│   ├── build_voiceover_video.py           # Script to align narration beats with scene renders
│   ├── optimize_6min.py                   # Script to trim silence and synchronize 6-min final MP4
│   ├── narration_script.md                # Full synchronized narration script
│   ├── requirements.txt                   # Python dependencies
│   └── assets/                            # Project assets directory
└── Supporting_Files/
    ├── storyboard.md                      # Markdown source of the storyboard
    └── Project_Technical_Notes.md         # Colour system and audio-video sync notes
```

---

## Tools & Technologies Used

- **Python 3.10**
- **Manim Community Edition (`0.19.1`)** — Mathematical animations and equation transforms
- **NumPy (`>=1.26`)** — Numerical computations
- **Edge TTS (`en-IN-PrabhatNeural`) & `pydub`** — Indian English male AI voiceover generation and beat alignment
- **FFmpeg** — Video concatenation, pitch-preserved pacing (`atempo`), and 1080p60 MP4 muxing

---

## Installation & Running the Animation

### 1. Prerequisites
- Python 3.10+
- `ffmpeg` installed on your system (`brew install ffmpeg` on macOS)

### 2. Setup
```bash
cd Code
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Render the Manim Scenes
```bash
# Render all six scenes at 1080p 60fps and concatenate:
python main.py

# Or render a single scene individually:
manim -pqh scene3_secant_tangent.py Scene3SecantTangent
```

---

## Final Video Information

- **Filename:** `Derivatives_RateOfChange_Video.mp4`
- **Duration:** `6 minutes 04 seconds` (`364.16 s`)
- **Resolution & Frame Rate:** `1920 × 1080` (16:9), `60 FPS` (`H.264`)
- **Audio:** Synchronized Indian English male narration (`AAC`, `44100 Hz`, Stereo)
- **File Size:** `~19.6 MB`

---

## AI Tools Disclosure

AI assistance was used for scripting structure, Manim Python animation code generation/refinement, and neural text-to-speech voiceover synthesis (`edge-tts`). All mathematical definitions, derivations, calculations, and educational explanations were reviewed and verified against standard university calculus references.

---

## Academic References

- Stewart, J. (2016). *Calculus: Early Transcendentals* (8th Edition). Cengage Learning.
- Manim Community Edition Documentation: https://docs.manim.community/
- 3Blue1Brown — *Essence of Calculus* (visual intuition inspiration)
