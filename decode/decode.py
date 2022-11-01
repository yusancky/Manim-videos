from manim import *

my_font = "HarmonyOS Sans SC Light"


class Makeee0(Scene):
    def construct(self):
        title0 = MarkupText(
            "[CSP-J 2022] 解密", font=my_font, gradient=(BLUE, GREEN)
        ).scale(2.5)
        self.play(Write(title0))
        self.wait(1.5)
        self.play(FadeOut(title0))
        self.wait()


class Makeee1(Scene):
    def construct(self):
        title1 = MarkupText("题意简述", font=my_font, gradient=(BLUE, GREEN)).scale(2)
        a1 = Text("给定正整数", font=my_font)
        a2 = Tex("$n,e,d$").scale(1.2)
        a3 = Text("，求两个正整数", font=my_font)
        a4 = Tex("$p,q(p\leq q)$").scale(1.2)
        a5 = Text("，", font=my_font)
        a = VGroup(a1, a2, a3, a4, a5).arrange(RIGHT, buff=0.2)

        b1 = Text("使", font=my_font)
        b2 = Tex(
            "$\\begin{cases} n&=p\\cdot q\\\\ e\\cdot d &= (p-1)(q-1)+1 \\end{cases}$"
        ).scale(1.2)
        b3 = Text("。存在多组数据。", font=my_font)
        b = VGroup(b1, b2, b3).arrange(RIGHT, buff=0.2)
        task = VGroup(a, b).arrange(DOWN, buff=0.4)

        self.play(Write(title1))
        self.wait(1.5)
        self.play(FadeOut(title1))
        self.play(*[FadeIn(mob) for mob in task])
        self.wait(8)
        self.play(*[FadeOut(mob) for mob in task])
        self.wait()


