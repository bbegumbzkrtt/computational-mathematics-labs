import os
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Define Transformation Matrix A and Unit Circle Grid ---
# A non-symmetric 2x2 matrix representing a shear + stretch linear transformation
A = np.array([
    [1.5, 0.5],
    [0.2, 0.8]
])

# Compute analytical Eigenvalues and Eigenvectors: A * v = lambda * v
eigenvalues, eigenvectors = np.linalg.eig(A)

# Create a dense unit circle set of vectors v in R^2
theta = np.linspace(0, 2 * np.pi, 200)
unit_circle = np.array([np.cos(theta), np.sin(theta)])  # Shape: (2, 200)

# Apply linear transformation: A * v
transformed_circle = A @ unit_circle                   # Shape: (2, 200)

# --- 2. Professional Visualization Setup ---
plt.style.use('dark_background')
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Subplot 1: Original Domain (Unit Circle & Unit Eigenvectors)
axes[0].plot(unit_circle[0, :], unit_circle[1, :], color='cyan', alpha=0.6, label='Unit Circle (||v|| = 1)')
axes[0].scatter(0, 0, color='white', zorder=5)

# Plot Eigenvectors in Original Space
colors = ['#FF4B4B', '#00E676']
for i in range(len(eigenvalues)):
    v = eigenvectors[:, i]
    axes[0].quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, 
                   color=colors[i], label=f'Eigenvector v_{i+1}')

axes[0].set_title('Original Domain ($\mathbb{R}^2$)\nUnit Vectors', fontsize=11, fontweight='bold')
axes[0].set_xlim(-2.5, 2.5)
axes[0].set_ylim(-2.5, 2.5)
axes[0].axhline(0, color='gray', linestyle='--', alpha=0.3)
axes[0].axvline(0, color='gray', linestyle='--', alpha=0.3)
axes[0].set_aspect('equal')
axes[0].legend(loc='upper left', fontsize=9)
axes[0].grid(True, linestyle=':', alpha=0.2)

# Subplot 2: Transformed Domain (A * v)
axes[1].plot(transformed_circle[0, :], transformed_circle[1, :], color='cyan', alpha=0.6, label='Transformed Ellipse (A * v)')
axes[1].scatter(0, 0, color='white', zorder=5)

# Plot Transformed Eigenvectors: A * v_i = lambda_i * v_i
for i in range(len(eigenvalues)):
    v_transformed = A @ eigenvectors[:, i]
    lam = eigenvalues[i]
    axes[1].quiver(0, 0, v_transformed[0], v_transformed[1], angles='xy', scale_units='xy', scale=1, 
                   color=colors[i], label=f'$A v_{i+1} = \lambda_{i+1} v_{i+1}$ ($\lambda$={lam:.2f})')

axes[1].set_title('Transformed Domain ($A \cdot \mathbb{R}^2$)\nSheared Ellipse & Scaled Eigenvectors', fontsize=11, fontweight='bold')
axes[1].set_xlim(-2.5, 2.5)
axes[1].set_ylim(-2.5, 2.5)
axes[1].axhline(0, color='gray', linestyle='--', alpha=0.3)
axes[1].axvline(0, color='gray', linestyle='--', alpha=0.3)
axes[1].set_aspect('equal')
axes[1].legend(loc='upper left', fontsize=9)
axes[1].grid(True, linestyle=':', alpha=0.2)

# --- 3. Robust Directory Handling & Save ---
script_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(script_dir, 'assets')
os.makedirs(assets_dir, exist_ok=True)

plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'eigen_transformations_output.png'), dpi=300)
plt.show()