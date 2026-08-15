import matplotlib.pyplot as plt
import numpy as np


def monte_carlo_integral_solver():
    print("=" * 60)
    print("  MONTE CARLO INTEGRAL SOLVER & VISUALIZER  ")
    print("=" * 60)

    # 1. Get user inputs
    expr_input = input(
        "Enter function f(x) using NumPy syntax (e.g., np.exp(-x**2), np.sin(x**2)): "
    )
    a = float(input("Enter lower limit (a): "))
    b = float(input("Enter upper limit (b): "))
    N = int(
        input("Enter number of random points (N) [e.g., 50000]: ")
    )

    # Define function dynamically
    def f(x):
        return eval(expr_input)

    # 2. Determine bounding box for random sampling
    x_grid = np.linspace(a, b, 1000)
    y_grid = f(x_grid)
    y_min = min(0, np.min(y_grid))
    y_max = max(np.max(y_grid), 0)

    # 3. Generate uniform random points
    x_rand = np.random.uniform(a, b, N)
    y_rand = np.random.uniform(y_min, y_max, N)

    # 4. Check if points fall inside the area under the curve
    fx_rand = f(x_rand)
    under_curve = (y_rand >= 0) & (y_rand <= fx_rand)
    above_curve = (y_rand < 0) & (y_rand >= fx_rand)
    inside_mask = under_curve | above_curve

    # 5. Calculate approximate integral
    box_area = (b - a) * (y_max - y_min)
    positive_count = np.sum(under_curve)
    negative_count = np.sum(above_curve)

    approx_integral = box_area * (
        (positive_count - negative_count) / N
    )

    print("\n" + "-" * 60)
    print(f" Approximate Integral Value: {approx_integral:.6f}")
    print("-" * 60)

    # 6. Plotting and Visualization
    plt.figure(figsize=(10, 6))

    # Plot the function curve
    plt.plot(
        x_grid, y_grid, color="black", linewidth=2, label=f"f(x) = {expr_input}"
    )

    # Plot sampled points (subsample up to 3000 points to keep plot rendering fast)
    sample_size = min(N, 3000)
    plt.scatter(
        x_rand[:sample_size][inside_mask[:sample_size]],
        y_rand[:sample_size][inside_mask[:sample_size]],
        color="green",
        s=5,
        alpha=0.5,
        label="Inside Region (Contributes to Integral)",
    )
    plt.scatter(
        x_rand[:sample_size][~inside_mask[:sample_size]],
        y_rand[:sample_size][~inside_mask[:sample_size]],
        color="red",
        s=5,
        alpha=0.3,
        label="Outside Region",
    )

    # Styling and Labels
    plt.axhline(0, color="gray", linestyle="--", linewidth=1)
    plt.axvline(0, color="gray", linestyle="--", linewidth=1)
    plt.title(
        f"Monte Carlo Integration Visualizer\nApproximate Value: {approx_integral:.5f} (N={N})",
        fontsize=12,
    )
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend(loc="upper right")
    plt.grid(True, alpha=0.3)

    # Save output and show
    plt.savefig("monte_carlo_result.png", dpi=300, bbox_inches="tight")
    print("\nVisualization saved successfully as 'monte_carlo_result.png'!")
    plt.show()


if __name__ == "__main__":
    monte_carlo_integral_solver()