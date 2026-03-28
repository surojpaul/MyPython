import numpy as np
import matplotlib.pyplot as plt
# Constants
GM = 5.63e26  # Gravitational constant * Mass of Sgr A* in (m^3/s^2)
a = 1.5e14  # Semi-major axis (m)
e = 0.88  # Eccentricity
# Create an array of angles from 0 to 360 degrees
theta = np.linspace(0, 2*np.pi, 100)
# Calculate 'r' using eccentricity and semi-major axis
r = a * (1 - e**2) / (1 + e * np.cos(theta))
# Calculate 'v' using the vis-viva equation for every 'r'
v = np.sqrt(GM * (2/r - 1/a))
# Plotting: How velocity changes with respect to the distance 'r'
plt.plot(r/1000, v/1000) # Distance in km and velocity in km/s
plt.xlabel('Distance from Sgr A* (km)')
plt.ylabel('Orbital Velocity (km/s)')
plt.title(f"Orbital Velocity vs. Distance for a = {a/1000} km, e = {e}")
plt.grid(True)
plt.show()

