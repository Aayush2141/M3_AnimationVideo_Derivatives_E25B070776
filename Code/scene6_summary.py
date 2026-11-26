"""
Scene 6: Summary and Credits (4:25 – 5:00, ~35s)
Summarize average rate, instantaneous rate, derivatives, key formulas,
student details (Aayush Singh / E25B070776), and professional thank-you screen.
"""

from manim import *

BG_COLOR     = "#0A0E1A"
ACCENT_GOLD  = "#FFD700"
ACCENT_CYAN  = "#00D4FF"
ACCENT_GREEN = "#39FF14"
ACCENT_PINK  = "#FF6B9D"
WHITE_SOFT   = "#E8EEF4"


class Scene6Summary(Scene):
    def construct(self):
        self.camera.background_color = BG_COLOR

        # ── 1. Summary title & three takeaways (~14s) ─────────────────────
        title = Text("Summary", color=ACCENT_GOLD, font_size=48, weight=BOLD
                     ).to_edge(UP, buff=0.4)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.7)
        self.wait(4.30)

        c1 = VGroup(
            Text("1", font_size=30, color=ACCENT_GOLD, weight=BOLD),
            Text("Average Rate of Change  =  slope of a secant line between two points",
                 font_size=21, color=WHITE_SOFT),
        ).arrange(RIGHT, buff=0.3)

        c2 = VGroup(
            Text("2", font_size=30, color=ACCENT_CYAN, weight=BOLD),
            Text("Instantaneous Rate of Change  =  slope of the tangent line at one point",
                 font_size=21, color=WHITE_SOFT),
        ).arrange(RIGHT, buff=0.3)

        c3 = VGroup(
            Text("3", font_size=30, color=ACCENT_GREEN, weight=BOLD),
            Text("The Derivative  f'(x)  gives the exact instantaneous rate at any x",
                 font_size=21, color=WHITE_SOFT),
        ).arrange(RIGHT, buff=0.3)

        concepts = VGroup(c1, c2, c3).arrange(DOWN, buff=0.45, aligned_edge=LEFT).shift(UP * 0.85)

        concept_waits = [6.38, 6.16, 1.50]
        for idx, concept in enumerate(concepts):
            self.play(FadeIn(concept, shift=RIGHT * 0.4), run_time=0.8)
            self.wait(concept_waits[idx])

        # ── 2. Formula recap (~7s) ────────────────────────────────────────
        h_line = Line(LEFT * 5.2, RIGHT * 5.2, color=ACCENT_GOLD, stroke_width=1.5).shift(DOWN * 0.65)
        self.play(Create(h_line), run_time=0.5)

        formulas_top = VGroup(
            Text("f(x) = x²",   font_size=32, color=ACCENT_GREEN),
            Text("f'(x) = 2x",  font_size=32, color=ACCENT_CYAN),
            Text("f'(2) = 4",   font_size=36, color=ACCENT_GOLD, weight=BOLD),
            Text("f'(3) = 6",   font_size=32, color=ACCENT_PINK),
        ).arrange(RIGHT, buff=0.75).shift(DOWN * 1.3)

        def_recap = Text(
            "f'(x) = lim (h → 0) [f(x + h) - f(x)] / h",
            font_size=24, color=WHITE_SOFT,
        ).shift(DOWN * 2.35)

        self.play(Write(formulas_top), run_time=1.5)
        box = SurroundingRectangle(formulas_top[2], color=ACCENT_GOLD, buff=0.18, corner_radius=0.12)
        self.play(Create(box), FadeIn(def_recap, shift=UP * 0.2), run_time=0.9)
        self.wait(10.16)

        self.play(FadeOut(title, concepts, h_line, formulas_top, box, def_recap), run_time=0.8)

        # ── 3. Credits (~8s) ──────────────────────────────────────────────
        cred_title = Text("DERIVATIVES & RATE OF CHANGE",
                          color=ACCENT_GOLD, font_size=30, weight=BOLD)
        cred_line1 = Line(LEFT * 4, RIGHT * 4, color=ACCENT_GOLD, stroke_width=1.5)

        name_row = VGroup(
            Text("Student Name:",  font_size=20, color=ACCENT_CYAN),
            Text("Aayush Singh", font_size=20, color=WHITE_SOFT),
        ).arrange(RIGHT, buff=0.3)

        id_row = VGroup(
            Text("Student ID:",  font_size=20, color=ACCENT_CYAN),
            Text("E25B070776", font_size=20, color=WHITE_SOFT),
        ).arrange(RIGHT, buff=0.3)

        topic_row = VGroup(
            Text("Topic:", font_size=20, color=ACCENT_CYAN),
            Text("Derivatives and Rate of Change – M3 Internal Assessment",
                 font_size=18, color=WHITE_SOFT),
        ).arrange(RIGHT, buff=0.3)

        cred_line2 = Line(LEFT * 4, RIGHT * 4, color=ACCENT_CYAN, stroke_width=1)

        ref_row = VGroup(
            Text("Reference:", font_size=18, color=ACCENT_CYAN),
            Text("Stewart, J. (2016). Calculus: Early Transcendentals, 8th Ed.",
                 font_size=16, color=WHITE_SOFT),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)

        ai_row = VGroup(
            Text("AI Disclosure:", font_size=18, color=ACCENT_PINK),
            Text("Animation assisted by Manim CE & AI code-generation tools",
                 font_size=16, color=WHITE_SOFT),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)

        credits_group = VGroup(
            cred_title, cred_line1,
            name_row, id_row, topic_row,
            cred_line2,
            ref_row, ai_row,
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT).scale(0.95).move_to(ORIGIN)

        self.play(FadeIn(credits_group, shift=UP * 0.3), run_time=1.2)
        self.wait(7.5)
        self.play(FadeOut(credits_group), run_time=0.8)

        # ── 4. Professional Thank-You Screen (~6s) ────────────────────────
        ty_title = Text("Thank You for Watching", font_size=50, color=ACCENT_GOLD, weight=BOLD)
        ty_sub   = Text("M3 Linear Algebra and Calculus  |  Internal Assessment",
                        font_size=22, color=ACCENT_CYAN)
        ty_grp   = VGroup(ty_title, ty_sub).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        self.play(FadeIn(ty_grp, shift=UP * 0.25), run_time=1.0)
        self.wait(3.8)
        self.play(FadeOut(ty_grp), run_time=0.9)
