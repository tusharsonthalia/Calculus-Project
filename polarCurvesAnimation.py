from manimlib.imports import *


def polarPlane():
    grid = NumberPlane(x_line_frequency=PI/4, y_line_frequency=PI/4,)
    grid.generate_target()
    grid.target.faded_lines[4:9].fade(1)
    grid.target.faded_lines[12:].fade(1)
    grid.target.background_lines[4:9].fade(1)
    grid.target.background_lines[12:].fade(1)
    grid.target.prepare_for_nonlinear_transform()
    grid.target.apply_function(lambda p: np.array(
        [p[0]*np.cos(p[1]), p[0]*np.sin(p[1]), 0]))

    return grid

class PolarCurve(ParametricFunction):
    CONFIG = {
        "theta_min": 0,
        "theta_max": TAU,
        "color": YELLOW
    }

    def __init__(self, function, **kwargs):
        digest_config(self, kwargs)
        self.polar_function = lambda t: np.array(
            [function(t) * np.cos(t), function(t) * np.sin(t), 0])
        ParametricFunction.__init__(
            self,
            self.polar_function,
            t_min=self.theta_min,
            t_max=self.theta_max,
            **kwargs
        )
        self.function = function

    def get_function(self):
        return self.function

    def get_point_from_function(self, x):
        return self.polar_function(x)

class Introduction(Scene):
    def construct(self):
        intro_text = TextMobject("Polar Curves")
        intro_text.scale(3)
        intro_text.set_color_by_gradient(BLUE, PURPLE)

        explanation1 = TextMobject("""
            Polar Coordinates replaces the conventional Cartesian\n
            coordinate system by using $r$ and $\\theta$ as its coordinate\n
            base instead of $x$ and $y$.
        """, alignment="")
        explanation1.to_corner(UL)

        explanation2 = TextMobject("""
            For a line at $(x, y)$ from the origin\n
            the length of the line is considered to be $r$\n
            and the angle it makes with the $x-axis$\n
            is considered as the $\\theta$.
        """, alignment="")
        explanation2.to_corner(UL)

        vert_line = Line(np.array([-4, -3, 0]), np.array([-4, 0, 0]))
        vert_line.set_color(BLUE)
        horz_line = Line(np.array([-4, -3, 0]), np.array([-1, -3, 0]))
        horz_line.set_color(BLUE)
        diag_line = Line(np.array([-4, -3, 0]), np.array([-2, -1, 0]))
        dot = Dot([-4, -3, 0])
        graph_group = VGroup(vert_line, horz_line, diag_line, dot)

        x = DashedLine([-4, -2, 0], [-3, -2, 0])
        x.set_color(RED)
        y = DashedLine([-3, -3, 0], [-3, -2, 0])
        y.set_color(RED)

        x_label = TextMobject("$x$")
        x_label.next_to(x, UP)
        y_label = TextMobject("$y$")
        y_label.next_to(y, RIGHT)
        r_label = TextMobject("$r$")
        r_label.move_to(np.array([-2.5, -1.2, 0]))
        angle_arc = ArcBetweenPoints(
            np.array([-3.5, -3, 0]), np.array([-3.7, -2.7, 0]))
        theta_label = TextMobject("$\\theta$")
        theta_label.next_to(angle_arc, np.array([0.3, 0, 0]))

        index = VGroup(x, y)
        labels = VGroup(x_label, y_label, r_label, angle_arc, theta_label)

        explanation3 = TextMobject("""
            The concept of polar curves becomes\n
            easier to understand by converting a normal\n
            cartesian coordinate system into polar\n
            coordinate system.
        """, alignment="")
        explanation3.to_corner(UL)

        grid = NumberPlane()
        polar = polarPlane().target

        explanation4 = TextMobject("""
            The cartesian coordinates can be converted to polar\n
            coordiates by the following conversion formulae:\n\n\n\n
            $x = r \\cos{\\theta}$\n
            $y = r \\sin{\\theta}$\n
            $r^{2} = x^{2} + y^{2}$\n
            $\\tan{\\theta} = \\frac{y}{x}$
        """, alignment="")
        explanation4.to_corner(UL)
        grid_copy = NumberPlane()

        self.play(Write(intro_text))
        self.wait()
        self.play(ReplacementTransform(intro_text, explanation1))
        self.wait()
        self.play(ReplacementTransform(explanation1, explanation2),
                  ShowCreation(graph_group))
        self.wait()
        self.play(ShowCreation(index))
        self.wait()
        self.play(Write(labels))
        self.wait()
        self.play(FadeOut(VGroup(graph_group, index, explanation2, labels)))
        self.wait()
        self.play(ShowCreation(grid, run_time=3))
        self.play(Write(explanation3))
        self.wait()
        self.play(ReplacementTransform(grid, polar, run_time=3))
        self.wait()
        self.play(ReplacementTransform(explanation3, explanation4),
                  ReplacementTransform(polar, grid_copy, run_time=3))
        self.wait()

    def polar_to_c(self, point):
        return np.array([
            point[0] * np.cos(point[1]),
            point[0] * np.sin(point[1]),
            0
        ])

