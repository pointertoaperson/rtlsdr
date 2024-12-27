import argparse
import traceback

from scripts.SdrInit import SdrInit
from dsp.sdr_fft import fft,freq_axis
from matplotlib import pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from rtlsdr import RtlSdr
import numpy as np
from time import sleep


def sine(shift=False):
    t = np.linspace(0,1,1024)
    data =  np.sin(2*np.pi*1e6*t)
    psd,phase= fft(data,shift=False,psd=True)
    freqs = freq_axis(1024,2.048e6)
    figure, axis = plt.subplots(2,1)
    axis[0].stem(psd)
    axis[1].stem(phase)
    axis[0].xaxis.set_major_formatter(FormatStrFormatter('%2.2f'))
    axis[0].xaxis.set_ticks(freqs)
    axis[1].xaxis.set_major_formatter(FormatStrFormatter('%2.2f'))
    axis[1].xaxis.set_ticks(freqs)
    plt.show()


def sdr_run(
    no_of_read_samples,
    sample_rate = 2.048e6,
    center_freq = 100e6,
    freq_correction=60,
    gain = 'auto',
    shift=True):

    sdr = RtlSdr()
    sdr.sample_rate = sample_rate
    sdr.center_freq = center_freq
    sdr.freq_correction = freq_correction
    sdr.gain = gain

    try :
        sdr.read_samples(2048)
        read_data = sdr.read_samples(no_of_read_samples)
        print(read_data[0:10])
        psd,phase = fft(read_data, shift=shift,psd=True)
        freq_axes_values =  freq_axis(no_of_read_samples,sdr.sample_rate,shift=shift)
        print (len(psd),len(freq_axes_values))
        print(min(freq_axes_values), max(freq_axes_values))

        figure, axis = plt.subplots(2,1)
        axis[0].plot(freq_axes_values,10*np.log10(psd))
        axis[1].plot(freq_axes_values, phase)
        #axis[0].set_yscale("log")
        #axis[0].set_xscale("log")
        #axis[1].set_yscale("log")
        #axis[1].set_xscale("log")
        plt.show()
        sdr.close()
    except Exception:
        sdr.close()
        print(traceback.format_exc())

#freq_try()
#sine()
sdr_run(1024,
        sample_rate=2.4e6, #36.125MHZ, 4.57MHZ, 0IF28.8MHZ, tume 25mhz-1766Mhz, Fiti power 22-1100/9486
        center_freq=92.5e6,
        freq_correction=100,
        shift=True)