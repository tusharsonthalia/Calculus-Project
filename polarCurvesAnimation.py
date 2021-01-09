from manimlib.imports import *


def polarPlane():
    grid = NumberPlane()
#     grid.prepare_for_nonlinear_transform()
#     grid.background_lines[1:4].fade(1)
#     grid.background_lines[5:8].fade(1)
#     grid.faded_lines[1:4].fade(1)
#     grid.faded_lines[5:10].fade(1)
#
#     grid.apply_function(lambda p: np.array(
#         [p[0]*np.cos(p[1]), p[0]*np.sin(p[1]), 0]))
    grid.faded_lines[4:9].fade(1)
    grid.faded_lines[12:].fade(1)
    grid.background_lines[4:9].fade(1)
    grid.background_lines[12:].fade(1)
    grid.prepare_for_nonlinear_transform()
    grid.apply_function(lambda p: np.array(
        [p[0]*np.cos(p[1]), p[0]*np.sin(p[1]), 0]))

    return grid


class PolarCurve(ParametricFunction):
    CONFIG = {
        "theta_min": 0,
        "theta_max": TAU,
        "color": TEAL
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
        polar = polarPlane()

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

        explanation6 = TextMobject("""
            However, the graph for $r = \\abs{\\sin{n\\theta}}$\n
            has $2n$ loops for all values of $n$ as every point on\n
            the graph is traversed just once.
        """)

        odd_mod_polar, even_mod_polar = self.get_mod_polar_sin_curves([3,4])
        odd_mod_polar_label = TextMobject("$r = \\abs{\\sin{3\\theta}}$")
        even_mod_polar_label = TextMobject("$r = \\abs{\\sin{4\\theta}}$")
        odd_mod_group = VGroup(odd_mod_polar, odd_mod_polar_label)
        odd_mod_group.arrange(DOWN)
        even_mod_group = VGroup(even_mod_polar, even_mod_polar_label)
        even_mod_group.arrange(DOWN)
        mod_group = VGroup(odd_mod_group, even_mod_group)
        mod_group.arrange(RIGHT, buff=2)

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
        self.play(ShowCreation(even_sin_group), Write(sin_even_label), explanation5.to_edge, UP)
        self.wait()
        self.play(ReplacementTransform(left_sin_even, left_sin_even_polar), ReplacementTransform(right_sin_even, right_sin_even_polar))
        self.wait()
        self.play(MoveToTarget(left_sin_even_polar), MoveToTarget(right_sin_even_polar))
        self.wait()
        self.play(ReplacementTransform(VGroup(left_sin_even_polar, right_sin_even_polar), odd_sin_group), ReplacementTransform(sin_even_label, sin_odd_label))
        self.wait()
        self.play(ReplacementTransform(left_sin_odd, left_sin_odd_polar), ReplacementTransform(right_sin_odd, right_sin_odd_polar))
        self.wait()
        self.play(MoveToTarget(left_sin_odd_polar), MoveToTarget(right_sin_odd_polar))
        self.wait()
        self.remove(left_sin_odd_polar, right_sin_odd_polar)
        self.play(Write(explanation6))
        self.wait()
        self.play(explanation6.to_edge, UP, ShowCreation(mod_group, run_time=2.5))
        self.wait()


    def get_mod_polar_sin_curves(self, n, x_min=-PI, x_max=PI):
        result = []
        for i in n:
            graph = FunctionGraph(lambda x: np.abs(np.sin(i * x)), x_min=x_min, x_max=x_max)
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