class Question1(GraphScene):
    def construct(self):
        grid = NumberPlane(x_line_frequency=PI/4, y_line_frequency=PI/4,)
        grid.generate_target()
        grid.target.faded_lines[4:9].fade(1)
        grid.target.faded_lines[12:].fade(1)
        grid.target.background_lines[4:9].fade(1)
        grid.target.background_lines[12:].fade(1)
        grid.target.prepare_for_nonlinear_transform()
        grid.target.apply_function(lambda p: np.array(
            [p[0]*np.cos(p[1]), p[0]*np.sin(p[1]), 0]))

        question = TextMobject("""
            Investigate the family of curves defined by the polar\n
            equation $r = \\sin{(n\\theta)}$, where n is a positive\n
            integer. How is the number of loops related to n?
        """, alignment="")
        question.to_edge(UP)

        explanation1 = TextMobject("""
            Let us plot the graph of $\\sin{(n\\theta)}$ on cartesian\n
            coordinate system where n ranges from 1 to 5.
        """)
        explanation1.to_edge(UP)
        annotations = [self.get_annotation(
            i, explanation1) for i in range(1, 6)]
        sin_curves = [self.get_sin_curve(i) for i in range(1, 6)]

        explanation2 = TextMobject("""
            Now, the same graphs for $\\sin{\\theta}$\n
            will be plotted on the polar coordinate system.
        """)
        explanation2.to_edge(UP)

        polar_sin_curves = self.polar_sin_curves(sin_curves)
        new_annotations = [self.get_annotation(
            i, explanation1) for i in range(1, 6)]

        explanation3 = TextMobject("""
            It is noticed that for every odd value of $n$\n
            there are $n$ number of loops in the sin curve,\n
            however, for every even number of $n$ there seems\n
            to be $2n$ number of loops in the sin curve.
        """)
        explanation3.to_edge(UP)

        explanation4 = TextMobject("""
            The reason for this is that when $n$ is odd, every\n
            point on the graph is traversed twice resulting in\n
            $n$ number of loops, and when $n$ is even,\n
            each point is only traversed once which results in\n
            $2n$ number of loops.
        """)
        explanation5 = TextMobject("""
            This can be proved visually in the following way:
        """)
        left_sin_odd = self.get_sin_curve(3, -PI, 0)
        right_sin_odd = self.get_sin_curve(3, 0)
        left_sin_even = self.get_sin_curve(2, -PI, 0)
        right_sin_even = self.get_sin_curve(2, 0)
        left_sin_odd_polar, right_sin_odd_polar,\
            left_sin_even_polar, right_sin_even_polar = self.polar_sin_curves([left_sin_odd,
                                                                               right_sin_odd,
                                                                               left_sin_even,
                                                                               right_sin_even])

        sin_odd_label = TextMobject("$\\sin{(3\\theta)}$")
        sin_even_label = TextMobject("$\\sin{(2\\theta)}$")

        even_sin_group = VGroup(left_sin_even, right_sin_even)
        even_sin_group.arrange(RIGHT, buff=0)
        sin_even_label.next_to(even_sin_group, DOWN)
        odd_sin_group = VGroup(left_sin_odd, right_sin_odd)
        odd_sin_group.arrange(RIGHT, buff=0)
        sin_odd_label.next_to(odd_sin_group, DOWN)

        left_sin_odd_polar.move_to(left_sin_odd)
        right_sin_odd_polar.move_to(right_sin_odd)
        left_sin_even_polar.move_to(left_sin_even)
        right_sin_even_polar.move_to(right_sin_even)

        left_sin_even_polar.generate_target()
        left_sin_even_polar.target.shift(RIGHT * 1.2)
        right_sin_even_polar.generate_target()
        right_sin_even_polar.target.shift(LEFT * 1.2)
        left_sin_odd_polar.generate_target()
        left_sin_odd_polar.target.move_to(ORIGIN)
        right_sin_odd_polar.generate_target()
        right_sin_odd_polar.target.move_to(ORIGIN)

        explanation5_footnote = TextMobject("""
            The mathematical reason for why the number of loops is $2n$\n
            when $n$ is even and $n$ when $n$ is odd is:\n
            $r(\\theta + \\pi) = \\sin{[n(\\theta + \\pi)]}$\n 
            $= \\sin{n\\theta}\\cos{n\\pi} + \\cos{n\\theta}\\sin{n\\pi}$\n
            $= \\begin{cases}\\sin{(n\\theta)}\\\\ -\\sin{(n\\theta)} \\end{cases}$
        """)

        explanation6 = TextMobject("""
            However, the graph for $r = \\abs{\\sin{n\\theta}}$\n
            has $2n$ loops for all values of $n$ as every point on\n
            the graph is traversed just once since\n
            $r(\\theta + \\pi) = r(\\theta)$.
        """)

        odd_mod_polar, even_mod_polar = self.get_mod_polar_sin_curves([3, 4])
        odd_mod_polar_label = TextMobject("$r = \\abs{\\sin{3\\theta}}$")
        even_mod_polar_label = TextMobject("$r = \\abs{\\sin{4\\theta}}$")
        odd_mod_group = VGroup(odd_mod_polar, odd_mod_polar_label)
        odd_mod_group.arrange(DOWN)
        even_mod_group = VGroup(even_mod_polar, even_mod_polar_label)
        even_mod_group.arrange(DOWN)
        mod_group = VGroup(odd_mod_group, even_mod_group)
        mod_group.arrange(RIGHT, buff=2)
        mod_group.shift(DOWN)

        self.play(Write(question))
        self.wait()
        self.play(ReplacementTransform(question, explanation1))
        self.wait()
        self.play(ShowCreation(grid, run_time=2))
        self.wait()
        self.play(ShowCreation(sin_curves[0],
                               run_time=2), Write(annotations[0]))
        self.wait()
        self.play(
            ReplacementTransform(sin_curves[0], sin_curves[1]),
            ReplacementTransform(annotations[0], annotations[1])
        )
        self.wait()
        self.play(
            ReplacementTransform(sin_curves[1], sin_curves[2]),
            ReplacementTransform(annotations[1], annotations[2])
        )
        self.wait()
        self.play(
            ReplacementTransform(sin_curves[2], sin_curves[3]),
            ReplacementTransform(annotations[2], annotations[3])
        )
        self.wait()
        self.play(
            ReplacementTransform(sin_curves[3], sin_curves[4]),
            ReplacementTransform(annotations[3], annotations[4])
        )
        self.wait()
        self.play(ReplacementTransform(explanation1, explanation2))
        self.wait()
        self.play(MoveToTarget(grid), ReplacementTransform(
            sin_curves[4], polar_sin_curves[4]), run_time=2)
        self.wait()
        self.play(
            ReplacementTransform(polar_sin_curves[4], polar_sin_curves[3]),
            ReplacementTransform(annotations[4], new_annotations[3])
        )
        self.wait()
        self.play(
            ReplacementTransform(polar_sin_curves[3], polar_sin_curves[2]),
            ReplacementTransform(new_annotations[3], new_annotations[2])
        )
        self.wait()
        self.play(
            ReplacementTransform(polar_sin_curves[2], polar_sin_curves[1]),
            ReplacementTransform(new_annotations[2], new_annotations[1])
        )
        self.wait()
        self.play(
            ReplacementTransform(polar_sin_curves[1], polar_sin_curves[0]),
            ReplacementTransform(new_annotations[1], new_annotations[0])
        )
        self.wait()
        self.play(ReplacementTransform(explanation2, explanation3),
                  FadeOut(new_annotations[0]))
        self.wait()
        self.play(ReplacementTransform(explanation3, explanation4),
                  FadeOut(VGroup(grid, polar_sin_curves[0])))
        self.wait()
        self.play(ReplacementTransform(explanation4, explanation5))
        self.wait()
        self.play(ShowCreation(even_sin_group), Write(
            sin_even_label), explanation5.to_edge, UP)
        self.wait()
        self.play(ReplacementTransform(left_sin_even, left_sin_even_polar),
                  ReplacementTransform(right_sin_even, right_sin_even_polar))
        self.wait()
        self.play(MoveToTarget(left_sin_even_polar),
                  MoveToTarget(right_sin_even_polar))
        self.wait()
        self.play(ReplacementTransform(VGroup(left_sin_even_polar, right_sin_even_polar),
                                       odd_sin_group), ReplacementTransform(sin_even_label, sin_odd_label))
        self.wait()
        self.play(ReplacementTransform(left_sin_odd, left_sin_odd_polar),
                  ReplacementTransform(right_sin_odd, right_sin_odd_polar))
        self.wait()
        self.play(MoveToTarget(left_sin_odd_polar),
                  MoveToTarget(right_sin_odd_polar))
        self.wait()
        self.play(FadeOut(VGroup(left_sin_odd_polar,
                                 right_sin_odd_polar, sin_odd_label, explanation5)))
        self.play(Write(explanation5_footnote))
        self.wait()
        self.play(ReplacementTransform(explanation5_footnote, explanation6))
        self.wait()
        self.play(explanation6.to_edge, UP,
                  ShowCreation(mod_group, run_time=4))
        self.wait()

    def get_mod_polar_sin_curves(self, n, x_min=-PI, x_max=PI):
        result = []
        for i in n:
            graph = FunctionGraph(lambda x: np.abs(
                np.sin(i * x)), x_min=x_min, x_max=x_max)
            graph.rotate(PI, axis=UR, about_point=ORIGIN)
            graph.apply_function(lambda p: np.array(
                [p[0] * np.cos(p[1]), p[0] * np.sin(p[1]), 0]))
            result.append(graph)
        return result

    def get_sin_curve(self, n=1, x_min=-PI, x_max=PI):
        return FunctionGraph(lambda x: np.sin(n * x), x_min=x_min, x_max=x_max)

    def get_annotation(self, n, object):
        if n == 1:
            return TextMobject("For $\\sin{(\\theta)}$:").next_to(object, DOWN)
        return TextMobject("For $\\sin{("+str(n)+"\\theta)}$:").next_to(object, DOWN)

    def polar_sin_curves(self, sin_curves):
        result = [sin_curve.copy() for sin_curve in sin_curves]
        for sin_curve in result:
            sin_curve.rotate(PI, axis=UR, about_point=ORIGIN)
            sin_curve.apply_function(lambda p: np.array(
                [p[0] * np.cos(p[1]), p[0] * np.sin(p[1]), 0]))
        return result


