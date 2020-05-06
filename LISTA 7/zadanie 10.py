import numpy as np

a = np.arange(81).reshape(9,9)
print(a)
z=a.ravel()
print(z)
y=a.T #transpozycja
print(y)