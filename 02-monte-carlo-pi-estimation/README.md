# 02. Monte Carlo Pi Estimation

## Overview
This module implements a stochastic simulation using the **Monte Carlo method** to approximate the mathematical constant $\pi$. By utilizing uniform random sampling over a defined geometric space, the algorithm demonstrates the **Law of Large Numbers** in computational probability.

## Mathematical Formulation
Consider a circle of radius $r = 1$ inscribed inside a square with side length $L = 2$ centered at the origin $(0,0)$.

- **Area of the Bounding Square:**
  $$A_{\text{square}} = L^2 = 2 \times 2 = 4$$

- **Area of the Inscribed Circle:**
  $$A_{\text{circle}} = \pi \cdot r^2 = \pi \cdot 1^2 = \pi$$

When generating $N$ uniformly distributed random points $(x_i, y_i) \in [-1, 1] \times [-1, 1]$, the probability $P$ of a point falling inside the circle is equal to the ratio of their areas:

$$P \approx \frac{N_{\text{inside}}}{N_{\text{total}}} = \frac{A_{\text{circle}}}{A_{\text{square}}} = \frac{\pi}{4}$$

Solving for $\pi$ yields the estimation formula:

$$\pi \approx 4 \cdot \frac{N_{\text{inside}}}{N_{\text{total}}}$$

A point $(x_i, y_i)$ lies inside the unit circle if it satisfies the inequality:

$$x_i^2 + y_i^2 \le 1$$

## Visualization Output
The simulation exports a monochromatic high-resolution plot highlighting points inside and outside the unit circle boundary:

![Monte Carlo Pi Plot](monte_carlo_pi.png)

## Tech Stack
- **Python 3**
- **NumPy** (Vectorized random point generation)
- **Matplotlib** (Data visualization)