class Question2(GraphScene):
    def construct(self):
        question = TextMobject("""
            A family of curves is given by the equations $r=1+c\\sin{(n\\theta)}$,\n
            where $c$ is a real number and $n$ is a positive integer. How does\n
            the graph change as $n$ increases? How does it change as\n
            $c$ changes? Illustrate by graphing enough members of the\n
            family to support your conclusions.
        """)
        polar_plane = polarPlane().target

        explanation1 = TextMobject("""
            Let us plot some graphs to reach a conclusion.
        """)
        explanation2 = TextMobject("""
            First let us keep the value of c fixed\n
            at 3 while we vary n from 1 to 5.
        """)
        explanation2.to_edge(UP)

        polar_curves = [self.get_graph(n, 3) for n in range(1, 6)]
        annotations = [self.get_annotation(
            n, 3) for n in range(1, 6)]

        explanation3 = TextMobject("""
            It is observed that as and when the value of n increases,\n
            the number of loops of the polar curve also increases.\n
            More importantly, when $n$ is even the smaller loops\n
            are outside the bigger loops, while they are inside\n
            the bigger loops when the value of $n$ is odd.
        """)

        graph_n_3, graph_n_4 = self.get_graph(
            3, 3).scale(.3), self.get_graph(4, 3).scale(.3)
        graph_n_3_label = TextMobject("$r = 1 + 3\\sin{(3\\theta)}$")
        graph_n_4_label = TextMobject("$r = 1 + 3\\sin{(4\\theta)}$")
        graph_group = VGroup(VGroup(graph_n_3, graph_n_3_label).arrange(
            DOWN), VGroup(graph_n_4, graph_n_4_label).arrange(DOWN))
        graph_group.arrange(RIGHT, buff=3)
        graph_group.to_edge(DOWN)

        explanation4 = TextMobject("""
            Now let us fix the value of $n$ as 4 while the value of\n
            $c$ varies from -10 to 10.
        """)

        list_of_c_values = [-10, -7.4, -2.1, -0.1, 1.9, 5.7, 8.9, 10]
        annotations2 = [self.get_annotation(4, c) for c in list_of_c_values]
        polar_curves2 = [self.get_graph(4, c) for c in list_of_c_values]

        explanation5 = TextMobject("""
            It is observed from the previous demonstration that as $c$\n
            increased from $-10$, the curve seemed to get smaller,\n
            and as it reached close to $0$, the inner loops completely\n
            disappeared. Furthermore, as the value of $c$ increased to\n
            $10$ the curve started growing and the inner loops start to\n
            get bigger.
        """)

        explanation6 = TextMobject("""
            It is observed from the previous demonstration that as $c$ increased from\n
            -10, the curve seemed to get smaller, and as it reached close to 0, the\n
            inner loops completely disappeared. Furthermore, as the value of c\n
            increased to 10 the curve started growing and the inner loops start to\n
            get bigger.
        """)
        explanation6.to_edge(UP)
        explanation6.scale(.7)

        graph_group_1 = self.get_graph(3, -10)
        graph_group_1.scale(.15)
        graph_group_2 = self.get_graph(3, 10)
        graph_group_2.scale(.15)
        graph_group_3 = self.get_graph(4, -10)
        graph_group_3.scale(.15)
        graph_group_4 = self.get_graph(4, 10)
        graph_group_4.scale(.15)

        graph__label_1 = TextMobject("$n = 3, c = -10$")
        graph__label_1.scale(.6)
        graph__label_2 = TextMobject("$n = 3, c = 10$")
        graph__label_2.scale(.6)
        graph__label_3 = TextMobject("$n = 4, c = -10$")
        graph__label_3.scale(.6)
        graph__label_4 = TextMobject("$n = 4, c = 10$")
        graph__label_4.scale(.6)

        graph_group_1 = VGroup(graph_group_1, graph__label_1)
        graph_group_1.arrange(DOWN)
        graph_group_2 = VGroup(graph_group_2, graph__label_2)
        graph_group_2.arrange(DOWN)
        graph_group_3 = VGroup(graph_group_3, graph__label_3)
        graph_group_3.arrange(DOWN)
        graph_group_4 = VGroup(graph_group_4, graph__label_4)
        graph_group_4.arrange(DOWN)

        c_graph_group = VGroup(graph_group_1, graph_group_2,
                               graph_group_3, graph_group_4)
        c_graph_group.arrange(RIGHT)
        c_graph_group.to_edge(DOWN)

        self.play(Write(question))
        self.wait()
        self.play(ReplacementTransform(question, explanation1))
        self.wait()
        self.play(ReplacementTransform(explanation1, explanation2))
        self.wait()
        self.play(ShowCreation(polar_plane, run_time=3))
        self.wait()
        self.play(ShowCreation(polar_curves[0]), ReplacementTransform(
            explanation2, annotations[0]))
        self.wait()
        self.play(
            ReplacementTransform(annotations[0], annotations[1]),
            ReplacementTransform(polar_curves[0], polar_curves[1])
        )
        self.wait()
        self.play(
            ReplacementTransform(annotations[1], annotations[2]),
            ReplacementTransform(polar_curves[1], polar_curves[2])
        )
        self.wait()
        self.play(
            ReplacementTransform(annotations[2], annotations[3]),
            ReplacementTransform(polar_curves[2], polar_curves[3])
        )
        self.wait()
        self.play(
            ReplacementTransform(annotations[3], annotations[4]),
            ReplacementTransform(polar_curves[3], polar_curves[4])
        )
        self.wait()
        self.play(FadeOut(
            VGroup(polar_curves[4], annotations[4], polar_plane)), Write(explanation3))
        self.wait()
        self.play(explanation3.to_edge, UP, ShowCreation(graph_group))
        self.wait()
        self.play(FadeOut(VGroup(explanation3, graph_group)))
        self.wait()
        self.play(Write(explanation4))
        self.wait()
        self.play(ShowCreation(polar_plane), explanation4.to_edge, UP)
        self.wait()
        self.play(ReplacementTransform(explanation4,
                                       annotations2[0]), ShowCreation(polar_curves2[0]))
        self.wait()
        self.play(
            ReplacementTransform(annotations2[0], annotations2[1]),
            ReplacementTransform(polar_curves2[0], polar_curves2[1])
        )
        self.wait()
        self.play(
            ReplacementTransform(annotations2[1], annotations2[2]),
            ReplacementTransform(polar_curves2[1], polar_curves2[2])
        )
        self.wait()
        self.play(
            ReplacementTransform(annotations2[2], annotations2[3]),
            ReplacementTransform(polar_curves2[2], polar_curves2[3])
        )
        self.wait()
        self.play(
            ReplacementTransform(annotations2[3], annotations2[4]),
            ReplacementTransform(polar_curves2[3], polar_curves2[4])
        )
        self.wait()
        self.play(
            ReplacementTransform(annotations2[4], annotations2[5]),
            ReplacementTransform(polar_curves2[4], polar_curves2[5])
        )
        self.wait()
        self.play(
            ReplacementTransform(annotations2[5], annotations2[6]),
            ReplacementTransform(polar_curves2[5], polar_curves2[6])
        )
        self.wait()
        self.play(
            ReplacementTransform(annotations2[6], annotations2[7]),
            ReplacementTransform(polar_curves2[6], polar_curves2[7])
        )
        self.wait()
        self.play(FadeOut(VGroup(polar_curves2[7], polar_plane)), ReplacementTransform(
            annotations2[7], explanation5))
        self.wait()
        self.play(ReplacementTransform(explanation5, explanation6),
                  ShowCreation(c_graph_group))
        self.wait()
        self.play(FadeOut(VGroup(explanation6, c_graph_group)))
        self.wait()

    def get_graph(self, n, c):
        def function(theta): return 1 + c * np.sin(n * theta)
        graph = PolarCurve(function)
        return graph

    def get_annotation(self, n, c):
        text = TextMobject("For $n = "+str(n)+", c = "+str(c)+"$:")
        text.to_corner(UL)
        return text

