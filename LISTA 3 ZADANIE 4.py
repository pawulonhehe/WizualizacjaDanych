# zadanie 4
import math

def sprawdzanie(a,b,x):
    y = a * x + b
    if (a > 0):
        print("Funkcja jest rosnaca")
    elif (a==0):
        print("Funkcja jest stala")
    else:
        print("Funkcja jest malejaca")

print(sprawdzanie(3,1,2))