class Makeee2(Scene):
    def construct(self):
        title2 = MarkupText("题目分析", font=my_font, gradient=(BLUE, GREEN)).scale(2)
        my_color_map = {
            "n": BLUE_D,
            "p\\cdot q": TEAL_C,
            "e\\cdot d": GREEN_A,
            "(p-1)(q-1)+1": PURPLE_B,
            "p+q": MAROON_B,
            "2": RED_B,
        }
        a1 = (
            MathTex("n", "=", "p\\cdot q", ",", "e\\cdot d", "=", "(p-1)(q-1)+1")
            .set_color_by_tex_to_color_map(my_color_map)
            .scale(1.5)
        )
        a2 = (
            MathTex("n", "-", "e\cdot d", "=", "p\cdot q", "-[", "(p-1)(q-1)+1", "]")
            .set_color_by_tex_to_color_map(my_color_map)
            .scale(1.5)
        )
        a3 = (
            MathTex("n", "-", "e\cdot d", "=", "p+q", "-", "2")
            .set_color_by_tex_to_color_map(my_color_map)
            .scale(1.5)
        )
        a4 = (
            MathTex("p+q", "=", "n", "-", "e\cdot d", "+", "2")
            .set_color_by_tex_to_color_map(my_color_map)
            .scale(1.5)
        )
        a5_1 = (
            MathTex("{{p}}", "{{+}}", "{{q}}", "{{=}}", "{{n-e\cdot d+2}}")
            .move_to(UP)
            .scale(1.5)
        )
        a5_2 = (
            MathTex("{{p}}", "{{\\cdot}}", "{{q}}", "{{=}}", "{{n}}")
            .move_to(DOWN)
            .scale(1.5)
        )
        a5 = VGroup(a5_1, a5_2)
        Vieta1 = Text("Vieta 定理（推论）：一元二次多", font=my_font).scale(1.2)
        Vieta2 = Text("项式", font=my_font).scale(1.2)
        Vieta3 = Tex("$x^2+bx+c$").scale(1.2)
        Vieta4 = Text("的两根", font=my_font).scale(1.2)
        Vieta5 = Tex("$x_1,x_2$").scale(1.2)
        Vieta6 = Text("总满", font=my_font).scale(1.2)
        Vieta7 = Text("足", font=my_font).scale(1.2)
        Vieta8 = MathTex(
            "\\begin{cases} x_1+x_2=-b \\\\ x_1\\cdot x_2=c \\end{cases}"
        ).scale(1.2)
        Vieta9 = Text("。", font=my_font).scale(1.2)
        Vieta = VGroup(
            Vieta1,
            VGroup(Vieta2, Vieta3, Vieta4, Vieta5, Vieta6).arrange(RIGHT, buff=0.2),
            VGroup(Vieta7, Vieta8, Vieta9).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.4)
        Vieta10 = MathTex(
            "{{x_1}}",
            "+",
            "{{x_2}}",
            "&=",
            "{{-b}}",
            "\\\\",
            "{{x_1}}",
            "\\cdot",
            "{{x_2}}",
            "&=",
            "{{c}}",
        ).scale(1.5)
        Vieta11_1 = MathTex(
            "{{p}}", "{{+}}", "{{q}}", "{{=}}", "{{-b}}", "{{=}}", "{{n-e\cdot d+2}}"
        ).scale(1.5)
        Vieta11_2 = MathTex(
            "{{p}}", "{{\\cdot}}", "{{q}}", "{{=}}", "{{c}}", "{{=}}", "{{n}}"
        ).scale(1.5)
        Vieta11 = VGroup(Vieta11_1, Vieta11_2).arrange(DOWN, 1)
        Vieta12_1 = MathTex("b=e\cdot d-n-2").scale(1.5)
        Vieta12_2 = MathTex("c=n").scale(1.5)
        Vieta12 = VGroup(Vieta12_1, Vieta12_2).arrange(DOWN, 1)
        eq1 = MathTex("x^2+bx+c=0").scale(1.5).move_to(3 * UP)
        eq2 = MathTex("x^2+(e\\cdot d-n-2)x+c=0").scale(1.5).move_to(3 * UP)
        eq3 = MathTex("x^2+(e\\cdot d-n-2)x+n=0").scale(1.5).move_to(3 * UP)
        eq4 = VGroup(
            MathTex("p,q").scale(0.8),
            Text("是方程").scale(0.8),
            MathTex("x^2+(e\\cdot d-n-2)x+n=0").scale(0.8),
            Text("的两正整数根").scale(0.8),
        ).arrange(RIGHT, buff=0.2)
        eq4_dl = Line(Dot(8 * LEFT + 2.5 * UP), Dot(8 * RIGHT + 2.5 * UP))
        ans1 = MathTex("\\Delta =b^2-4ac").scale(1.5)
        ans2 = MathTex("p,q=\\frac{-b\\pm \\sqrt \\Delta}{2}").scale(1.5)
        ans3 = Text("（求根公式）", font=my_font)
        ans = VGroup(ans1, ans2, ans3).arrange(DOWN, buff=0.4)

        self.play(Write(title2))
        self.wait(1.5)
        self.play(FadeOut(title2))
        self.play(GrowFromCenter(a1))
        self.wait()
        self.play(TransformMatchingTex(a1, a2))
        self.wait(2)
        self.play(TransformMatchingTex(a2, a3))
        self.wait(2)
        self.play(TransformMatchingTex(a3, a4))
        self.wait(2)
        self.play(a4.animate.shift(UP))
        self.play(FadeOut(a4), FadeIn(a5_1, a5_2))
        self.wait(2)
        self.play(
            Indicate(a5_1[0:3], scale_factor=1.5),
            Indicate(a5_2[0:3], scale_factor=1.5),
            run_time=1.5,
        )
        self.play(*[ScaleInPlace(obj, 0.8) for obj in a5], run_time=0.3)
        self.play(a5_1.animate.to_edge(UP), a5_2.animate.to_edge(DOWN), run_time=0.5)
        self.play(*[GrowFromEdge(obj, DOWN) for obj in Vieta])
        self.play(Wiggle(Vieta))
        self.wait(5)
        self.play(
            *[
                FadeOut(obj, scale=0.5)
                for obj in VGroup(Vieta[0], Vieta[1], Vieta7, Vieta9)
            ],
            run_time=0.5
        )
        self.play(TransformMatchingShapes(Vieta8, Vieta10))
        self.wait()
        self.play(TransformMatchingTex(Group(Vieta10, a5), Vieta11), run_time=3)
        self.wait(2)
        self.play(TransformMatchingShapes(Vieta11, Vieta12), run_time=1)
        self.wait()
        self.play(FadeIn(eq1))
        self.play(Indicate(Vieta12_1))
        self.play(FadeTransform(eq1, eq2, stretch=True))
        self.wait(0.5)
        self.play(Indicate(Vieta12_2))
        self.play(FadeTransform(eq2, eq3, stretch=True))
        self.wait()
        self.play(*[FadeOut(obj, shift=DOWN) for obj in Vieta12])
        self.play(eq3.animate.shift(3 * DOWN))
        self.wait(2)
        self.play(FadeTransform(eq3, eq4, stretch=True))
        self.wait(2)
        self.play(eq4.animate.to_edge(UP))
        self.play(Write(eq4_dl), run_time=0.4)
        self.wait(2)
        self.play(*[Write(obj) for obj in ans], run_time=0.5)
        self.wait(3)
        self.play(*[Unwrite(obj) for obj in VGroup(eq4, eq4_dl, ans1, ans2, ans3)], run_time=0.5)
        self.wait()


class Makeee3(Scene):
    def construct(self):
        title3 = MarkupText("参考代码", font=my_font, gradient=(BLUE, GREEN)).scale(2)
        rendered_code = Code(
            "decode.cpp",
            tab_width=2,
            background="window",
            language="cpp",
            font="Consolas",
            font_size=18,
        )

        self.play(Write(title3))
        self.wait(1.5)
        self.play(Unwrite(title3))
        self.play(Write(rendered_code))
        self.wait(10)
        self.play(FadeOut(rendered_code))
        self.wait()