class Question3(GraphScene):
    def construct(self):
        question = TextMobject("""
            A family of curves has polar equations\n
            $r = \\frac{1 - a\\cos{\\theta}}{1 + a\\cos{\\theta}}$\n
            Investigate how the graph changes as the number a changes.\n
            In particular, you should identity the transitional values\n
            of a for which the basic shape of the curve changes.
        """)

        explanation1 = TextMobject("""
            Let us plot the graph for $r = \\frac{1 - a\\cos{\\theta}}{1 + a\\cos{\\theta}}$\n
            We will explore the shapes taken by the function for various\n
            values of a.
        """)
        explanation1.generate_target()
        explanation1.target.to_edge(UP)

        polar_plane = polarPlane()

        a_values = [-20, -10, 4, -2.5, -1.1, -.4,
                    0, .4, 1.6, 2.8, 4.3, 9.8, 19.5]

        polar_curves = [self.get_graph(a) for a in a_values]
        annotations = [self.get_annotation(a) for a in a_values]

        explanation2 = TextMobject("""
            With the increase in the value of $a$, the graph moves to the left\n
            and its right side becomes flattened. As $a$ increases through\n
            about 0.4, the right side of the graph begins to grow a dimple.\n
        """)

        e2_graph_1 = self.get_graph(0.2)
        e2_graph_label_1 = TextMobject(
            "$r = \\frac{1 - 0.2\\cos{\\theta}}{1 + 0.2\\cos{\\theta}}$")
        e2_graph_group_1 = VGroup(e2_graph_1, e2_graph_label_1)
        e2_graph_group_1.arrange(DOWN)
        e2_graph_group_1.to_edge(DOWN)
        e2_graph_2 = self.get_graph(0.4)
        e2_graph_label_2 = TextMobject(
            "$r = \\frac{1 - 0.4\\cos{\\theta}}{1 + 0.4\\cos{\\theta}}$")
        e2_graph_group_2 = VGroup(e2_graph_2, e2_graph_label_2)
        e2_graph_group_2.arrange(DOWN)
        e2_graph_group_2.to_edge(DOWN)
        e2_graph_3 = self.get_graph(0.6)
        e2_graph_label_3 = TextMobject(
            "$r = \\frac{1 - 0.6\\cos{\\theta}}{1 + 0.6\\cos{\\theta}}$")
        e2_graph_group_3 = VGroup(e2_graph_3, e2_graph_label_3)
        e2_graph_group_3.arrange(DOWN)
        e2_graph_group_3.to_edge(DOWN)

        explanation3 = TextMobject("""
            As $a$ tends to 1, this dimple becomes more pronounced,\n
            and the curve begins to stretch out horizontally,\n
            until at $a = 1$ the denominator vanishes at $\\theta = \\pi$.\n
        """)

        e3_graph_1 = self.get_graph(0.8)
        e3_graph_1.scale(.2)
        e3_graph_label_1 = TextMobject(
            "$r = \\frac{1 - 0.8\\cos{\\theta}}{1 + 0.8\\cos{\\theta}}$")
        e3_graph_group_1 = VGroup(e3_graph_1, e3_graph_label_1)
        e3_graph_group_1.arrange(DOWN)
        e3_graph_group_1.to_edge(DOWN)
        e3_graph_2 = self.get_graph(0.9)
        e3_graph_2.scale(.2)
        e3_graph_label_2 = TextMobject(
            "$r = \\frac{1 - 0.9\\cos{\\theta}}{1 + 0.9\\cos{\\theta}}$")
        e3_graph_group_2 = VGroup(e3_graph_2, e3_graph_label_2)
        e3_graph_group_2.arrange(DOWN)
        e3_graph_group_2.to_edge(DOWN)
        e3_graph_3 = self.get_graph(1)
        e3_graph_3.scale(.2)
        e3_graph_label_3 = TextMobject(
            "$r = \\frac{1 - \\cos{\\theta}}{1 + \\cos{\\theta}}$")
        e3_graph_group_3 = VGroup(e3_graph_3, e3_graph_label_3)
        e3_graph_group_3.arrange(DOWN)
        e3_graph_group_3.to_edge(DOWN)

        explanation4 = TextMobject("""
            As $a$ increases from 1, the curve splits into two parts.\n
            The left part of the loop, which grows larger as $a$ increases,\n
            and the right part grows broader vertically.
        """)

        e4_graph_1 = self.get_graph(2)
        e4_graph_1.scale(0.02)
        e4_graph_label_1 = TextMobject(
            "$r = \\frac{1 - 2\\cos{\\theta}}{1 + 2\\cos{\\theta}}$")
        e4_graph_group_1 = VGroup(e4_graph_1, e4_graph_label_1)
        e4_graph_group_1.arrange(DOWN)
        e4_graph_group_1.to_edge(DOWN)
        e4_graph_2 = self.get_graph(7)
        e4_graph_2.scale(0.02)
        e4_graph_label_2 = TextMobject(
            "$r = \\frac{1 - 7\\cos{\\theta}}{1 + 7\\cos{\\theta}}$")
        e4_graph_group_2 = VGroup(e4_graph_2, e4_graph_label_2)
        e4_graph_group_2.arrange(DOWN)
        e4_graph_group_2.to_edge(DOWN)
        e4_graph_3 = self.get_graph(15)
        e4_graph_3.scale(0.02)
        e4_graph_label_3 = TextMobject(
            "$r = \\frac{1 - 15\\cos{\\theta}}{1 + 15\\cos{\\theta}}$")
        e4_graph_group_3 = VGroup(e4_graph_3, e4_graph_label_3)
        e4_graph_group_3.arrange(DOWN)
        e4_graph_group_3.to_edge(DOWN)

        self.play(Write(question))
        self.wait()
        self.play(ReplacementTransform(question, explanation1))
        self.wait()
        self.play(MoveToTarget(explanation1),
                  ShowCreation(polar_plane, run_time=2.5))
        self.wait()
        self.play(ShowCreation(polar_curves[0]), ReplacementTransform(
            explanation1, annotations[0]))
        self.wait()
        self.add_and_remove_graphs(polar_curves, 0, 1, annotations, 0, 1)
        self.add_and_remove_graphs(polar_curves, 1, 2, annotations, 1, 2)
        self.add_and_remove_graphs(polar_curves, 2, 3, annotations, 2, 3)
        self.add_and_remove_graphs(polar_curves, 3, 4, annotations, 3, 4)
        self.add_and_remove_graphs(polar_curves, 4, 5, annotations, 4, 5)
        self.add_and_remove_graphs(polar_curves, 5, 6, annotations, 5, 6)
        self.add_and_remove_graphs(polar_curves, 6, 7, annotations, 6, 7)
        self.add_and_remove_graphs(polar_curves, 7, 8, annotations, 7, 8)
        self.add_and_remove_graphs(polar_curves, 8, 9, annotations, 8, 9)
        self.add_and_remove_graphs(polar_curves, 9, 10, annotations, 9, 10)
        self.add_and_remove_graphs(polar_curves, 10, 11, annotations, 10, 11)
        self.add_and_remove_graphs(polar_curves, 11, 12, annotations, 11, 12)
        self.play(
            FadeOut(VGroup(polar_plane, polar_curves[12], annotations[12])))
        self.wait()
        self.play(Write(explanation2))
        self.wait()
        self.play(ShowCreation(e2_graph_group_1), explanation2.to_edge, UP)
        self.wait()
        self.play(
            ReplacementTransform(e2_graph_group_1, e2_graph_group_2)
        )
        self.wait()
        self.play(
            ReplacementTransform(e2_graph_group_2, e2_graph_group_3)
        )
        self.wait()
        self.play(ReplacementTransform(explanation2, explanation3),
                  FadeOut(e2_graph_group_3))
        self.wait()
        self.play(ShowCreation(e3_graph_group_1), explanation3.to_edge, UP)
        self.wait()
        self.play(
            ReplacementTransform(e3_graph_group_1, e3_graph_group_2)
        )
        self.wait()
        self.play(
            ReplacementTransform(e3_graph_group_2, e3_graph_group_3)
        )
        self.wait()
        self.play(ReplacementTransform(explanation3, explanation4),
                  FadeOut(e3_graph_group_3))
        self.wait()
        self.play(ShowCreation(e4_graph_group_1), explanation4.to_edge, UP)
        self.wait()
        self.play(
            ReplacementTransform(e4_graph_group_1, e4_graph_group_2)
        )
        self.wait()
        self.play(
            ReplacementTransform(e4_graph_group_2, e4_graph_group_3)
        )
        self.wait()
        self.play(FadeOut(explanation4), FadeOut(e4_graph_group_3))
        self.wait()

    def add_and_remove_graphs(self, graph, ga, gb, label, la, lb):
        self.play(
            ReplacementTransform(graph[ga], graph[gb]),
            ReplacementTransform(label[la], label[lb])
        )
        self.wait()

    def get_graph(self, a):
        def function(theta): return (
            1 - a*np.cos(theta)) / (1 + a*np.cos(theta))
        graph = PolarCurve(function)
        return graph

    def get_annotation(self, a):
        text = TextMobject("For $a = "+str(a)+"$:")
        text.to_corner(UL)
        return text

