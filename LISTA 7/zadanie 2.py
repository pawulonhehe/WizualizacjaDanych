import numpy as np

a=np.arange(9).reshape(3, 3)
z=np.arange(16).reshape(4, 4)
print(a.min(axis=1))
print(a.min(axis=0))
print(z.min(axis=1))
print(z.min(axis=0))