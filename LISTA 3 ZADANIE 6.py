# zadanie 6
import math

def promien(x, y, a=0, b=0):
    r = math.sqrt((x-a) ** 2 + (y-b) ** 2)
    return r

print(promien(3,3))