class Question4(GraphScene):
    def construct(self):
        question = TextMobject("""
            The astronomer Giovanni Cassini (1625-1712) studied\n
            the family of curves with polar equations:\n
            $r^{4} - 2 c^{2}r^{2}\\cos{(2\\theta)} + c^{4} - a^{4} = 0$\n
            where $a$ and $c$ are positive real numbers. These curves\n
            are called the ovals of Cassini even though they are oval\n
            shaped only for certain values of $a$ and $c$. Investigate the\n
            variety of shapes that these curves may have. In particular,\n
            how are $a$ and $c$ related to each other when the curve\n
            splits into parts?   
        """)

        solution1 = TextMobject(
            """In order to plot the curve, we must solve the equation first.""")
        solution1.set_color(BLUE)
        solution1.generate_target()
        # solution1.target.match_color()
        solution1.target.to_edge(UP)

        solution2 = TexMobject(
            "r^{4} ",                           # 0
            "-",                                # 1
            " c^{2}r^{2}\\cos{(2\\theta)} ",    # 2
            "+",                                # 3
            " c^{4} ",                          # 4
            "-",                                # 5
            " a^{4} ",                          # 6
            "=",                                # 7
            '0'                                 # 8
        )
        solution2.next_to(solution1.target, DOWN)

        solution3 = TextMobject("Using the quadratic formula, we obtain;")
        solution3.set_color(BLUE)
        solution3.next_to(solution2, DOWN)

        solution4 = TexMobject(
            "r^{2} = \\frac{2c^{2}\\cos{(2\\theta)} \\pm \\sqrt{4c^{4}\\cos^{2}{(2\\theta)} - 4(c^{4} - a^{4})}}{2}"
        )
        solution4.next_to(solution3, DOWN)

        solution5 = TexMobject(
            "r^{2} ",                           # 0
            "=",                                # 1
            " c^{2}\\cos{(2\\theta)} ",         # 2
            "\pm",                              # 3
            " \\sqrt{",                         # 4
            "a^{4} ",                           # 5
            "-",                                # 6
            " c^{4}",                           # 7
            '\\sin^{2}{(2\\theta)}'             # 8
        )
        solution5.next_to(solution4, DOWN)

        solution6 = TextMobject(
            "On taking the square root on both the sides we obtain;")
        solution6.set_color(BLUE)
        solution6.next_to(solution5, DOWN)

        solution7 = TexMobject("""
            r = \\pm\\sqrt{c^{2}\\cos{(2\\theta)} \\pm \\sqrt{a^{4} - c^{4}\\sin^{2}{(2\\theta)}}}
        """)
        solution7.next_to(solution6, DOWN)
        solution7.generate_target()
        solution7.target.to_edge(UP)
        solution7.target.scale(1.25)

        solution8 = TextMobject(
            "Thus, 4 curves must be plotted for every graph of this equation")
        solution8.set_color(BLUE)

        explanation1 = TextMobject(
            "Let us plot the graphs for multiple values of $a$ and $c$")
        explanation1.generate_target()
        explanation1.target.to_edge(UP)

        polar_plane = polarPlane().target

        graph_vars = [(1, 1), (.99, 1), (1.01, 1),
                      (4.04, 4), (1.3, 1), (1.5, 1), (2, 1)]
        annotations = [self.get_annotation(a, c, explanation1.target) for a, c in graph_vars]
        graphs = [self.get_graph(a, c) for a, c in graph_vars]

        explanation2 = TextMobject("""
            We have observed that when $a$ and $c$ equalled 1, the shape\n
            of the curve resembled somewhat of the infinity ($\\infty$) sign.\n
        """)
        explanation2.shift(UP*1.5)

        explanation3 = TextMobject("""
            As the value of $a$ went on increasing, the curve began losing\n
            its dimples and started looking more like an oval.\n
        """) 
        explanation3.next_to(explanation2, DOWN)

        explanation4 = TextMobject("""
            The shape of the curve started resembling that of an oval\n
            as $a$ reached the value of 1.5 and for all the higher values\n
            the curve started becoming rounder and larger.
        """) 
        explanation4.next_to(explanation3, DOWN)

        self.play(Write(question))
        self.wait()
        self.play(ReplacementTransform(question, solution1))
        self.wait()
        self.play(MoveToTarget(solution1), Write(solution2))
        self.wait()
        self.play(Write(solution3))
        self.wait()
        self.play(
            ReplacementTransform(solution2.copy(), solution4),
        )
        self.wait()
        self.play(
            ReplacementTransform(solution4.copy(), solution5),
        )
        self.wait()
        self.play(Write(solution6))
        self.wait()
        self.play(
            ReplacementTransform(solution5.copy(), solution7),
        )
        self.wait()
        self.play(
            MoveToTarget(solution7),
            FadeOut(VGroup(
                solution1,
                solution2,
                solution3,
                solution4,
                solution5,
                solution6
            ))
        )
        self.wait()
        self.play(Write(solution8))
        self.wait()
        self.play(FadeOut(solution7),
                  ReplacementTransform(solution8, explanation1))
        self.play(MoveToTarget(explanation1), ShowCreation(polar_plane, run_time=2.5))
        self.wait()
        self.play(Write(annotations[0]), ShowCreation(graphs[0]))
        self.wait()
        self.add_and_remove_graphs(annotations, 1, graphs, 1)
        self.add_and_remove_graphs(annotations, 2, graphs, 2)
        self.add_and_remove_graphs(annotations, 3, graphs, 3)
        self.add_and_remove_graphs(annotations, 4, graphs, 4)
        self.add_and_remove_graphs(annotations, 5, graphs, 5)
        self.add_and_remove_graphs(annotations, 6, graphs, 6)
        self.play(
            FadeOut(VGroup(polar_plane, annotations[6], graphs[6], explanation1)),
            Write(explanation2)
        )
        self.wait()
        self.play(Write(explanation3))
        self.wait()
        self.play(Write(explanation4))
        self.wait()

    def add_and_remove_graphs(self, annotations, index, graphs, index2):
        self.play(
            ReplacementTransform(annotations[index - 1], annotations[index]),
            ReplacementTransform(graphs[index2 - 1], graphs[index2])
        )
        self.wait()

    def get_annotation(self, a, c, obj):
        text = TextMobject(f"For $a =$ {a} and $c =$ {c}:")
        text.next_to(obj, DOWN)
        return text

    def get_graph(self, a, c):
        func1 = lambda theta: np.sqrt(c**2 * np.cos(2 * theta)) + np.sqrt(a**4 - c**4 * np.square(np.sin(2*theta)))
        graph1 = PolarCurve(func1)
        graph1.move_to(ORIGIN)
        group = VGroup(graph1)
        return group

