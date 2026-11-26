"""
Scene 5: Interpretation and Worked Example (3:30 – 4:25, ~55s)
Calculate f'(2) = 4, geometric meaning of tangent slope, derive y = 4x - 4,
connect to car speed, and add second worked example at x = 3 (f'(3) = 6).
"""

from manim import *

BG_COLOR      = "#0A0E1A"
ACCENT_GOLD   = "#FFD700"
ACCENT_CYAN   = "#00D4FF"
ACCENT_GREEN  = "#39FF14"
ACCENT_PINK   = "#FF6B9D"
WHITE_SOFT    = "#E8EEF4"
TANGENT_COLOR = "#FFD700"


class Scene5Interpretation(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        header = Text("Interpreting the Derivative",
                      color=ACCENT_GOLD, font_size=38, weight=BOLD).to_edge(UP, buff=0.35)
        self.play(FadeIn(header, shift=DOWN * 0.3), run_time=0.7)

        # ── Axes ──────────────────────────────────────────────────────────
        axes = Axes(
            x_range=[-0.3, 4.5, 1],
            y_range=[-1, 18, 2],
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
        ).shift(RIGHT * 1.5 + DOWN * 0.35)

        x_lbl = Text("x", font_size=22, color=ACCENT_CYAN).next_to(axes.x_axis, RIGHT, buff=0.1)
        y_lbl = Text("y", font_size=22, color=ACCENT_CYAN).next_to(axes.y_axis, UP, buff=0.1)
        parabola = axes.plot(lambda x: x**2, x_range=[-0.2, 4.1], color=ACCENT_GREEN, stroke_width=3)
        f_lbl = Text("f(x) = x²", font_size=24, color=ACCENT_GREEN
                     ).move_to(axes.c2p(1.6, 15.5))

        self.play(Create(axes), FadeIn(x_lbl, y_lbl), run_time=1.0)
        self.play(Create(parabola), Write(f_lbl), run_time=1.1)

        # ── 1. Highlight (2, 4) & evaluate f'(2) = 4 ─────────────────────
        pt = axes.c2p(2, 4)
        dot_pt  = Dot(pt, color=ACCENT_PINK, radius=0.12)
        coord_l = Text("(2, 4)", font_size=24, color=ACCENT_PINK).next_to(dot_pt, UL, buff=0.12)
        v_line  = DashedLine(axes.c2p(2, 0), axes.c2p(2, 4), color=ACCENT_PINK, stroke_width=1.5)
        h_line  = DashedLine(axes.c2p(0, 4), axes.c2p(2, 4), color=ACCENT_PINK, stroke_width=1.5)

        self.play(Create(v_line), Create(h_line), run_time=0.8)
        self.play(FadeIn(dot_pt), Write(coord_l), run_time=0.7)
        self.play(Indicate(dot_pt, color=ACCENT_GOLD, scale_factor=1.4), run_time=1.0)
        self.wait(2.0)

        deriv_steps = VGroup(
            Text("f'(x)  =  2x", font_size=25, color=WHITE_SOFT),
            Text("f'(2)  =  2 × 2", font_size=25, color=WHITE_SOFT),
            Text("f'(2)  =  4", font_size=36, color=ACCENT_GOLD, weight=BOLD),
        ).arrange(DOWN, buff=0.25).to_edge(LEFT, buff=0.4).shift(UP * 1.15)

        for s in deriv_steps:
            self.play(Write(s), run_time=0.8)
            self.wait(1.0)

        box_d = SurroundingRectangle(deriv_steps[2], color=ACCENT_GOLD, buff=0.15, corner_radius=0.1)
        self.play(Create(box_d), run_time=0.5)
        self.wait(1.81)

        # ── 2. Tangent line & slope triangle ──────────────────────────────
        tangent = axes.plot(lambda x: 4*x - 4, x_range=[0.6, 3.6],
                            color=TANGENT_COLOR, stroke_width=3)
        self.play(Create(tangent), run_time=1.2)

        t_p1 = axes.c2p(2, 4)
        t_p2 = axes.c2p(3, 4)
        t_p3 = axes.c2p(3, 8)
        tri_h = DashedLine(t_p1, t_p2, color=ACCENT_CYAN, stroke_width=2)
        tri_v = DashedLine(t_p2, t_p3, color=ACCENT_GOLD, stroke_width=2)
        tri_hl = Text("+1", font_size=18, color=ACCENT_CYAN).next_to(tri_h, DOWN, buff=0.08)
        tri_vl = Text("+4", font_size=18, color=ACCENT_GOLD).next_to(tri_v, RIGHT, buff=0.08)
        self.play(Create(tri_h), Create(tri_v), FadeIn(tri_hl, tri_vl), run_time=1.0)
        self.wait(3.5)

        # ── 3. Tangent equation derivation ────────────────────────────────
        eq_steps = VGroup(
            Text("y - y₁  =  m(x - x₁)", font_size=21, color=WHITE_SOFT),
            Text("y - 4  =  4(x - 2)", font_size=23, color=ACCENT_CYAN),
            Text("∴  y  =  4x - 4", font_size=27, color=ACCENT_GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.22).to_edge(LEFT, buff=0.4).shift(DOWN * 0.85)

        for eq in eq_steps:
            self.play(Write(eq), run_time=0.85)
            self.wait(1.5)

        slope_note = Text("slope = 4", font_size=21, color=TANGENT_COLOR
                          ).move_to(axes.c2p(3.6, 10.6))
        self.play(FadeIn(slope_note, shift=LEFT * 0.3), run_time=0.6)
        self.wait(10.70)

        # ── 4. Real-world car connection ──────────────────────────────────
        rw = Text(
            "At x = 2, y rises at 4 units per x —\njust like the car's speedometer reading!",
            font_size=19, color=WHITE_SOFT, line_spacing=1.3,
        ).to_edge(LEFT, buff=0.4).shift(DOWN * 2.55)

        self.play(FadeIn(rw, shift=UP * 0.2), run_time=1.0)
        self.wait(10.07)

        # ── 5. Additional example at x = 3: f'(3) = 6 ─────────────────────
        self.play(
            FadeOut(deriv_steps, box_d, eq_steps, rw, tri_h, tri_v, tri_hl, tri_vl),
            run_time=0.6,
        )

        pt3 = axes.c2p(3, 9)
        dot3 = Dot(pt3, color=ACCENT_CYAN, radius=0.12)
        lbl3 = Text("(3, 9)", font_size=24, color=ACCENT_CYAN).next_to(dot3, UL, buff=0.12)
        tangent3 = axes.plot(lambda x: 6*x - 9, x_range=[1.5, 4.1],
                             color=ACCENT_CYAN, stroke_width=3)
        slope3_note = Text("slope = 6", font_size=21, color=ACCENT_CYAN
                           ).move_to(axes.c2p(3.8, 15.2))

        ex3_panel = VGroup(
            Text("Another Point: x = 3", font_size=24, color=ACCENT_CYAN, weight=BOLD),
            Text("Point on curve:  (3, 9)", font_size=21, color=WHITE_SOFT),
            Text("f'(3)  =  2 × 3  =  6", font_size=30, color=ACCENT_GOLD, weight=BOLD),
            Text("Tangent:  y - 9 = 6(x - 3)\n              y = 6x - 9", font_size=20, color=ACCENT_GREEN, line_spacing=1.25),
            Text("Steeper curve → larger slope\n(6 > 4)", font_size=20, color=WHITE_SOFT, line_spacing=1.25),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT).to_edge(LEFT, buff=0.4).shift(DOWN * 0.1)

        self.play(FadeIn(dot3), Write(lbl3), run_time=0.8)
        self.play(Create(tangent3), FadeIn(slope3_note), run_time=1.1)
        for item in ex3_panel:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.75)
            self.wait(1.5)

        self.wait(9.13)

        self.play(
            FadeOut(header, axes, x_lbl, y_lbl, parabola, f_lbl,
                    dot_pt, coord_l, v_line, h_line, tangent, slope_note,
                    dot3, lbl3, tangent3, slope3_note, ex3_panel),
            run_time=0.8,
        )
