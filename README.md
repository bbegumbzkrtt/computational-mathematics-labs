# Computational Mathematics & Visualizations
Welcome! This repository serves as an academic archive for my computational mathematics, algorithmic simulation, and data visualization projects developed during my undergraduate studies in **Mathematics**.
The primary goal of these projects is to bridge theoretical mathematical concepts-ranging from discrete systems and dynamical behavior to linear algebra and number theory-with computational implementation using Python.
---
## Project Directory
### 01. Rule 30 Cellular Automata
* **Folder:** ['/01-rule-30-cellular-automata'](./01-rule-30-cellular-automata)
* **Topics:** Discrete Mathematics, Cellular Automata, Deterministic Chaos, Complex Systems.
*  **Tech Stack:** `Python 3`, `NumPy`, `Matplotlib`.
*  **Summary:** Simulation of Stephen Wolfram's **Rule 30** 1D elementary cellular automaton. It demonstrates how estremely simple deterministic transition rules applied to binary states can generate infinitely complex, non-periodic, chaotic patterns.

### 02. Monte Carlo Methods
* **Folder:** ['02-monte-carlo-methods'](./02-monte-carlo-methods)
* **Topics:** Probability Theory, Stochastic Simulations, Numerical Integration, Law of Large Numbers.
* **Tech Stack:** `Python 3`, `NumPy`, `Matplotlib`.
* **Summary:** Implementation of Monte Carlo algorithms for probabilistic mathematical estimation. Features stochastic estimation of Pi ($\pi$) via uniform area sampling and numerical integration of trigonometric functions f(x) = sin(x).

### 03. Chaos Theory & Lorenz Attractor
* **Folder:** ['/03-chaos-theory-lorenz-attractor'](./03-chaos-theory-lorenz-attractor)
* **Topics:** Ordinary Differential Equations, Chaos Theory, Dynamical Systems, Euler Integration.
* **Tech Stack:** `Python 3`, `NumPy`, `Matplotlib`.
* **Summary:** Simulation of Edward Lorenz's 3D non-linear atmospheric convection model. Demonstrates deterministic chaos and sensitive dependence on initial conditions (Butterfly Effect) using first-order numerical integration.

---

## Mathematical Overview: Rule 30

In Rule 30, the state of cell $C_i$ at time step $t+1$ depends strictly on its current state and its left/right neighbors at time $t$:

$$C_i^{t+1} = \text{Rule}(C_{i-1}^t, C_i^t, C_{i+1}^t)$$

### Transition Rules:
| $C_{i-1}^t C_i^t C_{i+1}^t$ | 111 | 110 | 101 | 100 | 011 | 010 | 001 | 000 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$C_i^{t+1}$** | **0** | **0** | **0** | **1** | **1** | **1** | **1** | **0** |

---

## Mathematical Overview: Monte Carlo Methods

### 1. Pi ($\pi$) Estimation
By inscribing a unit circle ($r = 1$) inside a bounding square ($L = 2$), $N$ uniform random points are generated over $[-1, 1] \times [-1, 1]$. The ratio of points landing inside the circle approximates the geometric area ratio:

$$\frac{N_{\text{inside}}}{N_{\text{total}}} \approx \frac{A_{\text{circle}}}{A_{\text{square}}} = \frac{\pi}{4} \implies \pi \approx 4 \cdot \frac{N_{\text{inside}}}{N_{\text{total}}}$$

### 2. Numerical Integration
Definite integration over a region $[a, b] \times [0, y_{\text{max}}]$ using hit-or-miss probability:

$$\int_{0}^{\pi} \sin(x) \, dx \approx A_{\text{box}} \cdot \frac{N_{\text{under}}}{N_{\text{total}}} = \pi \cdot \frac{N_{\text{under}}}{N_{\text{total}}}$$

### 3. Non-Elementary Integration (Gaussian Integral)
Estimating non-elementary integrals where traditional anti-derivatives do not exist (e.g., $f(x) = e^{-x^2}$ over $[0, 1]$):

