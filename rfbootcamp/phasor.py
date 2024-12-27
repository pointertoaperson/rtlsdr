import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Frequency definition
f = 1  # Frequency of the sine and cosine waves

# Time vector
t = np.linspace(0, 1, 100)  # 100 points between 0 and 1 seconds
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

# Prepare the I_c and Q_c data
I_c = np.cos(2 * np.pi * f * t)  # In-phase component
Q_c = np.sin(2 * np.pi * f * t)   # Quadrature component
mod2 = I_c + 1j * Q_c              # Complex representation

# Animation function
def animate(i):
    # Calculate the endpoints of the phasor
    x1 = np.real(mod2[i])  # Real part (I_c)
    y1 = np.imag(mod2[i])  # Imaginary part (Q_c)

    # Update line data
    line1.set_data([0, x1], [0, y1])

    # Update angle text
    angle_text1.set_text(f'Angle: {np.degrees(np.angle(mod2[i])):.1f}°')

    return line1, angle_text1

# Create animation
ani = FuncAnimation(fig, animate, frames=len(t), interval=100, blit=True)

# Show the plot
plt.show()
