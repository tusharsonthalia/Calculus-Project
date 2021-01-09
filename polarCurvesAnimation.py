from manimlib.imports import *


class PolarCurve(ParametricFunction):
    CONFIG = {
        "theta_min": 0,
        "theta_max": TAU,
        "color": TEAL
    }

    def __init__(self, function, **kwargs):
        digest_config(self, kwargs)
        self.polar_function = \
            lambda t: np.array(
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
        # func = PolarCurve(lambda theta: 1)
        # self.play(ShowCreation(func))
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
        r_label.move_to( np.array([-2.5, -1.2, 0]))
        angle_arc = ArcBetweenPoints(np.array([-3.5, -3, 0]), np.array([-3.7, -2.7, 0]))
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
        grid.generate_target()
        grid.target.prepare_for_nonlinear_transform()
        grid.target.apply_function(lambda point: self.polar_to_c(point))

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
        self.play(ReplacementTransform(explanation1, explanation2), ShowCreation(graph_group))
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
        self.play(MoveToTarget(grid, run_time=3))
        self.wait(2)
        self.play(ReplacementTransform(explanation3, explanation4), ReplacementTransform(grid, grid_copy, run_time = 3))
        self.wait()
    
    def polar_to_c(self, point):
        return np.array([
            point[0] * np.cos(point[1]),
            point[0] * np.sin(point[1]),
            0
        ])
