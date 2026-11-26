"""
Scene 1: Opening Hook (0:00 - 0:30, ~30s)
Engaging question, average vs instantaneous speed with car & speedometer,
transition to f(x)=x² and derivatives, title display.
"""

from manim import *

BG_COLOR      = "#0A0E1A"
ACCENT_GOLD   = "#FFD700"
ACCENT_CYAN   = "#00D4FF"
ACCENT_GREEN  = "#39FF14"
ACCENT_PINK   = "#FF6B9D"
WHITE_SOFT    = "#E8EEF4"


class Scene1Intro(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # ── 1. Opening question (~5.5s) ───────────────────────────────────
        q_line1 = Text("How can we calculate the", font_size=42, color=WHITE_SOFT)
        q_line2 = Text("exact rate at which something", font_size=42, color=ACCENT_GOLD)
        q_line3 = Text("changes at one particular instant?", font_size=42, color=ACCENT_CYAN)
        question = VGroup(q_line1, q_line2, q_line3).arrange(DOWN, buff=0.25).scale(0.9).move_to(ORIGIN)

        underline = Underline(question, color=ACCENT_GOLD, buff=0.15)

        self.play(FadeIn(question, shift=UP * 0.4), run_time=1.4)
        self.play(Create(underline), run_time=0.8)
        self.wait(8.03)
        self.play(FadeOut(question, underline, shift=UP * 0.5), run_time=0.7)

        # ── 2. Car speed example: Average vs Instantaneous (~12.5s) ───────
        body    = Rectangle(width=2.4, height=0.9,
                            color=ACCENT_CYAN, fill_color="#0A1A2E", fill_opacity=1, stroke_width=2.5)
        roof    = Rectangle(width=1.4, height=0.6,
                            color=ACCENT_CYAN, fill_color="#0D2040", fill_opacity=1, stroke_width=2
                            ).shift(UP * 0.65)
        wheel_l = Circle(radius=0.28, color=WHITE_SOFT,
                         fill_color="#222222", fill_opacity=1, stroke_width=2).shift(LEFT * 0.75 + DOWN * 0.45)
        wheel_r = Circle(radius=0.28, color=WHITE_SOFT,
                         fill_color="#222222", fill_opacity=1, stroke_width=2).shift(RIGHT * 0.75 + DOWN * 0.45)
        car_txt = Text("CAR", font_size=20, color=ACCENT_CYAN, weight=BOLD)
        car_icon = VGroup(body, roof, wheel_l, wheel_r, car_txt).shift(LEFT * 4.2 + UP * 0.5)

        ring     = Circle(radius=0.9, color=ACCENT_CYAN, stroke_width=3).shift(RIGHT * 0.6 + UP * 0.5)
        spd_num  = Text("0", font_size=28, color=ACCENT_GOLD).move_to(ring.get_center())
        km_lbl   = Text("km/h", font_size=20, color=WHITE_SOFT).next_to(ring, DOWN, buff=0.15)

        ex_line1 = Text("A car's speed changes every instant.", font_size=25, color=WHITE_SOFT)
        ex_line2 = Text("At exactly  t = 3 s,  what is its speed?", font_size=25, color=ACCENT_CYAN)
        ex_text  = VGroup(ex_line1, ex_line2).arrange(DOWN, buff=0.18).shift(DOWN * 1.35)

        self.play(FadeIn(car_icon, shift=RIGHT * 0.4), run_time=0.7)
        self.play(Create(ring), FadeIn(spd_num, km_lbl), run_time=0.8)
        self.play(Write(ex_text), run_time=1.1)

        for v in [0, 20, 45, 72, 95, 60]:
            new = Text(str(v), font_size=28, color=ACCENT_GOLD).move_to(ring.get_center())
            self.play(Transform(spd_num, new), run_time=0.25)
        self.wait(12.34)

        # Average vs Instantaneous Speed comparison cards
        avg_card = VGroup(
            Text("Average Speed", font_size=22, color=ACCENT_PINK, weight=BOLD),
            Text("Total Distance / Total Time\n(over an interval)", font_size=18, color=WHITE_SOFT, line_spacing=1.25),
        ).arrange(DOWN, buff=0.12).to_edge(LEFT, buff=0.8).shift(DOWN * 2.7)

        inst_card = VGroup(
            Text("Instantaneous Speed", font_size=22, color=ACCENT_GREEN, weight=BOLD),
            Text("Speedometer reading at t = 3 s\n(at one exact instant)", font_size=18, color=WHITE_SOFT, line_spacing=1.25),
        ).arrange(DOWN, buff=0.12).to_edge(RIGHT, buff=0.8).shift(DOWN * 2.7)

        self.play(FadeIn(avg_card, shift=UP * 0.2), run_time=0.8)
        self.wait(1.0)
        self.play(FadeIn(inst_card, shift=UP * 0.2), run_time=0.8)
        self.wait(13.72)

        self.play(FadeOut(car_icon, ring, spd_num, km_lbl, ex_text, avg_card, inst_card), run_time=0.7)

        # ── 3. Quick parabola sketch + derivative intro (~6.0s) ───────────
        axes = Axes(
            x_range=[-0.3, 3.5, 1], y_range=[-0.5, 10, 2],
            x_length=5, y_length=4,
            axis_config={"color": ACCENT_CYAN, "stroke_width": 2},
            tips=False,
        ).shift(LEFT * 1.5 + DOWN * 0.3)

        parabola = axes.plot(lambda x: x**2, x_range=[0, 3.1], color=ACCENT_GREEN, stroke_width=3)
        f_lbl    = Text("f(x) = x²", font_size=34, color=ACCENT_GREEN).next_to(axes, RIGHT, buff=0.5).shift(UP * 0.6)
        deriv_intro = Text(
            "Derivatives measure\ninstantaneous rate of change.",
            font_size=22, color=ACCENT_GOLD, line_spacing=1.3,
        ).next_to(f_lbl, DOWN, buff=0.4).align_to(f_lbl, LEFT)

        self.play(Create(axes), run_time=0.9)
        self.play(Create(parabola), run_time=1.1)
        self.play(Write(f_lbl), run_time=0.7)
        self.play(FadeIn(deriv_intro, shift=UP * 0.2), run_time=0.8)
        self.wait(1.6)
        self.play(FadeOut(axes, parabola, f_lbl, deriv_intro, shift=LEFT * 0.5), run_time=0.8)

        # ── 4. Title card (~6.0s) ─────────────────────────────────────────
        t_line1  = Text("DERIVATIVES &", font_size=64, color=ACCENT_GOLD, weight=BOLD)
        t_line2  = Text("RATE OF CHANGE", font_size=64, color=ACCENT_GOLD, weight=BOLD)
        title    = VGroup(t_line1, t_line2).arrange(DOWN, buff=0.15).move_to(UP * 0.5)
        deco     = Line(LEFT * 4.5, RIGHT * 4.5, color=ACCENT_GOLD, stroke_width=2).next_to(title, DOWN, buff=0.15)
        subtitle = Text("From Average Rate to Instantaneous Rate",
                        font_size=28, color=ACCENT_CYAN).next_to(title, DOWN, buff=0.5)

        self.play(Write(title), run_time=1.4)
        self.play(Create(deco), run_time=0.5)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.9)
        self.wait(2.01)
        self.play(FadeOut(title, deco, subtitle), run_time=0.8)
