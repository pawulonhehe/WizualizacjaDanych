import numpy as np

def zeze(n):
    a=np.diag([n for n in range(n, 0, -1)])
    return a
print(zeze(6))