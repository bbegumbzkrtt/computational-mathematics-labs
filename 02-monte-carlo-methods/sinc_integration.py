import numpy as np
import matplotlib.pyplot as plt

# 1. Function definition (handling 0/0 indeterminate form at x = 0)
def sinc(x):
    return np.where(x == 0, 1.0, np.sin(x) / x)

a, b = 0, np.pi
y_min, y_max = 0, 1.0  # Peak value occurs at f(0) = 1.0
N = 25000

# 2. Monte Carlo Random Sampling
np.random.seed(42)
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(y_min, y_max, N)

# 3. Identify Points Under Curve
under_curve = y_rand <= sinc(x_rand)

# 4. Integration Estimation
box_area = (b - a) * (y_max - y_min)
estimated_integral = box_area * (np.sum(under_curve) / N)
exact_value = 1.85193705  # Analytical value Si(pi)

print(f"Estimated Integral: {estimated_integral:.6f}")
print(f"Exact Value Si(pi): {exact_value:.6f}")
print(f"Absolute Error:     {abs(estimated_integral - exact_value):.6f}")

# 5. Visualization Output
plt.figure(figsize=(8, 5))
x_vals = np.linspace(a, b, 500)
plt.plot(x_vals, sinc(x_vals), 'k-', linewidth=2, label=r'$f(x) = \frac{\sin(x)}{x}$')

plt.scatter(x_rand[under_curve], y_rand[under_curve], color='#8a2be2', s=1, alpha=0.5, label='Under Curve')
plt.scatter(x_rand[~under_curve], y_rand[~under_curve], color='#d3d3d3', s=1, alpha=0.3, label='Above Curve')

plt.title(f'Monte Carlo Sinc Integration: $\\int_0^\\pi \\frac{{\\sin(x)}}{{x}} dx$\nSamples (N) = {N:,} | Estimate = {estimated_integral:.5f} (Exact ≈ {exact_value:.5f})')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right')
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('02-monte-carlo-methods/assets/sinc_integration.png', dpi=300)
plt.show()