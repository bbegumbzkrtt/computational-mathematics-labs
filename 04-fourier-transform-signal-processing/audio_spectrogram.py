import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram

# Set seed for reproducibility
np.random.seed(42)

# --- 1. Signal Generation (Clean Multi-Tone Chirp) ---
fs = 1000                             # Sampling frequency (Hz)
duration = 2.0                        # Duration in seconds
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# Linear chirp sweeping from 20 Hz to 220 Hz
f0, f1 = 20, 220
chirp_signal = np.sin(2 * np.pi * (f0 + (f1 - f0) * (t / (2 * duration))) * t)

# Add a subtle fixed background harmonic at 80 Hz
harmonic = 0.4 * np.sin(2 * np.pi * 80 * t)

# Add low-level white noise (Reduced for crisp visualization)
noise = 0.25 * np.random.randn(len(t))
composite_signal = chirp_signal + harmonic + noise

# --- 2. Short-Time Fourier Transform (STFT) ---
nperseg = 256    # Increased segment length for better frequency resolution
noverlap = 224   # High overlap for smooth resolution
frequencies, times, Sxx = spectrogram(composite_signal, fs=fs, window='hann', 
                                      nperseg=nperseg, noverlap=noverlap)

# --- 3. Crisp & High-Contrast Visualization ---
plt.style.use('dark_background')
fig, axs = plt.subplots(2, 1, figsize=(10, 7), gridspec_kw={'height_ratios': [1, 2]})

# Plot 1: Time Domain Signal
axs[0].plot(t, composite_signal, color='cyan', alpha=0.7, linewidth=0.8, label='Composite Signal')
axs[0].set_xlim(0, duration)
axs[0].set_ylabel('Amplitude')
axs[0].set_title('Time Domain: Chirp Signal with 80 Hz Harmonic', fontsize=12, fontweight='bold')
axs[0].legend(loc='upper right')
axs[0].grid(True, linestyle='--', alpha=0.3)

# Plot 2: High-Contrast Spectrogram
pcm = axs[1].pcolormesh(times, frequencies, 10 * np.log10(Sxx + 1e-10), 
                        shading='gouraud', cmap='viridis', vmin=-40, vmax=0)
axs[1].set_ylim(0, 300)
axs[1].set_xlabel('Time (s)')
axs[1].set_ylabel('Frequency (Hz)')
axs[1].set_title('STFT Spectrogram: Time-Frequency Heatmap', fontsize=12, fontweight='bold')

# Colorbar
cbar = fig.colorbar(pcm, ax=axs[1], orientation='vertical', pad=0.02)
cbar.set_label('Power Spectral Density (dB/Hz)')

plt.tight_layout()
plt.savefig('spectrogram_output.png', dpi=300)
plt.show()