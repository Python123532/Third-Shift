# Intro Biophysics Study Guide

*Example output from Third Shift task T-006, made from the "Study guide" starter template. The original is a Google Doc in the user's Drive.*

A one-unit review of the physics that governs cells and molecules: thermal energy, diffusion, fluid flow at small scales, membranes, and single-molecule measurement. Room temperature is 298 K and body temperature 310 K unless a question says otherwise.

## Key terms

- **Thermal energy ($k_BT$):** the typical energy of random molecular motion. At 298 K, $k_BT \approx 4.1\times10^{-21}$ J $\approx 4.1$ pN·nm.
- **Boltzmann distribution:** $P(E) \propto e^{-E/k_BT}$; two states differing by $\Delta E$ have a population ratio of $e^{-\Delta E/k_BT}$.
- **Diffusion coefficient ($D$):** in one dimension $\langle x^2\rangle = 2Dt$ ($6Dt$ in three).
- **Stokes–Einstein relation:** $D = \dfrac{k_BT}{6\pi\eta r}$.
- **Fick's first law:** $J = -D\,\dfrac{dc}{dx}$.
- **Reynolds number:** $Re = \rho v L/\eta$; cells live at $Re \ll 1$.
- **Osmotic pressure (van 't Hoff):** $\Pi = cRT$.
- **Nernst potential:** $V = \dfrac{k_BT}{ze}\ln\dfrac{c_\text{out}}{c_\text{in}}$; at 310 K, $k_BT/e \approx 26.7$ mV.
- **Gibbs free energy:** $\Delta G = \Delta H - T\Delta S$.
- **Hydrophobic effect:** nonpolar groups cluster mainly because it frees ordered water, an entropy gain.
- **Michaelis–Menten:** $v = \dfrac{V_\max[S]}{K_m + [S]}$.
- **FRET:** $E = \dfrac{1}{1 + (r/R_0)^6}$, a ruler at 1 to 10 nm.
- **Optical tweezers:** a trapped bead acts like a spring, $F = -kx$.

## Main ideas

- **Thermal noise rules small scales:** molecular machines work against energies of a few $k_BT$.
- **Diffusion is fast over short distances and slow over long ones:** $t \approx x^2/2D$.
- **At low Reynolds number there is no coasting,** and a reciprocal stroke goes nowhere.
- **Gradients store energy:** ion gradients set resting potentials and power ATP synthesis.
- **Folding is a small free-energy balance.**
- **Single-molecule tools measure what bulk averages hide.**

## Practice questions

1. What is $k_BT$ at 310 K, in pN·nm?
2. A protein has $D = 100\ \mu\text{m}^2/\text{s}$. How long to diffuse 10 μm in 1D? 1 cm?
3. Estimate $D$ for a 2.5 nm sphere in water ($\eta = 10^{-3}$ Pa·s) at 298 K.
4. Estimate $Re$ for a 1 μm bacterium swimming at 30 μm/s. What does it mean?
5. K⁺ is 140 mM inside, 5 mM outside. Nernst potential at 310 K?
6. Osmotic pressure of 300 mM solute at 310 K, in atm?
7. Two states differ by $2k_BT$. Relative population of the higher one?
8. Fraction of $V_\max$ at $[S] = K_m$? At $[S] = 3K_m$?
9. FRET efficiency at $r = R_0$? At $r = 2R_0$?
10. Why can't a one-hinge "scallop" swim at low $Re$?

## Answers

1. $(1.38\times10^{-23})(310) \approx 4.3\times10^{-21}$ J $\approx 4.3$ pN·nm.
2. $t = \dfrac{(10)^2}{2\times100} = 0.5$ s; for 1 cm, $\dfrac{10^8}{200} = 5\times10^5$ s, about 6 days.
3. $D = \dfrac{4.1\times10^{-21}}{6\pi(10^{-3})(2.5\times10^{-9})} \approx 8.7\times10^{-11}$ m²/s $\approx 87\ \mu$m²/s.
4. $Re = \dfrac{(1000)(3\times10^{-5})(10^{-6})}{10^{-3}} \approx 3\times10^{-5}$: viscosity dominates, no inertia.
5. $V = 26.7\ln(5/140) \approx -89$ mV.
6. $\Pi = (300)(8.314)(310) \approx 7.7\times10^5$ Pa $\approx 7.6$ atm.
7. $e^{-2} \approx 0.14$.
8. $0.5\,V_\max$; $\dfrac{3}{4} = 0.75\,V_\max$.
9. $0.5$; $\dfrac{1}{65} \approx 0.015$.
10. At low $Re$ motion depends only on the sequence of shapes; a hinge retraces its shapes in reverse, so each stroke undoes the last (Purcell's scallop theorem).

## Sources

- Phillips, Kondev and Theriot, *Physical Biology of the Cell*; Nelson, *Biological Physics*.
- Purcell, E. M. (1977). Life at low Reynolds number. *American Journal of Physics*, 45(1), 3–11.
