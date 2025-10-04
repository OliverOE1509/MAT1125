import numpy as np
import matplotlib.pyplot as plt

v = np.array([1/np.sqrt(2), 1/np.sqrt(2)])
v2 = np.array([-1/np.sqrt(2), 1/np.sqrt(2)])

fig, ax = plt.subplots()
ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1)
ax.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1)
ax.set_xlim(-1, 2)
ax.set_ylim(-1, 2)
ax.set_aspect('equal', adjustable='box')
plt.grid()
ax.set_label('x')
ax.set_ylabel('y')
plt.title('Vektor i 2D')
plt.show()