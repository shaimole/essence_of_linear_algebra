import matplotlib.pyplot as plt
from essence_la.vector import Vector
from essence_la.vector import format_for_quiver

vec1 = Vector([1, 2])
vec2 = Vector([3, -1]).set_origin(vec1.elements)
vec3 = vec1.add(vec2)
positions = format_for_quiver([vec1,vec2])
plt.xlim(-5, 5)
plt.ylim(-5, 5)

plt.quiver(*format_for_quiver([vec1]), scale=1, angles='xy', scale_units='xy')
plt.pause(0.5)
plt.quiver(*format_for_quiver([vec2]), scale=1, angles='xy', scale_units='xy')
plt.pause(0.5)
plt.quiver(*format_for_quiver([vec3]), scale=1, angles='xy', scale_units='xy')

plt.show()