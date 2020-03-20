import sys

# zad 1

zdanie = "Byl tam kiedys taki Pawel"
print(zdanie.count(" "))

# zad 2

x = sys.stdin.readline()
y = sys.stdin.readline()
wynik = int(x)*int(y)
sys.stdout.write(str(wynik)+"\n")

# zad 3

# <
# <=
# >
# >=
# ==
# !=

# zad 4

liczba = input("Podaj liczbe: ")
liczba = int(liczba)
if liczba < 0:
    print(-liczba)
else:
    print(liczba)

# zad 5

a = input("Podaj liczbe a: ")
b = input("Podaj liczbe b: ")
c = input("Podaj liczbe c: ")
a = int(a)
b = int(b)
c = int(c)
if ((int(a) int range(1,11)) and (a>b or b>c)):
    print("Tak")
else:
    print("Nie")

# zad 6

for liczba in range(2000):
    if (liczba%5==0):
        print(liczba)

# zad 7

for liczba in range(2000):
    if (liczba!=0):
        print(liczba*liczba)

# zad 9

a = input("Podaj liczbe wielocyfrowa: ")
a = int(a)
suma = 0
while (a>0):
    suma += int(a%10)
    a=a/10
print (suma)

# zad 10

n=input("Podaj wysokosc wiezy: ")
n=int(n)
for i in range(n+1):
    for j in range(i):
        sys.stdout.write("A")
    print()

# zad 11



# zad 12

for x in range(1,11):
    for y in range(1,11):
        print(str(x)+ "*" + str(y) + " = " + str(x*y)+ "\n")
    