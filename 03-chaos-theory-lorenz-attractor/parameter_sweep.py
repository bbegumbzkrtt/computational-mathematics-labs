import numpy as np
import matplotlib.pyplot as plt

def lorenz(x, y, z, sigma=10.0, rho=28.0, beta=8.0/3.0):
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return dx_dt, dy_dt, dz_dt

def simulate(rho_value, dt=0.001, num_steps=30000):
    xs = np.empty(num_steps)
    ys = np.empty(num_steps)
    zs = np.empty(num_steps)
    xs[0], ys[0], zs[0] = (0.0, 1.0, 1.05)
    
    for i in range(num_steps - 1):
        dx, dy, dz = lorenz(xs[i], ys[i], zs[i], rho=rho_value)
        xs[i + 1] = xs[i] + (dx * dt)
        ys[i + 1] = ys[i] + (dy * dt)
        zs[i + 1] = zs[i] + (dz * dt)
        
    return xs, ys, zs

rhos = [14.0, 28.0, 99.96]
titles = [
    r'$\rho = 14.0$ (Convergence to Fixed Point)',
    r'$\rho = 28.0$ (Chaotic Butterfly Attractor)',
    r'$\rho = 99.96$ (Periodic Knot Trajectory)'
]
colors = ['#1f77b4', '#8a2be2', '#2ca02c']

fig = plt.figure(figsize=(16, 5))

for idx, (r, title, color) in enumerate(zip(rhos, titles, colors)):
    xs, ys, zs = simulate(r)
    ax = fig.add_subplot(1, 3, idx + 1, projection='3d')
    ax.plot(xs, ys, zs, lw=0.5, color=color)
    ax.set_title(title, fontsize=10, pad=10)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig('03-chaos-theory-lorenz-attractor/assets/parameter_sweep.png', dpi=300)
plt.show()