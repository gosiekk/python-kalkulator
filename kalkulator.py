print("kalkulator")

a = int(input("podaj a"))
b = int(input("podaj b"))

c = int(input("1:dodawanie, 2:odejmowanie, 3:mnozenie, 4:dzielenie"))

wynik = 0

if c == 1:
    wynik = a + b

if c == 2:
    wynik = a - b

if c == 3:
    wynik = a * b

if c == 4:
    wynik = a / b
        
print("wynik operacji:", wynik)