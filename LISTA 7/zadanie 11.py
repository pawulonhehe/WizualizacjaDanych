import numpy as np

a = np.arange(12).reshape(3, 4)
z = np.arange(12).reshape(4, 3)
y = np.arange(12).reshape(2, 6)

a1=a.ravel()
z1=z.ravel()
y1=y.ravel()

print(a1)
print(z1)
print(y1)