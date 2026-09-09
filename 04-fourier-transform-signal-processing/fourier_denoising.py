import numpy as np
import matplotlib.pyplot as plt

# Set seed for reproducibility
np.random.seed(42)

# --- 1. Signal Generation ---
dt = 0.001  # Time step (sampling rate = 1000 Hz)
t = np.arange(0, 1, dt)

# Composite signal: Sum of two sine waves (50 Hz and 120 Hz)
freq1, freq2 = 50, 120
clean_signal = np.sin(2 * np.pi * freq1 * t) + np.sin(2 * np.pi * freq2 * t)

# Add Gaussian white noise
noise = 2.5 * np.random.randn(len(t))
noisy_signal = clean_signal + noise

# --- 2. Fourier Transform (FFT) ---
n = len(t)
fhat = np.fft.fft(noisy_signal, n)                     # Compute FFT
PSD = fhat * np.conj(fhat) / n                         # Power Spectral Density
freq = (1 / (dt * n)) * np.arange(n)                   # Frequency vector
L = np.arange(1, np.floor(n / 2), dtype=int)          # Positive frequencies only

# --- 3. Denoising / Filtering in Frequency Domain ---
# Filter out frequencies with Power Spectral Density below threshold
indices = PSD > 100
PSD_clean = PSD * indices                              # Zero out low power frequencies
fhat_clean = fhat * indices                            # Zero out small Fourier coefficients

# --- 4. Inverse Fourier Transform (IFFT) ---
# Reconstruct clean signal back in time domain
denoised_signal = np.fft.ifft(fhat_clean)

# --- 5. Professional Visualization ---
plt.style.use('dark_background')
fig, axs = plt.subplots(3, 1, figsize=(10, 8), sharex=False)

# Plot 1: Noisy Signal vs Clean Signal
axs[0].plot(t, noisy_signal, color='c', linewidth=1.5, alpha=0.5, label='Noisy Signal')
axs[0].plot(t, clean_signal, color='k', linewidth=2, label='Clean Signal (Ground Truth)')
axs[0].set_xlim(t[0], t[-1])
axs[0].set_ylabel('Amplitude')
axs[0].set_title('Time Domain: Original & Noisy Signals', fontsize=12, fontweight='bold')
axs[0].legend(loc='upper right')
axs[0].grid(True, linestyle='--', alpha=0.3)

# Plot 2: Power Spectral Density (PSD) & Threshold
axs[1].plot(freq[L], PSD[L], color='r', linewidth=1.5, label='Noisy PSD')
axs[1].plot(freq[L], PSD_clean[L], color='g', linewidth=2, label='Filtered PSD (Dominant Frequencies)')
axs[1].set_xlim(0, 200)
axs[1].set_xlabel('Frequency (Hz)')
axs[1].set_ylabel('Power')
axs[1].set_title('Frequency Domain: Power Spectral Density (FFT)', fontsize=12, fontweight='bold')
axs[1].legend(loc='upper right')
axs[1].grid(True, linestyle='--', alpha=0.3)

# Plot 3: Denoised Signal Reconstruction
axs[2].plot(t, denoised_signal.real, color='lime', linewidth=1.8, label='Denoised Signal (IFFT)')
axs[2].plot(t, clean_signal, color='white', linestyle=':', linewidth=1.5, alpha=0.7, label='Clean Signal')
axs[2].set_xlim(t[0], t[-1])
axs[2].set_xlabel('Time (s)')
axs[2].set_ylabel('Amplitude')
axs[2].set_title('Time Domain: Reconstructed Signal', fontsize=12, fontweight='bold')
axs[2].legend(loc='upper right')
axs[2].grid(True, linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig('fourier_denoising_output.png', dpi=300)
plt.show()