import numpy as np
import matplotlib.pyplot as plt

def fft(inp,shift=False, psd=False):
    input_len=len(inp)
    fft = np.fft.fft(inp)
    if shift:
        fft = np.fft.fftshift(fft)
    return (np.abs(fft) if psd else np.real(fft), np.imag(fft))

def freq_axis(N,sample_rate, shift=False):
    """
        the sampling rate contributes to the resolution.
        The frequency bins are the amount of N, with -sr/2 to sr/2
    """
    spacings= (
        np.linspace(0, sample_rate, N) 
        if not shift 
        else np.linspace(-sample_rate/2, sample_rate/2, N)
    )
    return spacings

    