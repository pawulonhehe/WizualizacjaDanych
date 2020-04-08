# zadanie 10

def pakupki(** rodzaj):
    suma = 0

    for x in rodzaj:
        suma += rodzaj[x]
    print(suma)

pakupki(baton=2, woda=3, banan=1)