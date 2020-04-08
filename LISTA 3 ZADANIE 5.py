# zadanie 5
import math

def spr(a1,b1,a2,b2,x):
    # y = a1*x + b1
    # y = a2*x + b2

    if (a1 == a2):
        print("Proste są równoległe")           
    elif (a1*a2 == -1):
        print("Proste są prostopadłe")
    else:
        print("Nie jest ani prosta ani prostopadła")


print(spr(3,5,3,4,9))