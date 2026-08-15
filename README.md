# Computational Mathematics & Visualizations
Welcome! This repository serves as an academic archive for my computational mathematics, algorithmic simulation, and data visualization projects developed during my undergraduate studies in **Mathematics**.
The primary goal of these projects is to bridge theoretical mathematical concepts-ranging from discrete systems and dynamical behavior to linear algebra and number theory-with computational implementation using Python.
---
## Project Directory
### 01. Rule 30 Cellular Automata
* **Folder:** ['/01-rule-30-cellular-automata'](./01-rule-30-cellular-automata)
* **Topics:** Discrete Mathematics, Cellular Automata, Deterministic Chaos, Complex Systems.
*  **Tech Stack:** 'Python 3', 'NumPy', 'Matplotlib'.
*  **Summary:** Simulation of Stephen Wolfram's **Rule 30** 1D elementary cellular automaton. It demonstrates how estremely simple deterministic transition rules applied to binary states can generate infinitely complex, non-periodic, chaotic patterns.
### 02. Monte Carlo Methods
* **Folder:** ['02-monte-carlo-methods'](./02-monte-carlo-methods)
* **Topics:** Probability Theory, Stochastic Simulations, Numerical Integration, Law of Large Numbers.
* **Tech Stack:** 'Python 3', 'NumPy', 'Matplotlib'.
* **Summary:** Implementation of Monte Carlo algorithms for probabilistic mathematical estimation. Features stochastic estimation of Pi ($\pi$) via uniform area sampling and numerical integration of trigonometric functions f(x) = sin(x).
---
## Mathematical Overview: Rule 30

In Rule 30, the state of cell $C_i$ at time step $t+1$ depends strictly on its current state and its left/right neighbors at time $t$:

$$C_i^{t+1} = \text{Rule}(C_{i-1}^t, C_i^t, C_{i+1}^t)$$

### Transition Rules:
| $C_{i-1}^t C_i^t C_{i+1}^t$ | 111 | 110 | 101 | 100 | 011 | 010 | 001 | 000 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **$C_i^{t+1}$** | **0** | **0** | **0** | **1** | **1** | **1** | **1** | **0** |

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
