import numpy as np
import matplotlib.pyplot as plt

# 1. Lorenz System Differential Equations
def lorenz(x, y, z, sigma=10.0, rho=28.0, beta=8.0/3.0):
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return dx_dt, dy_dt, dz_dt

# 2. Simulation Parameters & Initial Conditions
dt = 0.01
num_steps = 10000

# Initialize arrays to store trajectory points
xs = np.empty(num_steps)
ys = np.empty(num_steps)
zs = np.empty(num_steps)

# Set initial point in 3D space
xs[0], ys[0], zs[0] = (0.0, 1.0, 1.05)

# 3. Numerical Integration via Euler's Method
for i in range(num_steps - 1):
    dx, dy, dz = lorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (dx * dt)
    ys[i + 1] = ys[i] + (dy * dt)
    zs[i + 1] = zs[i] + (dz * dt)

# 4. 3D Trajectory Visualization
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(projection='3d')

# Plot the chaotic attractor path
ax.plot(xs, ys, zs, lw=0.6, color='#8a2be2')

ax.set_title(f'Lorenz Attractor (Chaos Theory)\nSteps = {num_steps:,} | dt = {dt}', fontsize=12)
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig('03-chaos-theory-lorenz-attractor/assets/lorenz_attractor.png', dpi=300)
plt.show()