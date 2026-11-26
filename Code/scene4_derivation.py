"""
Scene 4: First Principles Derivation (2:15 – 3:30, ~75s)
Connection from secant slope to difference quotient, why h=0 is undefined,
complete step-by-step algebraic derivation of f'(x) = 2x, and slope examples.
"""

from manim import *

BG_COLOR     = "#0A0E1A"
ACCENT_GOLD  = "#FFD700"
ACCENT_CYAN  = "#00D4FF"
ACCENT_GREEN = "#39FF14"
ACCENT_PINK  = "#FF6B9D"
WHITE_SOFT   = "#E8EEF4"


STEPS = [
    ("f'(x)  =  lim (h → 0)  [f(x + h) - f(x)] / h",
     "First-principles definition of the derivative",
     ACCENT_CYAN),

    ("Step 1:   f'(x)  =  lim (h → 0)  [(x + h)² - x²] / h",
     "Substitute  f(x) = x²  and  f(x + h) = (x + h)²",
     WHITE_SOFT),

    ("Step 2:   =  lim (h → 0)  [x² + 2xh + h² - x²] / h",
     "Expand  (x + h)²  =  x² + 2xh + h²",
     WHITE_SOFT),

    ("Step 3:   =  lim (h → 0)  [2xh + h²] / h",
     "Cancel  x²  and  -x²  in the numerator",
     ACCENT_GREEN),

    ("Step 4:   =  lim (h → 0)  [h(2x + h)] / h",
     "Factor out the common factor  h  from the numerator",
     WHITE_SOFT),

    ("Step 5:   =  lim (h → 0)  (2x + h)",
     "Cancel  h / h = 1  (valid because h → 0 means h ≠ 0)",
     ACCENT_GREEN),

    ("Result:   f'(x)  =  2x",
     "Now substitute  h = 0 :   2x + 0  =  2x",
     ACCENT_GOLD),
]


class Scene4Derivation(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # ── Header ────────────────────────────────────────────────────────
        header = Text("First Principles Derivation",
                      color=ACCENT_GOLD, font_size=40, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(FadeIn(header, shift=DOWN * 0.3), run_time=0.8)

        # ── 1. Setup: from secant slope to difference quotient ────────────
        setup_grp = VGroup(
            Text("Start with two points on  f(x) = x² :", font_size=26, color=WHITE_SOFT),
            Text("Point A: (x, f(x))     and     Point B: (x + h, f(x + h))", font_size=26, color=ACCENT_CYAN),
            Text("Run = (x + h) - x = h       |       Rise = f(x + h) - f(x)", font_size=24, color=ACCENT_GOLD),
            Text("Secant Slope  =  [f(x + h) - f(x)] / h", font_size=28, color=ACCENT_GREEN, weight=BOLD),
            Text("As  h → 0,  the secant slope becomes the derivative f'(x).", font_size=23, color=WHITE_SOFT),
        ).arrange(DOWN, buff=0.35).shift(UP * 0.1)

        self.play(FadeIn(setup_grp[0], shift=UP * 0.2), run_time=0.8)
        self.play(FadeIn(setup_grp[1], shift=UP * 0.2), run_time=0.9)
        self.wait(1.2)
        self.play(FadeIn(setup_grp[2], shift=UP * 0.2), run_time=0.9)
        self.play(Write(setup_grp[3]), run_time=1.0)
        self.wait(1.5)
        self.play(FadeIn(setup_grp[4], shift=UP * 0.2), run_time=0.8)
        self.wait(18.85)
        self.play(FadeOut(setup_grp), run_time=0.6)

        # ── 2. Why can't we set h=0 immediately? ─────────────────────────
        warning = VGroup(
            Text("Why can't we substitute  h = 0  immediately?", font_size=28, color=ACCENT_PINK, weight=BOLD),
            Text("[f(x + 0) - f(x)] / 0   =   0 / 0   →   Undefined!", font_size=26, color=ACCENT_PINK),
            Text("Division by zero has no mathematical meaning.", font_size=22, color=WHITE_SOFT),
            Text("Solution: Simplify algebraically while  h ≠ 0,  then take the limit.", font_size=22, color=ACCENT_CYAN),
        ).arrange(DOWN, buff=0.38).shift(UP * 0.15)

        self.play(FadeIn(warning[0], shift=UP * 0.2), run_time=0.9)
        self.play(Write(warning[1]), run_time=1.0)
        self.wait(1.5)
        self.play(FadeIn(warning[2], shift=UP * 0.15), run_time=0.8)
        self.play(FadeIn(warning[3], shift=UP * 0.15), run_time=0.9)
        self.wait(14.34)
        self.play(FadeOut(warning), run_time=0.6)

        # ── 3. Step-by-step derivation ────────────────────────────────────
        step_waits = [8.14, 6.95, 5.54, 7.72, 5.49, 10.24, 2.00]
        prev = None
        for i, (line_tex, note_tex, color) in enumerate(STEPS):
            is_final = (i == len(STEPS) - 1)
            font_sz  = 38 if is_final else 29

            step_text = Text(line_tex, font_size=font_sz, color=color).shift(UP * 0.55)
            note_text = Text(note_tex, font_size=22, color=ACCENT_CYAN).next_to(step_text, DOWN, buff=0.5)

            if prev is None:
                self.play(Write(step_text), run_time=1.3)
            else:
                self.play(ReplacementTransform(prev, step_text), run_time=1.1)

            self.play(FadeIn(note_text, shift=UP * 0.15), run_time=0.6)
            self.wait(step_waits[i])
            self.play(FadeOut(note_text), run_time=0.4)
            prev = step_text

        # ── 4. Final boxed result & slope machine ─────────────────────────
        result = Text("f'(x)  =  2x", font_size=56, color=ACCENT_GOLD, weight=BOLD)
        result.move_to(ORIGIN + UP * 0.6)
        box = SurroundingRectangle(result, color=ACCENT_GOLD, buff=0.3, corner_radius=0.15, stroke_width=3)

        self.play(ReplacementTransform(prev, result), run_time=0.9)
        self.play(Create(box), run_time=0.6)

        note_final = Text("The derivative of  x²  is  2x  for every point x",
                          font_size=24, color=WHITE_SOFT).next_to(box, DOWN, buff=0.45)

        examples = Text(
            "x = 1  →  f'(1) = 2      |      x = 2  →  f'(2) = 4      |      x = 3  →  f'(3) = 6",
            font_size=21, color=ACCENT_GREEN,
        ).next_to(note_final, DOWN, buff=0.45)

        self.play(FadeIn(note_final, shift=UP * 0.2), run_time=0.8)
        self.wait(1.2)
        self.play(FadeIn(examples, shift=UP * 0.2), run_time=0.9)
        self.wait(10.20)

        self.play(FadeOut(header, result, box, note_final, examples), run_time=0.8)
