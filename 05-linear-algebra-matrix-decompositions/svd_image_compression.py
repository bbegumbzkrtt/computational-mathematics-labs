import os
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Generate High-Rank Synthetic Mathematical Image ---
# Creating a complex spatial interference pattern (high linear independence / full rank)
x = np.linspace(-4, 4, 250)
y = np.linspace(-4, 4, 250)
X, Y = np.meshgrid(x, y)

# Overlaying multiple frequency components and dynamic cross-terms
A = (np.sin(X**2 + Y**2) + 
     0.5 * np.cos(3 * X) * np.sin(3 * Y) + 
     0.3 * np.exp(-0.2 * (X**2 + Y**2)) * np.cos(5 * X * Y))

# --- 2. Singular Value Decomposition (SVD): A = U * Sigma * V^T ---
U, S, Vt = np.linalg.svd(A, full_matrices=False)

# Select truncation ranks (k) for distinct visual reconstruction levels
k_values = [2, 8, 25]

# --- 3. Professional Visualization Setup ---
plt.style.use('dark_background')
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

# Original Full-Rank Matrix
axes[0, 0].imshow(A, cmap='magma')
axes[0, 0].set_title(f'Original Matrix A\n(Rank = {min(A.shape)})', fontsize=11, fontweight='bold')
axes[0, 0].axis('off')

# Rank-k Low-Rank Approximations
for idx, k in enumerate(k_values):
    row, col = (idx + 1) // 2, (idx + 1) % 2
    
    # Reconstruct rank-k approximation: A_k = sum_{i=1}^k (sigma_i * u_i * v_i^T)
    A_k = U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]
    
    # Calculate Relative Frobenius Norm Error
    error = np.linalg.norm(A - A_k) / np.linalg.norm(A)
    
    axes[row, col].imshow(A_k, cmap='magma')
    axes[row, col].set_title(f'Rank-{k} Approximation\nRelative Error: {error:.2%}', fontsize=11, fontweight='bold')
    axes[row, col].axis('off')

# --- 4. Robust Directory Handling & Save ---
script_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(script_dir, 'assets')
os.makedirs(assets_dir, exist_ok=True)

plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'svd_compression_output.png'), dpi=300)
plt.show()
