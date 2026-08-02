import numpy as np
import matplotlib.pyplot as plt

def generate_rule30(steps=250, width=501):
    """
    Generates a 2D array representing the state of Rule 30 Cellular Automaton over time.
    
    Parameters:
        steps (int): Number of time steps (rows).
        width (int): Width of the grid (columns).
        
    Returns:
        np.ndarray: 2D binary grid containing the simulation history.
    """
    # Initialize grid with zeros
    grid = np.zeros((steps, width), dtype=int)
    
    # Set the initial state: single active cell in the middle
    grid[0, width // 2] = 1

    # Binary mapping dictionary for Rule 30 transitions
    rule_30 = {
        (1, 1, 1): 0, (1, 1, 0): 0, (1, 0, 1): 0, (1, 0, 0): 1,
        (0, 1, 1): 1, (0, 1, 0): 1, (0, 0, 1): 1, (0, 0, 0): 0
    }

    # Evolve the cellular automaton through time
    for t in range(1, steps):
        for i in range(1, width - 1):
            neighborhood = (grid[t - 1, i - 1], grid[t - 1, i], grid[t - 1, i + 1])
            grid[t, i] = rule_30[neighborhood]

    return grid

if __name__ == "__main__":
    # Generate grid with 250 steps for deeper resolution
    grid = generate_rule30(steps=250, width=501)

    # Visualization Setup (Dark Mode & Cyberpunk/Ocean Colormap)
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Render with 'cool' colormap for high-contrast neon aesthetics
    cax = ax.imshow(grid, cmap='cool', interpolation='nearest')

    # Configure plot title and axes
    ax.set_title("Rule 30 - Deep Ocean & Cyberpunk Edition", fontsize=14, color='cyan', pad=12)
    ax.axis('off')  # Hide frame and axes for a clean graphical output

    # Save output image inside the project folder
    output_path = "01-rule-30-cellular-automata/rule_30_ocean_neon.png"
    plt.savefig(output_path, bbox_inches='tight', dpi=300, facecolor=fig.get_facecolor())
    print(f"Success: High-resolution visual output saved to {output_path}")
