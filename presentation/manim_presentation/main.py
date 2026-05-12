# manim-slides convert MyPresentation presentation.html

from manim import *
from manim_slides import Slide
import numpy as np

class MyPresentation(Slide):

    def construct(self):

        # -------------------------
        # Axes (shared across slides)
        # -------------------------
        axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[0, 2.5, 1],
            axis_config={"include_numbers": False}
        )

        self.add(axes)

        # -------------------------
        # Slide 1: Parabolic dispersion
        # -------------------------
        parabola = axes.plot(
            lambda k: k**2,
            color=BLUE
        )

        self.play(Create(parabola))
        self.next_slide()

        # -------------------------
        # Slide 2: Fermi level + occupation
        # -------------------------

        EF = 1

        # Fermi line
        fermi_line = axes.plot(
            lambda x: EF,
            color=RED
        )

        EF_label = MathTex(r"E_F = 1")

        EF_label.move_to(axes.c2p(1.6, EF+0.3))  # x chosen to be visually right side

        self.play(
            Create(fermi_line),
            FadeIn(EF_label)
        )

        # Full dispersion (reference, thin)
        full_parabola = axes.plot(
            lambda k: k**2,
            color=BLUE,
            stroke_width=2
        )

        # Occupied region: E(k) <= EF
        k_max = np.sqrt(EF)

        low_energy_part = axes.plot(
            lambda k: k**2,
            x_range=[-k_max, k_max],
            color=BLUE,
            stroke_width=12
        )

        self.play(
            Transform(parabola, full_parabola),
            FadeIn(low_energy_part)
        )

        # Ensure Fermi line stays on top
        self.bring_to_front(fermi_line)
        self.bring_to_front(EF_label)

        self.next_slide()