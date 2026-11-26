"""
Scene 2: Concept Introduction (0:30 – 1:10, ~40s)
Introduce f(x)=x², sample points, rise/run/slope, secant line meaning,
and a numerical average rate of change example.
"""

from manim import *

BG_COLOR     = "#0A0E1A"
ACCENT_GOLD  = "#FFD700"
ACCENT_CYAN  = "#00D4FF"
ACCENT_GREEN = "#39FF14"
ACCENT_PINK  = "#FF6B9D"
WHITE_SOFT   = "#E8EEF4"
SECANT_COLOR = "#FF6B9D"


class Scene2Concept(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # ── Section header ────────────────────────────────────────────────
        header = Text("Understanding the Concept", color=ACCENT_GOLD,
                      font_size=38, weight=BOLD).to_edge(UP, buff=0.4)
        self.play(FadeIn(header, shift=DOWN * 0.3), run_time=0.7)

        # ── Axes & parabola ───────────────────────────────────────────────
        axes = Axes(
            x_range=[-0.3, 4.5, 1],
            y_range=[-0.5, 16, 2],
            x_length=5.8,
            y_length=4.8,
            axis_config={
                "color": ACCENT_CYAN, "stroke_width": 2,
                "include_numbers": True,
                "font_size": 20,
                "label_constructor": Text,
                "decimal_number_config": {
                    "num_decimal_places": 0,
                    "color": WHITE_SOFT,
                },
            },
            tips=False,
        ).shift(RIGHT * 1.6 + DOWN * 0.35)

        x_label = Text("x", font_size=24, color=ACCENT_CYAN).next_to(axes.x_axis, RIGHT, buff=0.1)
        y_label = Text("y", font_size=24, color=ACCENT_CYAN).next_to(axes.y_axis, UP, buff=0.1)

        parabola = axes.plot(lambda x: x**2, x_range=[-0.2, 4.0], color=ACCENT_GREEN, stroke_width=3)
        func_label = Text("f(x) = x²", font_size=28, color=ACCENT_GREEN
                          ).move_to(axes.c2p(2.2, 14.5))

        self.play(Create(axes), FadeIn(x_label, y_label), run_time=1.0)
        self.play(Create(parabola), run_time=1.2)
        self.play(Write(func_label), run_time=0.7)

        # ── 1. Function mapping & sample points ───────────────────────────
        annot1 = Text(
            "A function maps each x\nto exactly one y = x²:\n  f(1) = 1,  f(2) = 4,  f(3) = 9",
            font_size=21, color=WHITE_SOFT, line_spacing=1.35,
        ).to_edge(LEFT, buff=0.4).shift(UP * 0.9)

        self.play(FadeIn(annot1, shift=RIGHT * 0.3), run_time=0.8)

        sample_pts = [(1, 1), (2, 4), (3, 9)]
        sample_dots = VGroup()
        sample_lbls = VGroup()
        for sx, sy in sample_pts:
            d = Dot(axes.c2p(sx, sy), color=ACCENT_GOLD, radius=0.08)
            l = Text(f"({sx}, {sy})", font_size=18, color=ACCENT_GOLD).next_to(d, DR, buff=0.08)
            sample_dots.add(d)
            sample_lbls.add(l)

        arrow_x = axes.get_vertical_line(axes.c2p(2, 4), color=ACCENT_GOLD, stroke_width=2)
        self.play(FadeIn(sample_dots, sample_lbls), Create(arrow_x), run_time=1.2)
        self.wait(7.75)

        self.play(FadeOut(annot1, sample_dots, sample_lbls, arrow_x), run_time=0.6)

        # ── 2. Rate of change & slope explanation ─────────────────────────
        annot2 = Text(
            "Rate of change measures\nhow fast y changes\nfor each unit increase in x.\n\nGeometrically, this is SLOPE.",
            font_size=21, color=WHITE_SOFT, line_spacing=1.35,
        ).to_edge(LEFT, buff=0.4).shift(UP * 0.7)
        self.play(FadeIn(annot2, shift=RIGHT * 0.3), run_time=0.9)
        self.wait(8.70)

        # ── 3. Two points, secant line, & rise/run triangle ───────────────
        a_val, b_val = 1.0, 3.0
        pA = axes.c2p(a_val, a_val**2)
        pB = axes.c2p(b_val, b_val**2)
        pC = axes.c2p(b_val, a_val**2)

        dotA = Dot(pA, color=ACCENT_PINK, radius=0.11)
        dotB = Dot(pB, color=ACCENT_PINK, radius=0.11)
        labelA = Text("A (1, 1)", font_size=18, color=ACCENT_PINK).next_to(dotA, UL, buff=0.08)
        labelB = Text("B (3, 9)", font_size=18, color=ACCENT_PINK).next_to(dotB, UR, buff=0.1)

        secant = Line(axes.c2p(0.5, -1.0), axes.c2p(3.6, 11.4), color=SECANT_COLOR, stroke_width=2.8)
        run_line  = DashedLine(pA, pC, color=ACCENT_CYAN, stroke_width=2)
        rise_line = DashedLine(pC, pB, color=ACCENT_GOLD, stroke_width=2)
        run_lbl   = Text("Run = b - a", font_size=17, color=ACCENT_CYAN).next_to(run_line, UP, buff=0.08)
        rise_lbl  = Text("Rise = f(b) - f(a)", font_size=17, color=ACCENT_GOLD).next_to(rise_line, RIGHT, buff=0.1)

        self.play(FadeIn(dotA, dotB, labelA, labelB), run_time=0.8)
        self.play(Create(secant), run_time=0.8)

        secant_def = Text(
            "A secant line connects\ntwo points on a curve.",
            font_size=20, color=SECANT_COLOR, line_spacing=1.25,
        ).to_edge(LEFT, buff=0.4).shift(DOWN * 1.1)

        self.play(FadeIn(secant_def, shift=UP * 0.2), run_time=0.7)
        self.play(Create(run_line), Create(rise_line), FadeIn(run_lbl, rise_lbl), run_time=1.0)
        self.wait(13.56)

        self.play(FadeOut(annot2, secant_def), run_time=0.5)

        # ── 4. Average rate formula + numerical example ───────────────────
        formula = Text(
            "Average Rate =\n[f(b) - f(a)] / (b - a)",
            font_size=23, color=ACCENT_GOLD, line_spacing=1.35,
        ).to_edge(LEFT, buff=0.4).shift(UP * 1.2)

        brace_label = Text(
            "= Rise / Run\n= Slope of the secant line",
            font_size=19, color=SECANT_COLOR, line_spacing=1.3,
        ).next_to(formula, DOWN, buff=0.25).align_to(formula, LEFT)

        num_example = VGroup(
            Text("Example (a = 1, b = 3):", font_size=20, color=ACCENT_CYAN, weight=BOLD),
            Text("[f(3) - f(1)] / (3 - 1)", font_size=20, color=WHITE_SOFT),
            Text("= (9 - 1) / 2  =  8 / 2  =  4", font_size=21, color=ACCENT_GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.18, aligned_edge=LEFT).to_edge(LEFT, buff=0.4).shift(DOWN * 1.35)

        self.play(Write(formula), run_time=1.2)
        self.play(FadeIn(brace_label, shift=UP * 0.2), run_time=0.8)
        self.wait(2.8)
        self.play(FadeIn(num_example, shift=UP * 0.2), run_time=1.2)
        self.wait(14.14)

        self.play(
            FadeOut(header, axes, x_label, y_label, parabola, func_label,
                    dotA, dotB, labelA, labelB, secant,
                    run_line, rise_line, run_lbl, rise_lbl,
                    formula, brace_label, num_example),
            run_time=0.8,
        )
