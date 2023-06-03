import numpy as np
import matplotlib.pyplot as plt


C_d = 0.53
r = 0.123
A = np.pi * r**2
rho = 1.293

def calculate_drag_1(v):
    """Calculate the drag force for a given velocity."""
    return 0.5 * C_d * A * rho * v**2


# Create an array of velocities
velocities = np.linspace(0, 30, 100)  # From 0 to 30 m/s

# Calculate the drag force for each velocity
drag_forces_1 = calculate_drag_1(velocities)


# Create the plot
plt.figure(figsize=(6,4))

plt.plot(velocities, drag_forces_1, label='Air drag')
plt.xlabel('Velocity (m/s)')
plt.ylabel('Drag Force (N)')
plt.title('Air Drag on a Basketball')
plt.legend()
plt.grid(True)
plt.show()