class Conclusion(Scene):
    def construct(self):
        writeup1 = TextMobject("""
            In this project, we have explored the beautiful shapes\n
            undertaken by Polar Curves along with the properties\n
            of the said graphs.
        """)
        writeup1.set_color_by_gradient(BLUE, PURPLE)

        writeup2 = TextMobject("""This project has been done by:\n
            - Pradeep Sandilya.\n
            - Tushar Sonthalia.\n
            - Vedant Kabra.
        """) 

        writeup3 = TextMobject("""
            All the animations used in this presentation has been generated\n
            with python. The code for this project is available at:\n
        """)
        url = TextMobject('https://github.com/tusharsonthalia/Calculus-Project')
        url.next_to(writeup3, DOWN)
        url.set_color(BLUE)

        self.play(Write(writeup1))
        self.wait()
        self.play(ReplacementTransform(writeup1, writeup2))
        self.wait()
        self.play(LaggedStart(*[ReplacementTransform(writeup2, writeup3), Write(url, run_time=2.5)]))
        self.wait()

class ExampleScene(Scene):
    def construct(self):
        def polar2c(p):
            return np.array([
                p[0]*np.cos(p[1]),
                p[0]*np.sin(p[1]),
                0
            ])

        grid = NumberPlane(
            x_line_frequency=PI/4,
            y_line_frequency=PI/4,
            x_min=-PI,
            x_max=PI,
            y_min=-PI,
            y_max=PI
        )

        # self.play()
        func = FunctionGraph(lambda x: np.sin(5*x), x_min=-PI, x_max=PI)
        grid.add(func)
        self.add(grid)
        grid.faded_lines[4:9].fade(1)
        grid.faded_lines[12:].fade(1)
        grid.background_lines[4:9].fade(1)
        grid.background_lines[12:].fade(1)
        self.play(Rotating(func, radians=PI, axis=UR,
                           about_point=ORIGIN, run_time=2, rate_func=smooth))
        grid.generate_target()
        grid.target.prepare_for_nonlinear_transform()
        grid.target.apply_function(lambda p: polar2c(p))

        self.play(
            MoveToTarget(grid, run_time=4)
        )
        self.wait(3)
