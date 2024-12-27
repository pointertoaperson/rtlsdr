import numpy as np
from matplotlib import pyplot as plt
from rtlsdr import RtlSdr
import time
#import statistics
import sounddevice as sd
import rough

sdr = RtlSdr()
freq_s = 2.048e6
N = 1024 #number of samples
center_freq = 94e6
sdr.sample_rate = freq_s
sdr.center_freq = center_freq
sdr.freq_correction = 60
sdr.gain = 'auto'
sdr.read_samples(2048)
arr = sdr.read_samples(256*1024)
sdr.close()
dtime = (1/freq_s)*N 
t = np.linspace(0,dtime,N)
    #
    #    arr = sdr.read_samples(N)
    #    #haning_arr = arr * np.hanning(N)
    #    mod.append(rough.cos_mean(freq_s/2,dtime)- statistics.mean(np.abs(np.abs(arr))))
    #   ## mod.append = np
    #
    #
    ##sound = rough.upsample(2000,mod)

    #time.sleep(1)
        #
    ##plt.plot(t,mod)


#rough.phasors(arr)
phase = np.angle(arr)
#plt.plot(t,phase)  

freq = np.diff(np.unwrap(phase))

 
mod = freq*freq_s
audio = mod / np.max(mod)


sd.play(audio,44.1e3)
time.sleep(4)
sd.stop()

#plt.plot(t[:-1],mod)
#plt.show()  


#fft_arr = np.fft.fft(arr)
#fft_hanning_r = np.fft.fft(haning_arr)
#shift_arr = np.fft.fftshift(fft_arr)
#
#

#f = np.linspace(-freq_s/2,freq_s/2,len(fft_arr))
#print(statistics.mean(np.abs(haning_arr)))
#print(rough.cos_mean(0.0000001,0.006))#+ rough.sin_mean(freq_s/2,time))
##print("length of f"+ str(len(f)))
##print("length of fft" + str(len(fft_arr)))
#
#
#fig,axs = plt.subplots(2)
##axs[0].title('time domain')
##axs[0].plot(t,arr)
###axs[1].title('fft')
##axs[1].plot(f,fft_arr)
##axs[0].plot(f, (fft_arr))
##axs[1].plot(f,(fft_hanning_r))
##axs[0].plot(t,arr)
#a = np.zeros((N,1))
#print(a)
#axs[0].plot(t,a)
#axs[1].plot(f,np.fft.fft(a*np.hanning(N)))
#
#
#
#plt.show()
