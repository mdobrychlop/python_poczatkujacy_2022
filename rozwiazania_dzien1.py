# Zadanie 1: sprawdzanie, czy liczba jest parzysta
x = int(input('Podaj liczbe:'))

if x % 2 == 0:
    print('Liczba jest parzysta')
else:
    print('Liczba jest nieparzysta')


# Zadanie 2: suma liczb n-1 i n+1
x = int(input('Podaj liczbe:'))

print((x-1) + (x+1))



# Zadanie 3: kalkulator
a = int(input('Podaj pierwszą liczbę:'))
b = int(input('Podaj drugą liczbę:'))
znak = input('Podaj znak działania (+, -, * lub /):')

if znak == "+":
    print(a + b)
if znak == "-":
    print(a - b)
if znak == "*":
    print(a * b)
if znak == "/":
    print(a / b)
else:
    print('Nieprawidlowy znak!')


# Zadanie 4: sortowanie trzech liczb
a = input("Podaj pierwszą liczbę: ")
b = input("Podaj drugą liczbę: ")
c = input("Podaj trzecią liczbę: ")

if a <= b and a <= c:
    if b <= c:
        print(a, b, c)
    else:
        print(a, c, b)
elif b <= a and b <= c:
    if a <= c:
        print(b, a, c)
    else:
        print(b, c, a)
else:
    if a <= b:
        print(c, a, b)
    else:
        print(c, b, a)

