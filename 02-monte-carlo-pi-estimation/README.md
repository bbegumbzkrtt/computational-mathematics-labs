# 02. Monte Carlo Methods in Computational Mathematics

## Overview
This module explores **Monte Carlo simulations**—a class of computational algorithms that rely on repeated random sampling to obtain numerical results. Two core applications are implemented:

1. **Stochastic Pi ($\pi$) Estimation** (`main.py`)
2. **Numerical Integration of Trigonometric Functions** (`integration.py`)

---

## 1. Monte Carlo Pi Estimation (`main.py`)

### Mathematical Principle
Consider a circle of radius $r = 1$ inscribed inside a square with side length $L = 2$ centered at the origin $(0,0)$.

- **Area of the Bounding Square:**
  $$A_{\text{square}} = L^2 = 2 \times 2 = 4$$

- **Area of the Inscribed Circle:**
  $$A_{\text{circle}} = \pi \cdot r^2 = \pi \cdot 1^2 = \pi$$

Generating $N$ uniformly distributed random coordinates $(x_i, y_i) \in [-1, 1] \times [-1, 1]$ yields a sample ratio proportional to the geometric area ratio:

$$P \approx \frac{N_{\text{inside}}}{N_{\text{total}}} = \frac{A_{\text{circle}}}{A_{\text{square}}} = \frac{\pi}{4} \implies \pi \approx 4 \cdot \frac{N_{\text{inside}}}{N_{\text{total}}}$$

A point satisfies the inside condition if:
$$x_i^2 + y_i^2 \le 1$$

### Visualization Output
![Monte Carlo Pi Estimation](monte_carlo_pi.png)

---

## 2. Monte Carlo Numerical Integration (`integration.py`)

### Mathematical Principle
Monte Carlo integration estimates definite integrals by taking advantage of the hit-or-miss probability over a bounding region. We evaluate the definite integral of $f(x) = \sin(x)$ over $[0, \pi]$:

$$\int_0^\pi \sin(x) \, dx = \Big[-\cos(x)\Big]_0^\pi = -\cos(\pi) - (-\cos(0)) = 1 + 1 = 2.0$$

#### Bounding Box Setup:
- $x \in [0, \pi]$
- $y \in [0, 1]$ (since $\max(\sin(x)) = 1$ on $[0, \pi]$)
- **Bounding Box Area:** $A_{\text{box}} = (\pi - 0) \times (1 - 0) = \pi$

Points $(x_i, y_i)$ are sampled uniformly within the bounding rectangle. A point lies under the curve if:

$$y_i \le \sin(x_i)$$

The integral value is estimated as:

$$\int_0^\pi \sin(x) \, dx \approx A_{\text{box}} \cdot \frac{N_{\text{under}}}{N_{\text{total}}} = \pi \cdot \frac{N_{\text{under}}}{N_{\text{total}}}$$

### Visualization Output
![Monte Carlo Integration](monte_carlo_integration.png)

---

## Tech Stack & Dependencies
- **Python 3**
- **NumPy** (Vectorized random sampling)
- **Matplotlib** (Data visualization)