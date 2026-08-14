import matplotlib.pyplot as plt
import numpy as np

def estimate_pi_monte_carlo(num_samples: int = 20000) -> tuple[np.ndarray, np.ndarray, np.ndarray, float]:
    """
    Estimates the value of Pi using the Monte Carlo simulation technique.

    Parameters:
        num_samples (int): Total number of random points generated inside the square.

    Returns:
        tuple: (x coordinates, y coordinates, boolean mask for points inside circle, estimated pi value)
    """
    # Generate uniform random coordinates (x, y) within the bounding square [-1, 1] x [-1, 1]
    x = np.random.uniform(-1, 1, num_samples)
    y = np.random.uniform(-1, 1, num_samples)

    # Calculate squared Euclidean distance from origin (x^2 + y^2 <= 1 indicates point inside unit circle)
    inside_mask = (x**2 + y**2) <= 1.0

    # Count points falling strictly inside the unit circle
    num_inside = np.sum(inside_mask)

    # Estimate Pi based on the area ratio: Area_circle / Area_square = Pi / 4
    pi_estimate = 4.0 * (num_inside / num_samples)

    return x, y, inside_mask, pi_estimate


def plot_and_save_monte_carlo(num_samples: int = 20000, filename: str = "monte_carlo_pi.png") -> None:
    """
    Visualizes the Monte Carlo Pi estimation using a high-contrast monochromatic style
    and saves the output as a publication-ready PNG file.
    """
    x, y, inside_mask, pi_estimate = estimate_pi_monte_carlo(num_samples)

    # Initialize figure
    plt.figure(figsize=(8, 8), dpi=300)

    # Plot points using monochromatic palette (Black for inside, Dark Grey for outside)
    plt.scatter(x[inside_mask], y[inside_mask], color='black', s=1.5, alpha=0.7, label='Inside Circle')
    plt.scatter(x[~inside_mask], y[~inside_mask], color='darkgray', s=1.5, alpha=0.5, label='Outside Circle')

    # Draw the unit circle boundary
    theta = np.linspace(0, 2 * np.pi, 360)
    plt.plot(np.cos(theta), np.sin(theta), color='black', linewidth=1.5, label='Unit Circle Boundary')

    # Configure labels and layout
    plt.title(
        f"Monte Carlo Pi Estimation\nSamples (N) = {num_samples:,} | Estimated $\pi \\approx {pi_estimate:.5f}$", 
        fontsize=13, 
        fontweight='bold', 
        pad=12
    )
    plt.xlabel("X Coordinate", fontsize=11)
    plt.ylabel("Y Coordinate", fontsize=11)
    plt.axis('equal')
    plt.xlim(-1.05, 1.05)
    plt.ylim(-1.05, 1.05)
    plt.legend(loc='upper right', frameon=True)
    plt.grid(False)

    # Save figure to file
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    plot_and_save_monte_carlo(num_samples=20000)