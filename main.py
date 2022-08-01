import matplotlib.pyplot as plt
from essence_la.vector import Vector
from essence_la.vector import format_for_quiver

vec1 = Vector([1, 2])
vec2 = Vector([3, -1])
positions = format_for_quiver([vec1,vec2])
plt.quiver(*positions, scale=1, angles='xy', scale_units='xy')
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.show()