import numpy as np
import matplotlib.pyplot as plt

def lorenz(x, y, z, sigma=10.0, rho=28.0, beta=8.0/3.0):
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z

def run_trajectory(init_cond, dt=0.01, num_steps=3000):
    xs = np.empty(num_steps)
    ys = np.empty(num_steps)
    zs = np.empty(num_steps)
    xs[0], ys[0], zs[0] = init_cond
    
    for i in range(num_steps - 1):
        dx, dy, dz = lorenz(xs[i], ys[i], zs[i])
        xs[i + 1] = xs[i] + dx * dt
        ys[i + 1] = ys[i] + dy * dt
        zs[i + 1] = zs[i] + dz * dt
        
    return xs, ys, zs

dt = 0.01
num_steps = 3000
time = np.linspace(0, num_steps * dt, num_steps)

# Trajectory 1 vs Trajectory 2 (Delta Z = 0.0001)
x1, y1, z1 = run_trajectory((0.0, 1.0, 1.0500), dt, num_steps)
x2, y2, z2 = run_trajectory((0.0, 1.0, 1.0501), dt, num_steps)

# Calculate Euclidean distance over time
distance = np.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)

fig = plt.figure(figsize=(14, 6))

# 3D Trajectory Comparison
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax1.plot(x1, y1, z1, lw=0.6, color='#1f77b4', label=r'State A: $Z_0 = 1.0500$')
ax1.plot(x2, y2, z2, lw=0.6, color='#d62728', label=r'State B: $Z_0 = 1.0501$')
ax1.set_title('Sensitive Dependence on Initial Conditions', fontsize=11)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.legend(loc='upper right')

# Divergence Distance vs Time
ax2 = fig.add_subplot(1, 2, 2)
ax2.plot(time, distance, color='#2ca02c', lw=1.2)
ax2.set_title('Divergence Distance Between Trajectories Over Time', fontsize=11)
ax2.set_xlabel('Time (t)')
ax2.set_ylabel('Euclidean Distance $||A - B||$')
ax2.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('03-chaos-theory-lorenz-attractor/assets/butterfly_effect_sensitivity.png', dpi=300)
plt.show()