from manim import *
import numpy as np

class HoliCinemaScene(ThreeDScene):
    def construct(self):

        # 1️⃣ Camera Setup
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)

        # 2️⃣ Torus
        torus = Torus(major_radius=2, minor_radius=0.7)
        torus.set_fill_by_checkerboard(RED, ORANGE, opacity=0.8)

        self.play(FadeIn(torus), run_time=2)
        self.wait(1)

        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(3)

        # 3️⃣ Hyperbolic Surface
        surface = Surface(
            lambda u, v: np.array([u, v, u**2 - v**2]),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=(40, 40),
        )

        surface.set_fill_by_checkerboard(
            RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE,
            opacity=0.85
        )

        self.play(Transform(torus, surface), run_time=4)
        self.wait(3)

        # 4️⃣ Color Pulse
        for color in [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]:
            self.play(torus.animate.set_color(color), run_time=0.4)

        self.wait(1)

        # 5️⃣ Fade Geometry
        self.play(FadeOut(torus), run_time=3)
        self.stop_ambient_camera_rotation()

        # 🔥 VERY IMPORTANT FIX
        self.move_camera(phi=0, theta=0, zoom=1)
        self.wait(1)

        # 6️⃣ Final Stable Text (NO ROTATION)
        final_text = Tex(r"\textbf{Happy Holi --- On Every Manifold}")
        final_text.scale(1.2)
        final_text.set_color_by_gradient(
            RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE
        )

        # Make text fixed to screen (no 3D rotation)
        self.add_fixed_in_frame_mobjects(final_text)

        self.play(FadeIn(final_text), run_time=3)
        self.wait(4)
