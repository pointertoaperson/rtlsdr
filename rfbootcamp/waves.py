import numpy as np
from matplotlib import pyplot as plt
from scipy import signal

def fake_fft(freq, x):
    N = len(x)
    X = np.zeros(freq, dtype=complex)  # Initialize array for FFT results
    
    for k in range(freq):
        sum = 0  # Reset sum for each frequency k
        for n in range(N):
            sum += x[n] * np.exp(-1j * 2 * np.pi * k * n / N)  # Correctly incorporate time index
        X[k] = sum
    return X

# Parameters
N = 100  # Number of samples
freq_s = 10  # Frequency sampling

# Time vector
t = np.linspace(0, 1, N)
sine = np.sin(2 * np.pi * 5 * t)
cosine = np.cos(2 * np.pi * 0.4 * t)
wwave = sine  # Using sine wave as the signal

# Calculate FFT using NumPy
raw_fft = np.fft.fft(wwave)
S = np.fft.fftshift(raw_fft)

# Frequency vector
f = np.fft.fftshift(np.fft.fftfreq(N, d=1/freq_s))

# Plotting
plt.figure(figsize=(12, 8))

# Time domain plot
plt.subplot(3, 1, 1)
plt.title("Wave Time")
plt.plot(t, wwave, label="wwave (Sine Wave)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()

# Magnitude FFT plot
plt.subplot(3, 1, 2)
plt.title("Magnitude FFT")
plt.plot(f, np.abs(S), label="Magnitude of FFT")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.legend()

# Phase plot
plt.subplot(3, 1, 3)
plt.title("Phase Plot")
plt.plot(f, np.angle(S), label="Phase of FFT")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Phase (radians)")
plt.legend()

plt.tight_layout()
plt.show()

# Using the custom FFT
fake_fft_result = fake_fft(freq_s, wwave)
plt.figure()
plt.title("Fake FFT")
plt.plot(np.arange(0, freq_s, 1), np.abs(fake_fft_result), label="Fake FFT Magnitude")
plt.xlabel("Frequency Index")
plt.ylabel("Magnitude")
plt.legend()
plt.grid()
plt.show()
