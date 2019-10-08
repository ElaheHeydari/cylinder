from mpl_toolkits.mplot3d import Axes3D
import mpl_toolkits.mplot3d.art3d as art3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

fig = plt.figure()

def plot_3D_cylinder(radius, height, elevation=0, resolution=100, color='r', x_center=256, y_center=256):
    ax = Axes3D(fig, azim=30, elev=30)
    x = np.linspace(x_center - radius, x_center + radius, resolution)
    z = np.linspace(elevation, elevation + height, resolution)
    X, Z = np.meshgrid(x, z)
    Y = np.sqrt(radius ** 2 - (X - x_center) ** 2) + y_center  # Pythagorean theorem
    ax.plot_surface(X, Y, Z, linewidth=0, color=color)
    ax.plot_surface(X, (2 * y_center - Y), Z, linewidth=0, color=color)
    floor = Circle((x_center, y_center), radius, color=color)
    ax.add_patch(floor)
    art3d.pathpatch_2d_to_3d(floor, z=elevation, zdir="z")
    ceiling = Circle((x_center, y_center), radius, color=color)
    ax.add_patch(ceiling)
    art3d.pathpatch_2d_to_3d(ceiling, z=elevation + height, zdir="z")
    ax.set_xlim([0, 256])
    ax.set_ylim([0, 256])
    ax.set_zlim([0, 256])
    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    ax.set_zlabel('z-axis')
    plt.show()


radius = 20
height = 150
elevation = -5
resolution = 100
color = 'b'
x_center = 128
y_center = 128
plot_3D_cylinder(radius, height, elevation=elevation, resolution=resolution, color=color, x_center=x_center,
                 y_center=y_center)
