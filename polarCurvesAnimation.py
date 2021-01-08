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

        self.play(Write(intro_text))
        self.wait(2)
