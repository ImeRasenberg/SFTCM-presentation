# manim-slides convert PairingIntro PairingIntro.html
from manim import *
from manim_slides import Slide
import numpy as np


class PairingIntro(Slide):
    def construct(self):

        # --------------------------------------------------
        # Slide 1: Free electron wavefunction
        # --------------------------------------------------
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[-1.5, 1.5, 1],
            axis_config={"include_numbers": False},
        )

        wave = axes.plot(
            lambda x: np.sin(3 * x),
            color=BLUE
        )

        psi_label = MathTex(
            r"\psi_k(x)=e^{ikx}"
        ).to_corner(UR)

        self.play(Create(axes), Create(wave), FadeIn(psi_label))
        self.next_slide()

        # --------------------------------------------------
        # Slide 2: Exchange particles
        # --------------------------------------------------
        particle1 = Dot(color=BLUE).shift(LEFT * 2)
        particle2 = Dot(color=RED).shift(RIGHT * 2)

        label12 = MathTex(r"\psi(1,2)").to_edge(UP)

        self.play(
            FadeOut(axes),
            FadeOut(wave),
            FadeOut(psi_label),
            FadeIn(particle1),
            FadeIn(particle2),
            FadeIn(label12),
        )

        self.play(
            particle1.animate.move_to(RIGHT * 2),
            particle2.animate.move_to(LEFT * 2),
            Transform(label12, MathTex(r"\psi(2,1)").to_edge(UP)),
            run_time=1.5
        )

        minus = MathTex(r"\psi(1,2) = -\psi(2,1)").move_to(DOWN * 2)
        self.play(FadeIn(minus))
        self.next_slide()

        # --------------------------------------------------
        # Slide 3: Singlet and triplet
        # --------------------------------------------------
        singlet = MathTex(
            r"\chi_s=\frac{1}{\sqrt2}(\uparrow\downarrow-\downarrow\uparrow)"
        ).shift(UP)

        triplet = MathTex(
            r"\chi_t=\frac{1}{\sqrt2}(\uparrow\downarrow+\downarrow\uparrow)"
        ).shift(DOWN)

        self.play(
            FadeOut(minus),
            FadeOut(label12),
            FadeIn(singlet),
            FadeIn(triplet)
        )
        self.next_slide()

        # --------------------------------------------------
        # Slide 4: Total wavefunction symmetry
        # --------------------------------------------------
        total1 = MathTex(
            r"\Psi=\phi_{sym}(r_1,r_2)\chi_s"
        ).shift(UP)

        total2 = MathTex(
            r"\Psi=\phi_{antisym}(r_1,r_2)\chi_t"
        ).shift(DOWN)

        self.play(
            Transform(singlet, total1),
            Transform(triplet, total2)
        )
        self.next_slide()

        # --------------------------------------------------
        # Slide 5: Spatial overlap + attraction
        # --------------------------------------------------
        left_peak = FunctionGraph(
            lambda x: np.exp(-(x + 1.5) ** 2 / 0.3),
            x_range=[-4, 4],
            color=BLUE
        )

        overlap_peak = FunctionGraph(
            lambda x: 1.5 * np.exp(-(x) ** 2 / 0.6),
            x_range=[-4, 4],
            color=GREEN
        )

        attract = MathTex(
            r"\mathrm{large\ overlap} \;\Rightarrow\; V<0"
        ).to_edge(DOWN)

        self.play(
            FadeOut(total2),
            Transform(total1, MathTex(r"\phi_{sym}\Rightarrow \text{large overlap}").to_edge(UP)),
            FadeIn(left_peak),
            FadeIn(overlap_peak),
        )

        self.play(FadeIn(attract))
        self.next_slide()