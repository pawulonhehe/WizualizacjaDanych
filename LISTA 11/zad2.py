import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin
fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')
n=20
for clr, mkr, zl, zh in [('r', 'o', 5, 20), ('b', '^', 15, 30), ('g', 'h', 5, 10), ('y', 'D', 5, 10), ('b', 'x', 5, 10)]:
    x=randrange(n, zl, zh)
    y=randrange(n, zl, zh)
    z=randrange(n, zl, zh)
    ax.scatter(x, y, z, c=clr, marker=mkr)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


plt.show()

