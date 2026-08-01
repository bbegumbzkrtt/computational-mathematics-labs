import numpy as np
import matplotlib.pyplot as plt

def generate_rule30(steps: int = 100, width: int = 201) -> np.ndarray:
    """
    Generates a 1D Cellular Automata grid based on Stephen Wolfram's Rule 30.
    
    Parameters:
        steps (int): Total number of time generations (rows).
        width (int): Total number of cells per generation (columns).
        
    Returns:
        np.ndarray: 2D binary matrix representing the evolution over time.
    """
    # Initialize grid with zeros
    grid = np.zeros((steps, width), dtype=int)
    
    # Set initial state: Single active cell in the center row
    grid[0, width // 2] = 1
    
    # Binary mapping dictionary for Rule 30 transitions
    # Neighborhood mapping: (Left, Center, Right) -> Next State
    rule_30 = {
        (1, 1, 1): 0,
        (1, 1, 0): 0,
        (1, 0, 1): 0,
        (1, 0, 0): 1,
        (0, 1, 1): 1,
        (0, 1, 0): 1,
        (0, 0, 1): 1,
        (0, 0, 0): 0
    }
    
    # Evolve the cellular automaton over time steps
    for t in range(1, steps):
        for i in range(1, width - 1):
            neighborhood = (grid[t - 1, i - 1], grid[t - 1, i], grid[t - 1, i + 1])
            grid[t, i] = rule_30[neighborhood]
            
    return grid


def plot_and_save(grid: np.ndarray, filename: str = "rule_30_pattern.png") -> None:
    """
    Visualizes the generated grid using Matplotlib and saves the output as PNG.
    """
    plt.figure(figsize=(10, 6))
    plt.imshow(grid, cmap='binary', interpolation='nearest')
    plt.title("Rule 30 Elementary Cellular Automaton", fontsize=14, fontweight='bold')
    plt.xlabel("Cell Index (Position)", fontsize=11)
    plt.ylabel("Time Step (Generation)", fontsize=11)
    
    # Save high-resolution pattern image for documentation
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()


if __name__ == "__main__":
    # Simulation Parameters
    TIME_STEPS = 100
    GRID_WIDTH = 201
    
    # Run Simulation
    automata_grid = generate_rule30(steps=TIME_STEPS, width=GRID_WIDTH)
    
    # Render and Save Output
    plot_and_save(automata_grid, filename="rule_30_pattern.png")
