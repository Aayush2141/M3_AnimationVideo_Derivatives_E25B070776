# Storyboard – Derivatives and Rate of Change
### M3 Internal Assessment Animation

---

## Scene 1 — Opening Hook (0:00–0:30)

| Frame | Visual | Text/Formula | Narration Cue |
|-------|--------|-------------|---------------|
| 1a | Black screen → text fades in | "How can we calculate the exact rate…" | Opening question |
| 1b | 🚗 car icon + speedometer animation | "speed changes every instant" | Car speed example |
| 1c | Simple parabola sketch | f(x) = x² | Transition to math |
| 1d | Full title card | DERIVATIVES & RATE OF CHANGE / From Average Rate to Instantaneous Rate | Topic introduction |

**Key animation:** Text fade-in with upward drift; speedometer number count-up; parabola draw-on; title bold reveal.

---

## Scene 2 — Understanding the Concept (0:30–1:00)

| Frame | Visual | Text/Formula | Narration Cue |
|-------|--------|-------------|---------------|
| 2a | Section header appears | "Understanding the Concept" | Scene intro |
| 2b | Coordinate axes draw in | x-axis, y-axis | Setting up graph |
| 2c | Parabola draws | f(x) = x² | Introduce function |
| 2d | Vertical drop to point (2,4) | (2, 4) highlighted | Mapping x to y |
| 2e | Two points A, B on curve | A, B marked | Secant concept |
| 2f | Secant line drawn | slope line | Average rate |
| 2g | Formula appears | [f(b)−f(a)] / (b−a) | Average rate formula |

**Key animation:** Sequential appear of axes → curve → points → secant → formula.

---

## Scene 3 — Secant to Tangent (1:00–2:00)

| Frame | Visual | Text/Formula | Narration Cue |
|-------|--------|-------------|---------------|
| 3a | Axes + parabola | y = x² | Setup |
| 3b | A=(2,4), B=(4,16) placed | Coordinates labeled | "Place two points" |
| 3c | Secant drawn | slope = (16-4)/(4-2) = 6 | Calculate first slope |
| 3d–3h | B moves: 3.5, 3, 2.5, 2.1, 2.01 | Slope: 5, 4.5, 4.1, 4.01 | B approaches A |
| 3i | Secant becomes golden tangent | Tangent at A | "Remarkable thing happens" |
| 3j | Result box | f'(2) = 4 | Instantaneous rate = 4 |

**Key animation:** `ValueTracker` drives B's x-position; `always_redraw` updates secant and slope display continuously.

---

## Scene 4 — Mathematical Derivation (2:00–3:30)

| Frame | Visual | Formula | Narration Cue |
|-------|--------|---------|---------------|
| 4a | Header + definition | f'(x) = lim[h→0] [f(x+h)−f(x)]/h | "First principles" |
| 4b | Warning panel | 0/0 problem | "Can't set h=0 yet" |
| 4c | Step 1 | [(x+h)²−x²]/h | Substitute f |
| 4d | Step 2 | [x²+2xh+h²−x²]/h | Expand (x+h)² |
| 4e | Step 3 | [2xh+h²]/h | Cancel x² |
| 4f | Step 4 | h(2x+h)/h | Factor h |
| 4g | Step 5 | lim(2x+h) | Cancel h |
| 4h | Final result (boxed, gold) | f'(x) = 2x | "The derivative is 2x" |

**Key animation:** `TransformMatchingShapes` morphs each equation step into the next.

---

## Scene 5 — Interpretation (3:30–4:30)

| Frame | Visual | Formula | Narration Cue |
|-------|--------|---------|---------------|
| 5a | Parabola reappears | y = x² | Return to graph |
| 5b | Point (2,4) highlighted with dashes | (2, 4) | "Our specific point" |
| 5c | Derivative evaluation | f'(2) = 2×2 = 4 | "What is f'(2)?" |
| 5d | Tangent line animates | y = 4x − 4 | Tangent drawn |
| 5e | Equation derivation | y−4 = 4(x−2) → y=4x−4 | "Using point-slope form" |
| 5f | Real-world connection | (car speedometer reference) | Connect to intro |

**Key animation:** Dashed crosshairs → dot highlight → derivative steps → tangent line creation.

---

## Scene 6 — Summary and Credits (4:30–5:00)

| Frame | Visual | Content | Narration Cue |
|-------|--------|---------|---------------|
| 6a | "Summary" header | — | Scene intro |
| 6b–6d | 3 concepts appear sequentially | 1. Secant = average / 2. Tangent = instant / 3. Derivative measures instant | Three key ideas |
| 6e | Horizontal divider | — | — |
| 6f | Formula trio | f(x)=x² / f'(x)=2x / f'(2)=4 | Recap formulas |
| 6g | Credits screen | Name, ID, Topic, References, AI Disclosure | Closing |

**Key animation:** Fade-in concepts one by one, horizontal rule, formula write-on, credits fade.

---

## Colour Coding Reference

| Object | Colour |
|--------|--------|
| Background | `#0A0E1A` navy |
| Parabola curve | `#39FF14` neon green |
| Tangent line | `#FFD700` gold |
| Secant line / points | `#FF6B9D` pink |
| Axes / formulas | `#00D4FF` cyan |
| Titles / results | `#FFD700` gold |
| Body text | `#E8EEF4` soft white |

---

*Storyboard for M3 Internal Assessment — Derivatives and Rate of Change*
