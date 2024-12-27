import numpy as np
import matplotlib.pyplot as plt
from rtlsdr import RtlSdr
from scipy.signal import butter, lfilter
import sounddevice as sd

# Configuration
sample_rate = 2.048e6  # Sample rate of RTL-SDR
center_freq = 94.5e6  # Center frequency to tune (in Hz)
duration = 1         # Duration of the sample in seconds
audio_sample_rate = 44100  # Audio playback sample rate

# Initialize RTL-SDR
sdr = RtlSdr()

# Configure RTL-SDR
sdr.sample_rate = sample_rate
sdr.center_freq = center_freq
sdr.gain = 'auto'

# Read samples
print("Reading samples...")
sdr.read_samples(2048)
samples = sdr.read_samples(duration * sample_rate)
sdr.close()

# FM Demodulation
# Calculate the instantaneous phase
phase = np.angle(samples)

# Calculate the difference in phase
phase_diff = np.diff(phase)

# Unwrap phase difference to avoid discontinuities
phase_diff = np.unwrap(phase_diff)

# Convert phase difference to instantaneous frequency (Hz)
instantaneous_frequency = np.concatenate(([0], phase_diff)) * (sample_rate / (2 * np.pi))

# To get the audio signal, we need to low-pass filter the instantaneous frequency
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

# Set parameters for low-pass filter
cutoff_freq = 5e3  # Cutoff frequency in Hz for audio
audio_signal = lowpass_filter(instantaneous_frequency, cutoff_freq, sample_rate)

# Normalize audio signal for playback
audio_signal = audio_signal / np.max(np.abs(audio_signal))  # Normalize to -1 to 1

# Resample the audio signal to the desired playback rate
def resample_audio(signal, original_rate, target_rate):
    number_of_samples = int(len(signal) * target_rate / original_rate)
    resampled_signal = np.interp(
        np.linspace(0.0, 1.0, number_of_samples),
        np.linspace(0.0, 1.0, len(signal)),
        signal
    )
    return resampled_signal

# Resample audio signal for playback
audio_signal_resampled = resample_audio(audio_signal, sample_rate, audio_sample_rate)

# Play the audio signal
print("Playing audio...")
sd.play(audio_signal_resampled, samplerate=audio_sample_rate)  # Play the audio at 44.1 kHz
sd.wait()  # Wait until audio is finished playing

# Plot the audio signal
plt.figure(figsize=(10, 6))
plt.plot(audio_signal_resampled, color='blue')
plt.title('Demodulated FM Audio Signal')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.grid()
plt.show()
