import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

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
    
    # Set initial state: single active cell in the middle
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
    # Generate 250-step high-resolution simulation grid
    grid = generate_rule30(steps=250, width=501)

    # Aesthetic Color Palette Setup (Midnight Ocean Theme)
    bg_color = '#000814'  # Deep Midnight Navy
    fg_color = '#00f5d4'  # Vibrant Cyan/Turquoise
    
    # Create custom high-contrast colormap
    custom_cmap = LinearSegmentedColormap.from_list("midnight_ocean", [bg_color, fg_color])

    # Plot Setup
    fig, ax = plt.subplots(figsize=(12, 8), facecolor=bg_color)
    ax.set_facecolor(bg_color)
    
    # Render automaton grid
    ax.imshow(grid, cmap=custom_cmap, interpolation='nearest')

    # Figure styling
    ax.set_title("Rule 30 - Midnight Ocean Visualization", fontsize=14, color=fg_color, pad=14, fontweight='bold')
    ax.axis('off')  # Remove axes for clean graphical aesthetic

    # Save output image
    output_path = "01-rule-30-cellular-automata/rule_30_ocean_neon.png"
    plt.savefig(output_path, bbox_inches='tight', dpi=300, facecolor=bg_color)
    print(f"Success: Aesthetically enhanced output saved to {output_path}")