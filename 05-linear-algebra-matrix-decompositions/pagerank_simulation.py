import os
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Construct Web Graph Adjacency & Stochastic Matrix ---
# 4 Web Pages: Page 0, Page 1, Page 2, Page 3
# Outgoing links: 0->1, 0->2 | 1->2 | 2->0 | 3->2
A = np.array([
    [0, 1, 1, 0],  # Outgoing from Page 0
    [0, 0, 1, 0],  # Outgoing from Page 1
    [1, 0, 0, 0],  # Outgoing from Page 2
    [0, 0, 1, 0]   # Outgoing from Page 3
], dtype=float)

# Convert Adjacency Matrix to Column-Stochastic Transition Matrix P
num_pages = A.shape[0]
P = np.zeros((num_pages, num_pages))

for j in range(num_pages):
    row_sum = np.sum(A[j, :])
    if row_sum > 0:
        P[:, j] = A[j, :] / row_sum
    else:
        P[:, j] = 1.0 / num_pages  # Handle dangling nodes

# Apply Damping Factor (d = 0.85) to ensure irreducibility (Google PageRank standard)
d = 0.85
M = d * P + (1 - d) / num_pages * np.ones((num_pages, num_pages))

# --- 2. Power Iteration: Iteratively find Eigenvector for lambda = 1 ---
v = np.ones(num_pages) / num_pages  # Uniform initial rank vector
history = [v.copy()]

for _ in range(20):
    v = M @ v
    v = v / np.sum(v)  # Normalize
    history.append(v.copy())

history = np.array(history)

# --- 3. Professional Visualization Setup ---
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(9, 6))

iterations = np.arange(history.shape[0])
colors = ['#FF4B4B', '#00E676', '#29B6F6', '#AB47BC']
page_labels = ['Page 0 (Hub)', 'Page 1 (Mid)', 'Page 2 (Authority)', 'Page 3 (Source)']

for i in range(num_pages):
    ax.plot(iterations, history[:, i], marker='o', linewidth=2, color=colors[i], label=f'{page_labels[i]}: {history[-1, i]:.1%}')

ax.set_title('PageRank Convergence via Power Iteration\nStationary Distribution ($\lambda = 1$ Eigenvector)', fontsize=11, fontweight='bold')
ax.set_xlabel('Iteration Step', fontsize=10)
ax.set_ylabel('PageRank Probability Score', fontsize=10)
ax.set_xticks(iterations)
ax.grid(True, linestyle=':', alpha=0.3)
ax.legend(loc='center right', fontsize=9)

# --- 4. Robust Directory Handling & Save ---
script_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(script_dir, 'assets')
os.makedirs(assets_dir, exist_ok=True)

plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'pagerank_simulation_output.png'), dpi=300)
plt.show()