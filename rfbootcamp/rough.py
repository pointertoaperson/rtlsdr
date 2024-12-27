 
import numpy as np 
from scipy.signal import resample
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
#import statistics 
#
def sin_mean(freq,t):
  
   avg = ((-1*(np.cos(2*np.pi*freq*t))+1)/(2*np.pi*freq*t))
   return avg
def cos_mean(freq,t):
   avg = np.sin(2*np.pi*freq*t)/(2*np.pi*freq*t)
   return avg
   
     
def fake_fft(freq,x):
   X =[]
   for k in np.arange(0,freq,1):
      for x_i in x:
         sum+=x_i*np.exp(-1*1j*2*np.pi*k)
      X[k] = sum
   return   X
      
   
def upsample(sample_rate,array):
   
   # Original sample rate in Hz
   #target_sample_rate = 44100     # Target sample rate in Hz

   # Example input data: 1 second of a sine wave at 440 Hz
   t = np.arange(0, 1, 1/sample_rate)
   #original_array = np.sin(2 * np.pi * 440 * t)

      # Calculate the number of samples in the upsampled array
   num_samples = int(len(array) * (44.1e3/ sample_rate))

      # Resample the array to the target sample rate
   resampled_array = resample(array, num_samples)
   return resampled_array

   
  
def phasors(mod):
   # Set up the figure and axis
   fig, ax = plt.subplots(figsize=(8, 8))
   ax.set_xlim(-1.5, 1.5)
   ax.set_ylim(-1.5, 1.5)
   ax.axhline(0, color='black', linewidth=0.5, ls='--')
   ax.axvline(0, color='black', linewidth=0.5, ls='--')
   ax.grid(color='gray', linestyle='--', linewidth=0.5)
   # Initialize phasor line and text for angles
   line1, = ax.plot([], [], color='r', lw=2, label='Phasor (I_c + jQ_c)')
   angle_text1 = ax.text(-1, 0.1, '', fontsize=12, color='r')
   
# Set labels and title
   ax.set_title('Animating Phasor from I_c and Q_c', fontsize=16)
   ax.set_xlabel('Real Part (I_c)', fontsize=14)
   ax.set_ylabel('Imaginary Part (Q_c)', fontsize=14)
   ax.legend()
   ax.set_aspect('equal', adjustable='box')
   def animate(i):
    # Calculate the endpoints of the phasor
    x1 = np.real(mod[i])  # Real part (I_c)
    y1 = np.imag(mod[i])  # Imaginary part (Q_c)

    # Update line data
    line1.set_data([0, x1], [0, y1])

    # Update angle text
    angle_text1.set_text(f'Angle: {np.degrees(np.angle(mod[i])):.1f}°')

    return line1, angle_text1

   
   # Create animation
   ani = FuncAnimation(fig, animate, frames=100, interval=100, blit=True)
   plt.show()