$$\int_{0}^{1} e^{-x^2} \, dx \approx A_{\text{box}} \cdot \left( \frac{N_{\text{under}} - N_{\text{above}}}{N_{\text{total}}} \right)$$

### 4. Sinc Function Integration
Integrating the non-elementary Sinc function $f(x) = \frac{\sin(x)}{x}$ over $[0, \pi]$:

$$\int_{0}^{\pi} \frac{\sin(x)}{x} \, dx \approx A_{\text{box}} \cdot \frac{N_{\text{under}}}{N_{\text{total}}} = \pi \cdot \frac{N_{\text{under}}}{N_{\text{total}}} \approx 1.851937$$

---

## Mathematical Overview: Chaos Theory & Lorenz Attractor

The Lorenz system models 3D chaotic fluid convection through three coupled ordinary differential equations:

$$\frac{dx}{dt} = \sigma (y - x)$$

$$\frac{dy}{dt} = x (\rho - z) - y$$

$$\frac{dz}{dt} = x y - \beta z$$

Trajectory points are iteratively updated via Euler's method with step size $\Delta t$:

$$x_{n+1} = x_n + \sigma (y_n - x_n) \Delta t$$

$$y_{n+1} = y_n + \left[ x_n (\rho - z_n) - y_n \right] \Delta t$$

$$z_{n+1} = z_n + \left( x_n y_n - \beta z_n \right) \Delta t$$

### Dynamics & Phase Transitions (`parameter_sweep.py`)

Varying the Rayleigh heating parameter $\rho$ induces qualitative regime changes in phase space:

* **$\rho = 14.0$ (Fixed Point Attractor):** Low thermal Rayleigh energy causes trajectories to spiral inward and decay to a stable fixed point.
* **$\rho = 28.0$ (Chaotic Butterfly Attractor):** The classical chaotic regime characterized by non-periodic orbits around two unstable foci.
* **$\rho = 99.96$ (Periodic Orbit / Knot):** High energy limits chaotic divergence, forcing trajectories into a deterministic closed loop.

### Sensitivity to Initial Conditions (`butterfly_effect_sensitivity.py`)

To evaluate the **Butterfly Effect**, two trajectories $A(t)$ and $B(t)$ are integrated simultaneously with a micro-perturbation of $\Delta z = 0.0001$:

$$D(t) = \sqrt{(x_A - x_B)^2 + (y_A - y_B)^2 + (z_A - z_B)^2}$$

Positive Lyapunov exponents cause exponential spatial separation over time, illustrating the fundamental unpredictability of deterministic chaotic systems.

---

## Mathematical Overview: Fourier Transform & Signal Processing

The Fourier Transform decomposes arbitrary time-domain signals into their constituent orthogonal frequency components, mapping spatial or temporal data into the frequency domain.

### Signal Denoising & Spectral Filtering (`fourier_denoising.py`)
Discrete time series signals $x_k$ are transformed via Discrete Fourier Transform (DFT):

$$X_k = \sum_{n=0}^{N-1} x_n e^{-i 2\pi \frac{k n}{N}}$$

Stochastic background noise is filtered by applying a power threshold to the Power Spectral Density ($PSD = \frac{|X_k|^2}{N}$). The clean signal is reconstructed using the Inverse Fast Fourier Transform (IFFT).

### Time-Frequency Spectrogram (`audio_spectrogram.py`)
To analyze non-stationary signals with time-varying frequencies, Short-Time Fourier Transform (STFT) computes spectral power over sliding windowed segments:

$$STFT\{x[n]\}(m, \omega) = \sum_{n=-\infty}^{\infty} x[n] w[n - m] e^{-i \omega n}$$

### 2D Curve Reconstruction via Epicycles (`fourier_epicycles.py`)
Closed 2D parametric curves $z(t) = x(t) + i \cdot y(t)$ are modeled using complex Fourier series. Summing $K$ dominant harmonic vectors (rotating epicycles) reconstructs continuous spatial geometry:

$$z(t) \approx \sum_{n=-K}^{K} c_n e^{i \frac{2\pi n t}{T}}$$

---