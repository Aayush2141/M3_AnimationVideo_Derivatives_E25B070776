"""
Scene 3: Secant to Tangent Animation (1:10 – 2:15, ~65s)
B approaches A through many intermediate positions on y = x²,
showing h and secant slope, why secant becomes tangent,
and distinguishing average vs instantaneous rate of change.
"""

from manim import *
import numpy as np

BG_COLOR      = "#0A0E1A"
ACCENT_GOLD   = "#FFD700"
ACCENT_CYAN   = "#00D4FF"
ACCENT_GREEN  = "#39FF14"
ACCENT_PINK   = "#FF6B9D"
WHITE_SOFT    = "#E8EEF4"
SECANT_COLOR  = "#FF6B9D"
TANGENT_COLOR = "#FFD700"


def secant_endpoints(axes, x_a, x_b, ext=0.8):
    ya = x_a ** 2
    if abs(x_b - x_a) < 1e-9:
        slope = 2 * x_a
    else:
        slope = (x_b**2 - ya) / (x_b - x_a)
    x_l = x_a - ext
    x_r = max(x_b, x_a) + ext
    return axes.c2p(x_l, ya + slope*(x_l-x_a)), axes.c2p(x_r, ya + slope*(x_r-x_a))


class Scene3SecantTangent(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        header = Text("Secant Line → Tangent Line",
                      color=ACCENT_GOLD, font_size=38, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(FadeIn(header, shift=DOWN * 0.3), run_time=0.7)

        # ── Axes ──────────────────────────────────────────────────────────
        axes = Axes(
            x_range=[-0.3, 5.0, 1],
            y_range=[-0.5, 18, 2],
            x_length=5.8,
            y_length=4.8,
            axis_config={
                "color": ACCENT_CYAN, "stroke_width": 2,
                "include_numbers": True,
                "font_size": 19,
                "label_constructor": Text,
                "decimal_number_config": {
                    "num_decimal_places": 0,
                    "color": WHITE_SOFT,
                },
            },
            tips=False,
        ).shift(RIGHT * 1.6 + DOWN * 0.35)

        x_lbl = Text("x", font_size=22, color=ACCENT_CYAN).next_to(axes.x_axis, RIGHT, buff=0.1)
        y_lbl = Text("y", font_size=22, color=ACCENT_CYAN).next_to(axes.y_axis, UP,    buff=0.1)
        parabola = axes.plot(lambda x: x**2, x_range=[-0.2, 4.1],
                             color=ACCENT_GREEN, stroke_width=3)
        f_lbl = Text("y = x²", font_size=26, color=ACCENT_GREEN
                     ).move_to(axes.c2p(1.8, 15.5))

        self.play(Create(axes), FadeIn(x_lbl, y_lbl), run_time=1.0)
        self.play(Create(parabola), Write(f_lbl), run_time=1.0)

        # ── A fixed at x=2, B starts at x=4 ─────────────────────────────
        x_a = 2.0
        b_tracker = ValueTracker(4.0)

        dotA = Dot(axes.c2p(x_a, x_a**2), color=ACCENT_CYAN, radius=0.11)
        dotB = always_redraw(lambda: Dot(
            axes.c2p(b_tracker.get_value(), b_tracker.get_value()**2),
            color=ACCENT_PINK, radius=0.11,
        ))

        lblA = Text("A=(2, 4)", font_size=20, color=ACCENT_CYAN
                    ).next_to(axes.c2p(x_a, x_a**2), DL, buff=0.12)

        lblB = always_redraw(lambda: Text(
            f"B=({b_tracker.get_value():.2f}, {b_tracker.get_value()**2:.2f})",
            font_size=18, color=ACCENT_PINK,
        ).next_to(axes.c2p(b_tracker.get_value(), b_tracker.get_value()**2), UR, buff=0.1))

        self.play(FadeIn(dotA, lblA), run_time=0.6)
        self.play(FadeIn(dotB, lblB), run_time=0.6)

        # ── Secant line (always redrawn) ──────────────────────────────────
        secant = always_redraw(lambda: Line(
            *secant_endpoints(axes, x_a, b_tracker.get_value(), ext=0.6),
            color=SECANT_COLOR, stroke_width=2.5,
        ))

        # ── Live slope & gap display ──────────────────────────────────────
        def slope_val():
            bv = b_tracker.get_value()
            return (bv**2 - x_a**2) / (bv - x_a) if abs(bv - x_a) > 1e-9 else 2*x_a

        formula_lbl = Text("Slope = (y₂ - y₁) / (x₂ - x₁)", font_size=20, color=WHITE_SOFT
                           ).to_edge(LEFT, buff=0.4).shift(UP * 1.85)

        init_calc = Text("(16 - 4) / (4 - 2) = 12 / 2 = 6", font_size=20, color=ACCENT_CYAN
                         ).to_edge(LEFT, buff=0.4).shift(UP * 1.3)

        slope_label = always_redraw(lambda: Text(
            f"Slope = {slope_val():.3f}",
            font_size=26, color=ACCENT_GOLD, weight=BOLD,
        ).to_edge(LEFT, buff=0.4).shift(UP * 0.75))

        gap_label = always_redraw(lambda: Text(
            f"Gap h = {b_tracker.get_value() - x_a:.3f}",
            font_size=20, color=ACCENT_PINK,
        ).to_edge(LEFT, buff=0.4).shift(UP * 0.25))

        self.play(Create(secant), run_time=0.8)
        self.play(FadeIn(formula_lbl, init_calc), run_time=0.8)
        self.wait(15.17)
        self.play(FadeOut(init_calc), FadeIn(slope_label, gap_label), run_time=0.7)
        self.wait(2.2)

        # ── Convergence log with 8 intermediate steps ─────────────────────
        log_header = Text("B approaching A (h → 0):", font_size=18, color=WHITE_SOFT
                          ).to_edge(LEFT, buff=0.4).shift(DOWN * 0.28)
        self.play(FadeIn(log_header), run_time=0.4)

        b_steps = [
            (3.5,   "h=1.50  |  x_B=3.50  →  5.50"),
            (3.0,   "h=1.00  |  x_B=3.00  →  5.00"),
            (2.5,   "h=0.50  |  x_B=2.50  →  4.50"),
            (2.2,   "h=0.20  |  x_B=2.20  →  4.20"),
            (2.1,   "h=0.10  |  x_B=2.10  →  4.10"),
            (2.05,  "h=0.05  |  x_B=2.05  →  4.05"),
            (2.01,  "h=0.01  |  x_B=2.01  →  4.01"),
            (2.001, "h→0.00  |  x_B→2.00  →  4.00"),
        ]
        log_items = VGroup()
        for idx, (bv, txt) in enumerate(b_steps):
            self.play(b_tracker.animate.set_value(bv), run_time=1.35, rate_func=smooth)
            entry = Text(txt, font_size=16, color=ACCENT_CYAN if idx < len(b_steps) - 1 else ACCENT_GOLD)
            entry.to_edge(LEFT, buff=0.4).shift(DOWN * (0.65 + idx * 0.30))
            log_items.add(entry)
            self.play(FadeIn(entry, shift=RIGHT * 0.2), run_time=0.35)
            self.wait(0.70)

        self.wait(2.01)

        self.play(FadeOut(formula_lbl, slope_label, gap_label, log_header, log_items), run_time=0.6)
        tangent_line = axes.plot(lambda x: 4*x - 4, x_range=[0.5, 3.8],
                                 color=TANGENT_COLOR, stroke_width=3.5)
        tangent_lbl = Text("Tangent at A", font_size=22, color=TANGENT_COLOR
                           ).move_to(axes.c2p(3.6, 8.0))

        t_p1 = axes.c2p(2, 4)
        t_p2 = axes.c2p(3, 4)
        t_p3 = axes.c2p(3, 8)
        tri_h = DashedLine(t_p1, t_p2, color=ACCENT_CYAN, stroke_width=2)
        tri_v = DashedLine(t_p2, t_p3, color=ACCENT_GOLD, stroke_width=2)
        tri_hl = Text("+1", font_size=18, color=ACCENT_CYAN).next_to(tri_h, DOWN, buff=0.08)
        tri_vl = Text("+4", font_size=18, color=ACCENT_GOLD).next_to(tri_v, RIGHT, buff=0.08)

        self.play(
            Create(tangent_line),
            Write(tangent_lbl),
            FadeOut(secant, lblB, dotB),
            run_time=1.2,
        )
        self.play(Create(tri_h), Create(tri_v), FadeIn(tri_hl, tri_vl), run_time=1.0)
        self.wait(12.37)

        self.play(FadeOut(formula_lbl, slope_label, gap_label, log_header, log_items), run_time=0.6)

        # ── Result box + Average vs Instantaneous distinction ─────────────
        result_lines = VGroup(
            Text("Instantaneous\nRate of Change", font_size=22, color=WHITE_SOFT, line_spacing=1.2),
            Text("f'(2)  =  4", font_size=38, color=ACCENT_GOLD, weight=BOLD),
        ).arrange(DOWN, buff=0.22).to_edge(LEFT, buff=0.4).shift(UP * 1.1)

        surround = SurroundingRectangle(result_lines, color=ACCENT_GOLD,
                                        buff=0.2, corner_radius=0.15)

        self.play(Write(result_lines), Create(surround), run_time=1.2)
        self.wait(1.5)

        distinction = VGroup(
            Text("Average Rate (Secant):", font_size=18, color=ACCENT_PINK, weight=BOLD),
            Text("Between 2 points (h > 0)", font_size=17, color=WHITE_SOFT),
            Text("Instantaneous Rate (Tangent):", font_size=18, color=ACCENT_GOLD, weight=BOLD),
            Text("At 1 point as h → 0", font_size=17, color=WHITE_SOFT),
        ).arrange(DOWN, buff=0.16, aligned_edge=LEFT).to_edge(LEFT, buff=0.4).shift(DOWN * 1.65)

        self.play(FadeIn(distinction, shift=UP * 0.2), run_time=1.0)
        self.wait(12.12)

        self.play(
            FadeOut(header, axes, x_lbl, y_lbl, parabola, f_lbl,
                    dotA, lblA, tangent_line, tangent_lbl,
                    tri_h, tri_v, tri_hl, tri_vl,
                    result_lines, surround, distinction),
            run_time=0.8,
        )
