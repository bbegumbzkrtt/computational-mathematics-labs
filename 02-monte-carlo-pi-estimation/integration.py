import matplotlib.pyplot as plt
import numpy as np

def monte_carlo_integration(num_samples: int = 15000) -> tuple[np.ndarray, np.ndarray, np.ndarray, float]:
    """
    Estimates the definite integral of f(x) = sin(x) over the interval [0, pi]
    using the Monte Carlo hit-or-miss integration technique.

    Exact Analytical Value:
        ∫_0^π sin(x) dx = [-cos(x)]_0^π = -cos(π) - (-cos(0)) = 1 + 1 = 2.0

    Bounding Box Specification:
        x ∈ [0, π],  y ∈ [0, 1]
        Total Box Area = π * 1 = π
    """
    a, b = 0.0, np.pi
    y_max = 1.0
    box_area = (b - a) * y_max

    # Uniformly random sample points inside the bounding box [0, π] x [0, 1]
    x = np.random.uniform(a, b, num_samples)
    y = np.random.uniform(0, y_max, num_samples)

    # Condition: Points that fall strictly beneath the target curve f(x) = sin(x)
    under_curve = y <= np.sin(x)

    # Estimate Area: (Points under curve / Total points) * Bounding Box Area
    integral_estimate = box_area * (np.sum(under_curve) / num_samples)

    return x, y, under_curve, integral_estimate


def plot_and_save_integration(num_samples: int = 15000, filename: str = "monte_carlo_integration.png") -> None:
    """
    Plots the Monte Carlo integration visualization using a clean monochromatic theme
    and exports a publication-ready PNG graphic.
    """
    x, y, under_curve, integral_estimate = monte_carlo_integration(num_samples)

    # Set up figure dimensions
    plt.figure(figsize=(9, 5.5), dpi=300)

    # Plot sample points: Black for inside region, Dark Grey for outside region
    plt.scatter(x[under_curve], y[under_curve], color='black', s=1.8, alpha=0.7, label='Points Under $f(x)$')
    plt.scatter(x[~under_curve], y[~under_curve], color='darkgray', s=1.8, alpha=0.4, label='Points Above $f(x)$')

    # Plot exact mathematical function curve f(x) = sin(x)
    x_curve = np.linspace(0, np.pi, 400)
    y_curve = np.sin(x_curve)
    plt.plot(x_curve, y_curve, color='black', linewidth=2.0, label=r'$f(x) = \sin(x)$')

    # Formatting and Math LaTeX Labels
    plt.title(
        f"Monte Carlo Numerical Integration: $\int_{{0}}^{{\pi}} \sin(x) \, dx$\n"
        f"Samples (N) = {num_samples:,} | Estimated Integral = {integral_estimate:.5f} (Exact = 2.0)",
        fontsize=12,
        fontweight='bold',
        pad=12
    )
    plt.xlabel("x", fontsize=11)
    plt.ylabel("y", fontsize=11)
    plt.xlim(-0.1, np.pi + 0.1)
    plt.ylim(-0.05, 1.1)
    
    # Custom x-axis ticks with Pi formatting
    plt.xticks(
        [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi],
        ['$0$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$']
    )
    plt.legend(loc='upper right', frameon=True)
    plt.grid(False)

    # Export figure
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    plot_and_save_integration(num_samples=15000)