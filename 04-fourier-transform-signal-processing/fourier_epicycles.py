import os
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Generate Parametric 2D Shape (Cardioid / Heart Shape) ---
N = 500
t = np.linspace(0, 2 * np.pi, N, endpoint=False)

# Parametric equations for a Cardioid
x = 16 * (np.sin(t) ** 3)
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# Express 2D spatial coordinates as Complex Numbers: z(t) = x(t) + i*y(t)
z = x + 1j * y

# --- 2. Compute Complex Fourier Coefficients (Discrete Fourier Transform) ---
# Each Fourier coefficient represents the amplitude, phase, and frequency of a rotating circle
cn = np.fft.fft(z) / N
freqs = np.fft.fftfreq(N)

# Sort coefficients by harmonic magnitude (keep dominant epicycles)
num_harmonics = 15  # Reconstruct using top 15 harmonics
sorted_indices = np.argsort(np.abs(cn))[::-1][:num_harmonics]

# --- 3. Reconstruct 2D Curve via Fourier Series Summation ---
z_reconstructed = np.zeros(N, dtype=complex)
for idx in sorted_indices:
    k = freqs[idx] * N
    z_reconstructed += cn[idx] * np.exp(1j * 2 * np.pi * k * t / N)

# --- 4. Professional Visualization ---
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(8, 8))

# Plot original continuous geometry
ax.plot(x, y, color='cyan', linestyle='--', linewidth=1.5, alpha=0.6, label='Original Parametric Curve')

# Plot Fourier reconstructed curve
ax.plot(z_reconstructed.real, z_reconstructed.imag, color='lime', linewidth=2.5, 
        label=f'Reconstructed Curve ({num_harmonics} Harmonics)')

# Plot center origin and key sample points
ax.scatter([0], [0], color='red', marker='+', s=100, label='Center (DC Component)')

ax.set_aspect('equal', 'box')
ax.set_title('2D Curve Reconstruction via Complex Fourier Series', fontsize=12, fontweight='bold')
ax.set_xlabel('Re(z) - X Coordinate')
ax.set_ylabel('Im(z) - Y Coordinate')
ax.legend(loc='lower right')
ax.grid(True, linestyle='--', alpha=0.3)

# --- 5. Robust Directory Handling & Save ---
# Dynamically locate the script's directory and save to module's assets/
script_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(script_dir, 'assets')
os.makedirs(assets_dir, exist_ok=True)

plt.tight_layout()
plt.savefig(os.path.join(assets_dir, 'fourier_epicycles_output.png'), dpi=300)
plt.show()