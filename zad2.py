print("Kalkulator")

x = int(input("Wpisz pierwsza cyfre"))
y = int(input("Wpisz druga cyfre"))
z = int(input("Typ działania"))

znaki ={"+": x + y,"-": x - y, "*": x * y, "/": x / y}

if z == "+":
    print(znaki)