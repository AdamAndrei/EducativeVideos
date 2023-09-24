from useful_constructs.intro_outro import *
from manim import *

"""
This class could use some refactoring
"""


class Introduction(Scene):
    config.frame_width = 35
    config.frame_height = 20

    def __init__(self):
        super(Introduction, self).__init__()
        self.lr = int(config["frame_width"] // 2)
        self.ud = int(config["frame_height"] // 2)

    def construct(self):
        self.show_intro()
        self.capitol1()
        self.show_questions()
        self.clear()
        self.wait(2)

    def show_intro(self):
        animate_intro_logo(self)
        title = Text("Numerele complexe", color=DARK_BROWN).scale(2).to_edge(UP).shift(2 * DOWN)
        self.play(Write(title), run_time=3)
        self.wait(0.1)
        self.play(Unwrite(title, run_time=1))
        self.wait(0.5)

    def capitol1(self):
        t = Text("Ca orice lecție care își propune să aducă răspunsuri, în primul rând avem nevoie de întrebări")
        self.play(Write(t, run_time=4))
        self.wait(1)
        self.clear()
        self.wait(0.5)

    def show_questions(self):
        title = MathTex(r"\cdot\quad\quad\quad\text{Înterbări}\quad\quad\quad\cdot").scale(2)
        title.add(Underline(title, buff=0.3))
        title.to_edge(UP, buff=0.25)
        self.play(Write(title))

        questions = self.get_questions()
        r = RoundedRectangle()
        for question in questions:
            self.play(FadeIn(question, run_time=1.5))
            if question == questions[0]:
                self.wait(0.5)
                r = self.mini_vector_question()
            elif question == questions[1]:
                self.wait(0.5)
                self.second_grade_eq(r)
            else:
                self.wait(0.5)
                self.derive_cos_formula(r)
            self.wait(0.5)

    """
    This is highly customized for this class usage only, should be kept inside this class not in a utils file
    so that is not confusing.
    """

    def get_questions(self) -> VGroup:
        question_texts = [
            "Un vector fiind dat cum găsim un vetor perpendicular lui?",
            "Putem rezolva cu adevărat o ecuație de gradul II?",
            r"\text{Cum rețin formula pentru } \cos(\alpha + \beta) \text{ ?}"
        ]
        qs = []
        for n, text in enumerate(question_texts):
            if n == 2:
                qs.append(
                    VGroup(
                        Text(f"Întrebarea #{n + 1}:").set_fill(GREY_A),
                        MathTex(text, stroke_width=1).scale(1.2),
                    ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
                )
            else:
                qs.append(
                    VGroup(
                        Text(f"Întrebarea #{n + 1}:").set_fill(GREY_A),
                        Text(text),
                    ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
                )
        questions = VGroup(*qs)
        questions.arrange(DOWN, buff=1.0, aligned_edge=LEFT)
        questions.set(height=4)
        questions.to_corner(UL).shift(3 * DOWN)
        return questions

    def mini_vector_question(self):
        h = self.ud - 1.5
        w = self.lr - 1.5

        r = RoundedRectangle(width=w, height=h, stroke_width=15, color=YELLOW) \
            .to_edge(DR, buff=1).shift(UP)
        t = Text("Poți observa un tipar?", font_size=50).move_to(r.get_top()).shift(UP)

        xl = int(r.get_x(LEFT)) + 0.5
        xr = int(r.get_x(RIGHT)) - 0.5
        yu = int(r.get_y(UP)) - 0.5
        yd = int(r.get_y(DOWN)) + 0.5

        aw = abs((xl + xr) / 2)
        ah = abs((yu + yd) / 2)

        axes = Axes(x_range=[-aw, aw], y_range=[-ah, ah], x_length=xr - xl,
                    y_length=yu - yd).move_to(r)

        points = []
        un_points = []
        for i in range(1, 9):
            for j in range(1, 5):
                p1 = Dot(point=axes.coords_to_point(i, j), radius=0.05, color=RED)
                p2 = Dot(point=axes.coords_to_point(-i, -j), radius=0.05, color=RED)
                p3 = Dot(point=axes.coords_to_point(i, -j), radius=0.05, color=RED)
                p4 = Dot(point=axes.coords_to_point(-i, j), radius=0.05, color=RED)
                points.append(Create(p1))
                points.append(Create(p2))
                points.append(Create(p3))
                points.append(Create(p4))

                un_points.append(Uncreate(p1))
                un_points.append(Uncreate(p2))
                un_points.append(Uncreate(p3))
                un_points.append(Uncreate(p4))

        self.play(*[FadeIn(r, run_time=1), FadeIn(axes, run_time=1), FadeIn(t, run_time=1)], *points)
        self.animate_vectors(3, 2, axes)
        self.animate_vectors(4, 1, axes)
        self.animate_vectors(4, 4, axes)
        self.play(*[Uncreate(t), Uncreate(axes)], *un_points)
        self.wait(0.5)
        return r

    def animate_vectors(self, i, j, axes: Axes):
        v = Arrow(start=axes.coords_to_point(0, 0), end=axes.coords_to_point(i, j), buff=0, color=RED)
        v_c = v.copy().set_opacity(opacity=0.4)
        ort_v = Arrow(start=axes.coords_to_point(0, 0), end=axes.coords_to_point(-j, i), buff=0, color=BLUE)
        ort_v_c = ort_v.copy().set_opacity(opacity=0.4)
        ort_v2 = Arrow(start=axes.coords_to_point(0, 0), end=axes.coords_to_point(-i, -j), buff=0, color=GREEN)
        ort_v2_c = ort_v2.copy().set_opacity(opacity=0.4)
        ort_v3 = Arrow(start=axes.coords_to_point(0, 0), end=axes.coords_to_point(j, -i), buff=0, color=PURPLE)
        ort_v3_c = ort_v3.copy().set_opacity(opacity=0.4)

        label = get_label(v, axes)
        label_c = label.copy().set_opacity(0.4)
        ort_label = get_label(ort_v, axes)
        ort_label_c = ort_label.copy().set_opacity(opacity=0.4)
        ort_label2 = get_label(ort_v2, axes)
        ort_label2_c = ort_label2.copy().set_opacity(opacity=0.4)
        ort_label3 = get_label(ort_v3, axes)
        ort_label3_c = ort_label3.copy().set_opacity(opacity=0.4)

        self.play(*[FadeIn(v, run_time=2), FadeIn(label, run_time=2)])
        self.add(*[v_c, label_c])
        self.play(*[ReplacementTransform(v, ort_v), ReplacementTransform(label, ort_label)], run_time=1.5)
        self.wait(0.3)
        self.add(*[ort_v_c, ort_label_c])
        self.play(*[ReplacementTransform(ort_v, ort_v2), ReplacementTransform(ort_label, ort_label2)], run_time=1.5)
        self.wait(0.3)
        self.add(*[ort_v2_c, ort_label2_c])
        self.play(*[ReplacementTransform(ort_v2, ort_v3), ReplacementTransform(ort_label2, ort_label3)], run_time=1.5)
        self.wait(0.3)

        self.remove(*[v, v_c, ort_v_c, ort_v_c, ort_v2, ort_v2_c, ort_v3, ort_v3_c,
                      label, label_c, ort_label, ort_label_c, ort_label2, ort_label2_c, ort_label3, ort_label3_c])

    def second_grade_eq(self, r: RoundedRectangle):
        t = Text("Dar cum rezolvăm o ecuație de gradul 2?", font_size=50).move_to(r.get_top()).shift(UP)
        scale = 2
        ec21 = MathTex(r"ax^2 + bx + c = 0").move_to(r.get_center()).scale(scale)
        ec22 = MathTex(r"ax^2 + bx + c = 0\: |\: \cdot 4a").move_to(r.get_center()).scale(scale)
        ec23 = MathTex(r"4a^2x^2 + 4abx + 4ac = 0").move_to(r.get_center()).scale(scale)
        ec24 = MathTex(r"(2ax)^2 + 2\cdot 2ax \cdot b + b^2 - b^2 + 4ac = 0").move_to(r.get_center()).scale(1.5)
        ec25 = MathTex(r"(2ax)^2 + 2\cdot 2ax \cdot b + b^2 = b^2 - 4ac").move_to(r.get_center()).scale(scale)
        ec26 = MathTex(r"(2ax + b)^2 = b^2 - 4ac").move_to(r.get_center()).scale(scale)
        ec27 = MathTex(r"2ax + b = \pm\sqrt{b^2 - 4ac}").move_to(r.get_center()).scale(scale)
        ec28 = MathTex(r"\Rightarrow x_{1, 2} =\dfrac{-b \pm\sqrt{b^2 - 4ac}}{2a}", color=YELLOW) \
            .move_to(r.get_center()).scale(scale)

        delta = MathTex(r"\Delta = b^2 - 4ac", color=TEAL).scale(scale).move_to(r.get_center()).shift(3 * UP)
        ec29 = MathTex(r"x_{1, 2} =\dfrac{-b \pm\sqrt{\Delta}}{2a}", color=YELLOW) \
            .move_to(r.get_center()).scale(scale)

        # c = Circle(radius=0.9, stroke_width=6).move_to(ec29).shift(2.9 * RIGHT + 0.8 * UP)
        c = RoundedRectangle(width=2, height=1.6, stroke_width=6, color=TEAL, fill_color=PURE_RED, fill_opacity=0.4) \
            .move_to(ec29).shift(2.9 * RIGHT + 0.7 * UP)

        t1 = Text("Dar avem o problemă...", font_size=50).move_to(r.get_top()).shift(UP)
        t2 = MathTex(r"\text{... dacă } \Delta < 0 \text{ ?}").move_to(r.get_bottom()).shift(UP).scale(2)
        self.play(Write(t, run_time=1))
        self.play(FadeIn(ec21, run_time=2))
        self.play(ReplacementTransform(ec21, ec22), run_time=2)
        self.play(ReplacementTransform(ec22, ec23), run_time=2)
        self.play(ReplacementTransform(ec23, ec24), run_time=2)
        self.play(ReplacementTransform(ec24, ec25), run_time=2)
        self.play(ReplacementTransform(ec25, ec26), run_time=2)
        self.play(ReplacementTransform(ec26, ec27), run_time=2)
        self.play(ReplacementTransform(ec27, ec28), run_time=2)
        self.play(ReplacementTransform(ec28, ec29), FadeIn(delta), run_time=2)
        self.play(ReplacementTransform(t, t1), FadeIn(c), run_time=2)
        self.play(FadeIn(t2, run_time=2))
        self.wait(1)
        self.play(*[Uncreate(t1), Uncreate(t2), Uncreate(delta), Uncreate(c), Uncreate(ec29)])

    def derive_cos_formula(self, r: RoundedRectangle):
        t = MathTex(r"\text{Cât face } \cos(\alpha + \beta) \text{ mai exact ?}", font_size=50).move_to(
            r.get_top()).shift(UP)
        alpha = PI / 9
        beta = 2 * PI / 9
        a_color = YELLOW
        b_color = TEAL

        xl = int(r.get_x(LEFT)) + 0.5
        xr = int(r.get_x(RIGHT)) - 0.5
        yu = int(r.get_y(UP)) - 0.5
        yd = int(r.get_y(DOWN)) + 0.5

        ah = abs((yu + yd) / 2)

        axes = Axes(
            x_range=[(2 * (ah + 0.4) / (yu - yd + 0.4)) * (xl - xr), (2 * (ah + 0.4) / (yu - yd + 0.4)) * (xr - xl)],
            y_range=[-ah - 0.4, ah + 0.4], x_length=xr - xl,
            y_length=yu - yd + 0.4).move_to(r)

        c = Circle(radius=4 * axes.get_y_unit_size()).move_to(r.get_center())

        la = Line(start=c.get_center(), end=c.get_right(), color=a_color)
        lb = Line(start=c.get_center(), end=c.get_right(), color=b_color)

        rad = Line(start=c.get_center(), end=c.get_left(), color=DARK_BROWN, stroke_width=8)
        brace = Brace(rad)
        one = Text("1").next_to(brace, DOWN)

        self.play(Write(t, run_time=1))
        self.play(FadeIn(c, run_time=2), FadeIn(axes))
        self.play(GrowFromCenter(brace), Create(rad), Write(one, run_time=1))

        self.play(la.animate.rotate(angle=alpha, about_point=c.get_center()))
        laa = Angle(line1=axes.get_x_axis(), line2=la, quadrant=(1, 1), radius=1.5, color=a_color)
        laa_lable = MathTex(r"\alpha", color=a_color).next_to(laa, RIGHT)
        self.play(*[FadeIn(laa), FadeIn(laa_lable)])

        self.play(lb.animate.rotate(angle=beta, about_point=c.get_center()))
        lab = Angle(line1=axes.get_x_axis(), line2=lb, quadrant=(1, 1), radius=0.5, color=b_color)
        lab_lable = MathTex(r"\beta", color=b_color).next_to(lab, RIGHT).shift(0.2 * UP)
        self.play(*[FadeIn(lab), FadeIn(lab_lable)])

        self.play(laa.animate.rotate(angle=beta, about_point=c.get_center()),
                  laa_lable.animate.rotate(angle=beta, about_point=c.get_center()),
                  la.animate.rotate(angle=beta, about_point=c.get_center()))

        new_a_angle = Angle(line1=lb, line2=la, quadrant=(1, 1), radius=0.7, color=a_color)
        self.play(*[ReplacementTransform(laa, new_a_angle),
                    laa_lable.animate.next_to(new_a_angle, RIGHT).shift(0.4 * UP + 0.1 * LEFT)])

        p = combinePoints(lb.get_start(), lb.get_end(), np.cos(alpha))
        pl = Line(start=la.get_end(), end=p, color=PURPLE)
        ra = RightAngle(line1=lb, line2=pl, length=0.1, quadrant=(1, -1), stroke_width=1)
        self.play(*[Create(pl), Create(ra)])

        heigth1 = axes.get_vertical_line(point=la.get_end())
        heigth2 = axes.get_vertical_line(point=pl.get_end())

        self.play(*[Create(heigth1), Create(heigth2)])

        p1 = combinePoints(heigth1.get_end(), heigth1.get_start(), np.sin(alpha) * np.cos(beta) / np.sin(alpha + beta))
        li = Line(start=p, end=p1, color=GREEN)
        self.play(Create(li, run_time=1))

        pi_beta = Angle(line1=heigth1, line2=lb, radius=0.3, color=TEAL, quadrant=(-1, -1), other_angle=True)
        arrow_to_pi_beta = Arrow(start=axes.coords_to_point(12, 2.5), end=pi_beta.get_center(), stroke_width=2)
        pi_beta_label = MathTex(r"\frac{\pi}{2} - \beta", color=TEAL).scale(0.7).move_to(
            arrow_to_pi_beta.get_start()).shift(0.7 * RIGHT)

        pi_beta1 = Angle(line1=heigth1, line2=lb, radius=0.3, color=TEAL, quadrant=(1, 1), other_angle=True)
        arrow_to_pi_beta1 = Arrow(start=axes.coords_to_point(12, 2.5), end=pi_beta1.get_center(), stroke_width=2)

        beta_ang = Angle(line1=heigth1, line2=pl, radius=0.3, color=TEAL, quadrant=(-1, 1))
        beta_label = MathTex(r"\beta", color=TEAL).scale(0.5).next_to(beta_ang, 0.5 * DOWN).shift(0.1 * RIGHT)

        self.play(*[FadeIn(pi_beta), FadeIn(arrow_to_pi_beta), FadeIn(pi_beta_label)])
        self.play(*[ReplacementTransform(arrow_to_pi_beta, arrow_to_pi_beta1), FadeIn(pi_beta1)])
        self.play(*[FadeOut(arrow_to_pi_beta1), FadeOut(pi_beta), FadeOut(pi_beta1), FadeOut(pi_beta_label),
                    FadeIn(beta_ang), FadeIn(beta_label)])

        m_label = Text("M").scale(0.5).next_to(heigth1.get_start(), DOWN)
        n_label = Text("N").scale(0.5).next_to(heigth2.get_start(), DOWN)
        o_label = Text("O").scale(0.5).next_to(axes.get_center(), DOWN + 0.5 * RIGHT)
        p_label = Text("P").scale(0.5).next_to(heigth2.get_end(), RIGHT).shift(0.2 * DOWN + 0.2 * LEFT)
        q_label = Text("Q").scale(0.5).next_to(li.get_end(), LEFT).shift(0.1 * RIGHT)
        r_label = Text("R").scale(0.5).next_to(la.get_end(), UP)

        self.play(
            *[Create(m_label), Create(n_label), Create(o_label), Create(p_label), Create(q_label), Create(r_label)])

        mini_r = RoundedRectangle(width=r.width, height=r.height, stroke_width=15, color=ORANGE) \
            .next_to(r, LEFT, buff=1)

        la_c = la.copy()
        pl_c = pl.copy()
        op = Line(start=axes.get_center(), end=p, color=b_color)
        o_c = o_label.copy()
        p_c = p_label.copy()
        r_c = r_label.copy()
        a_ang_c = new_a_angle.copy()
        alpha_c = laa_lable.copy()

        self.play(FadeIn(mini_r, run_time=2))
        results = self.animate_first_triangle(la_c, pl_c, op, o_c, p_c, r_c, a_ang_c, alpha_c, mini_r, beta, r)

        pr = pl.copy()
        qp = li.copy()
        qr = Line(start=la.get_end(), end=p1, color=PURE_RED)
        q_label_c = q_label.copy()
        p_label_c = p_label.copy()
        r_label_c = r_label.copy()
        beta_ang_c = beta_ang.copy()
        beta_label_c = beta_label.copy()

        results1 = self.animate_second_triangle(pr, qp, qr, q_label_c, p_label_c, r_label_c, beta_ang_c,
                                                beta_label_c, mini_r, r, beta, axes, results)

        op_c = Line(start=axes.get_center(), end=p, color=b_color)
        pn = Line(start=heigth2.get_end(), end=heigth2.get_start(), color=BLUE)
        no = Line(start=heigth2.get_start(), end=axes.get_center(), color=RED)
        p_lab = p_label.copy()
        o_lab = o_label.copy()
        n_lab = n_label.copy()
        beta_a = lab.copy()
        beta_lab = lab_lable.copy()

        results2 = self.animate_third_triangle(op_c, pn, no, p_lab, o_lab, n_lab, beta_a, beta_lab, mini_r, r, beta,
                                               axes,
                                               results1)

        p2 = combinePoints(heigth1.get_end(), heigth1.get_start(), np.sin(alpha) / np.cos(beta) / np.sin(alpha + beta))

        med = Line(start=axes.get_center(), end=p2, color=TEAL)
        om = Line(start=axes.get_center(), end=heigth1.get_start(), color=BLUE)
        mr = Line(start=heigth1.get_start(), end=heigth1.get_end(), color=PURPLE)
        ro = Line(start=la.get_end(), end=la.get_start(), color=YELLOW)
        o_lab_c = o_label.copy()
        m_lab = m_label.copy()
        r_lab = r_label.copy()
        al_ang = new_a_angle.copy()
        al_lab = laa_lable.copy()
        be_ang = lab.copy()
        be_lab = lab_lable.copy()

        self.animate_fourth_triangle(med, om, mr, ro, o_lab_c, m_lab, r_lab, al_ang, al_lab, be_ang, be_lab,
                                     mini_r, axes)

        self.play(*[FadeOut(t), FadeOut(axes), FadeOut(c), FadeOut(lb), FadeOut(rad), FadeOut(brace), FadeOut(one),
                    FadeOut(la), FadeOut(lb), FadeOut(new_a_angle), FadeOut(laa_lable), FadeOut(lab),
                    FadeOut(lab_lable),
                    FadeOut(pl), FadeOut(ra), FadeOut(heigth1), FadeOut(heigth2), FadeOut(li), FadeOut(beta_ang),
                    FadeOut(beta_label), FadeOut(m_label), FadeOut(n_label), FadeOut(o_label), FadeOut(p_label),
                    FadeOut(q_label), FadeOut(r_label), FadeOut(results2)], run_time=5)
        self.wait(1)

    def animate_first_triangle(self, la_c, pl_c, op, o_c, p_c, r_c, a_ang_c, alpha_c, mini_r, beta, r):
        opr = VGroup(*[la_c, pl_c, op, o_c, p_c, r_c, a_ang_c, alpha_c])
        self.play(opr.animate.scale(3 / 2), run_time=1)
        self.play(opr.animate.scale(2 / 3), run_time=1)
        self.play(opr.animate.move_to(mini_r.get_center()).scale(3 / 2).shift(1.5 * UP + 3 * LEFT), run_time=2)
        self.play(opr.animate.rotate(angle=- beta, about_point=opr.get_center()), run_time=1)
        self.play(o_c.animate.rotate(angle=beta, about_point=o_c.get_center()).next_to(la_c.get_start(), DOWN),
                  p_c.animate.rotate(angle=beta, about_point=p_c.get_center()).next_to(op.get_end(), DOWN),
                  r_c.animate.rotate(angle=beta, about_point=r_c.get_center()).next_to(la_c.get_end(), UP),
                  run_time=1)

        brace1 = BraceBetweenPoints(point_2=la_c.get_start(), point_1=la_c.get_end())
        one1 = Text("1").next_to(brace1, UP)

        self.play(GrowFromCenter(brace1), Write(one1, run_time=1))

        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{amsmath,amsfonts,amsthm,mathrsfs}")
        si = MathTex(r"\begin{cases}\sin\alpha = \dfrac{PR}{OR}\\ \\ \cos\alpha = \dfrac{OP}{OR}\end{cases}",
                     tex_template=myTemplate).next_to(opr, RIGHT, buff=2)
        si1 = MathTex(
            r"\Rightarrow\begin{cases}\sin\alpha = \dfrac{PR}{1}\\ \\ \cos\alpha = \dfrac{OP}{1}\end{cases}\Rightarrow"
            r"\begin{cases}PR = \sin\alpha \\ \\ OP = \cos\alpha\end{cases}").next_to(opr, DOWN, buff=1).shift(
            3 * RIGHT)

        si2 = MathTex(r"\begin{cases}PR = \sin\alpha \\ \\ OP = \cos\alpha\end{cases}").move_to(r.get_corner(DL)).shift(
            2 * UP + 2 * RIGHT)

        self.play(Write(si, run_time=2))
        self.play(Write(si1, run_time=4))
        self.wait(1)

        self.play(*[FadeOut(opr), FadeOut(brace1), FadeOut(one1), FadeOut(si), FadeOut(si1), FadeIn(si2)])

        return si2

    def animate_second_triangle(self, pr, qp, qr, q_label_c, p_label_c, r_label_c, beta_ang_c, beta_label_c,
                                mini_r, r, beta, axes, results):
        qpr = VGroup(*[pr, qp, qr, q_label_c, p_label_c, r_label_c, beta_ang_c, beta_label_c])
        self.play(qpr.animate.scale(3 / 2), run_time=1)
        self.play(qpr.animate.scale(2 / 3), run_time=1)
        self.play(qpr.animate.move_to(mini_r.get_center()).scale(2).shift(1.5 * UP + 5 * LEFT), run_time=2)
        self.play(q_label_c.animate.next_to(qr.get_end(), DOWN))
        brace = BraceBetweenPoints(point_2=pr.get_start(), point_1=pr.get_end())
        label = MathTex(r"\sin\alpha", color=YELLOW)
        label.rotate(angle=beta - PI / 2, about_point=label.get_center()).next_to(brace, 0.1 * RIGHT).shift(
            0.4 * UP + 0.4 * LEFT)

        self.play(*[GrowFromCenter(brace), Write(label, run_time=1)])

        text = MathTex(r"\sin\beta = \dfrac{PQ}{PR}").next_to(qpr, RIGHT, buff=1)

        self.play(Write(text, run_time=1))
        rt1 = Rectangle(width=1.1, height=0.6, color=PURE_RED).move_to(text).shift(0.4 * DOWN + 0.9 * RIGHT)
        rt2 = Rectangle(width=2.7, height=0.7, color=PURE_RED).move_to(text).move_to(
            axes.coords_to_point(-13.5, -1.9)).shift(0.1 * RIGHT)

        self.play(*[Create(rt1), Create(rt2)], run_time=1.5)
        self.play(*[FadeOut(rt1), FadeOut(rt2)], run_time=1.5)

        text1 = MathTex(r"=\dfrac{PQ}{\sin\alpha}").next_to(text, RIGHT)
        text2 = MathTex(r"\Rightarrow PQ = \sin\alpha\sin\beta").scale(3 / 2).next_to(qpr, DOWN, buff=1).shift(
            3 * RIGHT)

        self.play(Write(text1, run_time=1))
        self.play(Write(text2, run_time=1))
        self.wait(1)

        text3 = MathTex(
            r"\begin{cases} PR = \sin\alpha \\ OP = \cos\alpha \\ PQ = \sin\alpha\sin\beta\end{cases}").move_to(
            r.get_corner(DL)).shift(2 * UP + 3 * RIGHT)

        self.play(*[FadeOut(qpr), FadeOut(brace), FadeOut(label), FadeOut(text), FadeOut(text1), FadeOut(text2),
                    ReplacementTransform(results, text3)])

        return text3

    def animate_third_triangle(self, op_c, pn, no, p_lab, o_lab, n_lab, beta_a, beta_lab, mini_r, r, beta, axes,
                               results):
        mop = VGroup(*[op_c, pn, no, p_lab, o_lab, n_lab, beta_a, beta_lab])
        self.play(mop.animate.scale(3 / 2), run_time=1)
        self.play(mop.animate.scale(2 / 3), run_time=1)
        self.play(mop.animate.move_to(mini_r.get_center()).scale(3 / 2).shift(1.5 * UP + 5 * LEFT), run_time=2)
        self.play(p_lab.animate.next_to(pn.get_start(), UR), o_lab.animate.next_to(op_c.get_start(), DL))
        brace = BraceBetweenPoints(point_2=op_c.get_start(), point_1=op_c.get_end())
        label = MathTex(r"\cos\alpha", color=YELLOW)
        label.rotate(angle=beta, about_point=label.get_center()).move_to(brace.get_center()).shift(0.3 * UL)

        self.play(*[GrowFromCenter(brace), Write(label, run_time=1)])

        text = MathTex(r"\cos\beta = \dfrac{ON}{OP}").next_to(mop, RIGHT, buff=1)

        self.play(Write(text, run_time=1))
        rt1 = Rectangle(width=1.1, height=0.6, color=PURE_RED).move_to(text).shift(0.4 * DOWN + 0.9 * RIGHT)
        rt2 = Rectangle(width=2.7, height=0.7, color=PURE_RED).move_to(text).move_to(
            axes.coords_to_point(-13, -2.8)).shift(0.3 * RIGHT)

        self.play(*[Create(rt1), Create(rt2)], run_time=1.5)
        self.play(*[FadeOut(rt1), FadeOut(rt2)], run_time=1.5)

        text1 = MathTex(r"=\dfrac{ON}{\cos\alpha}").next_to(text, RIGHT)
        text2 = MathTex(r"\Rightarrow ON = \cos\alpha\cos\beta").scale(3 / 2).next_to(mop, DOWN, buff=1).shift(
            3 * RIGHT)

        self.play(Write(text1, run_time=1))
        self.play(Write(text2, run_time=1))
        self.wait(1)

        text3 = MathTex(
            r"\begin{cases} PR = \sin\alpha \\ OP = \cos\alpha \\ PQ = \sin\alpha\sin\beta \\ ON = "
            r"\cos\alpha\cos\beta\end{cases}").move_to(
            r.get_corner(DL)).shift(2 * UP + 3 * RIGHT)

        self.play(*[FadeOut(mop), FadeOut(brace), FadeOut(label), FadeOut(text), FadeOut(text1), FadeOut(text2),
                    ReplacementTransform(results, text3)])

        return text3

    def animate_fourth_triangle(self, med, om, mr, ro, o_lab_c, m_lab, r_lab, al_ang, al_lab, be_ang, be_lab,
                                mini_r, axes):
        omr = VGroup(*[om, mr, ro, o_lab_c, m_lab, r_lab, al_ang, al_lab, be_ang, be_lab, med])
        self.play(omr.animate.scale(3 / 2), run_time=1)
        self.play(omr.animate.scale(2 / 3), run_time=1)
        self.play(omr.animate.move_to(mini_r.get_center()).scale(3 / 2).shift(UP + 5 * LEFT), run_time=2)
        self.play(o_lab_c.animate.next_to(om.get_start(), DL))
        brace = BraceBetweenPoints(point_1=ro.get_start(), point_2=ro.get_end())
        label = Text("1", color=YELLOW)
        label.move_to(brace.get_center()).shift(0.4 * UL)

        self.play(*[GrowFromCenter(brace), Write(label, run_time=1)])

        sum_angle = Angle(line1=om, line2=ro, radius=1, color=TEAL, quadrant=(1, -1))
        sum_label = MathTex(r"\alpha + \beta")
        sum_label.rotate(angle=- PI / 4, about_point=sum_label.get_center()).move_to(sum_angle.get_center()).shift(
            0.4 * UR + 0.2 * RIGHT)

        v1 = VGroup(*[al_ang, al_lab, be_ang, be_lab, med])
        v2 = VGroup(*[sum_angle, sum_label])
        self.play(ReplacementTransform(v1, v2))

        t1 = MathTex(r"\cos(\alpha + \beta) = \dfrac{OM}{OP} = \dfrac{OM}{1} = OM").next_to(ro.get_start(),
                                                                                            RIGHT).shift(
            RIGHT + 3 * DOWN)
        t2 = MathTex(r"= ON - MN").next_to(t1, DOWN).shift(0.3 * RIGHT)
        t3 = MathTex(r"= ON - PQ").next_to(t1, DOWN).shift(0.2 * RIGHT)

        self.play(Write(t1, run_time=1.5))
        self.play(Write(t2, run_time=1))
        self.play(ReplacementTransform(t2, t3, run_time=2))

        t5 = MathTex(r"\Rightarrow\cos(\alpha+\beta) =").next_to(mini_r.get_corner(DL)).shift(1.5 * UP + 3 * RIGHT)

        self.play(Write(t5, run_time=1))

        rt1 = Rectangle(width=2.7, height=0.6, color=PURE_RED).move_to(t3).shift(0.4 * RIGHT)
        rt2 = Rectangle(width=4, height=1.5, color=PURE_RED).move_to(
            axes.coords_to_point(-13, -3.5)).shift(1 * RIGHT)

        self.play(*[Create(rt1), Create(rt2)], run_time=1.5)
        self.play(*[FadeOut(rt1), FadeOut(rt2)], run_time=1.5)

        t6 = MathTex(r"\cos\alpha\cos\beta - \sin\alpha\sin\beta").next_to(t5, RIGHT)

        self.play(Create(t6, run_time=3))

        rou = RoundedRectangle(width=10, height=1.4, fill_color=RED, fill_opacity=0.4).move_to(t6.get_center()).shift(
            1.5 * LEFT)

        self.play(DrawBorderThenFill(rou, run_time=2))

        self.play(*[FadeOut(omr), FadeOut(v2), FadeOut(t1), FadeOut(t3), FadeOut(t5), FadeOut(t6), FadeOut(rou),
                    FadeOut(brace), FadeOut(label), FadeOut(mini_r)])


"""
When running from command-line "manimce -pqh .\\ComplexNumbers\\lessons\\Introduction.py Introduction" the imports do
not work properly. To address this problem try running this file as a usual python project (using the IDE).

Note: for this to work you have to use the syntax below, you may add other parameters to config the rendering. 
"""

with tempconfig({"quality": "high_quality", "preview": True}):
    scene = Introduction()
    scene.render()
