# bonus_string_03.py
#
# Ten sam efekt jak w oryginalnym przykładzie będzie miało dodanie ręcznie wpisanego
# łańcucha znaków do zmiennej przechowującej łańcuch.
# Najważniejsze, żeby łączyć zmienne tego samego typu - a przede wszystkim nie próbować
# łączyć tekstu i liczb.
# Wokół symbolu dodawania można wstawić spacje, co poprawi czytelność kodu. Nie jest to
# jednak obowiązkowe.

text1 = 'hello, '
text2 = 'world!'
full_text = 'hello, ' + text2
print(full_text)

# Docelowy łańcuch do wyprintowania można też "zbudować" bezpośrednio w momencie
# wywoływania funkcji, która przyjmuje łańcuch jako argument.
text3 = 'hello'
text4 = 'world'
print(text3 + ', ' + text4 + '!')

# Metoda print() może przyjmować zarówno łańcuchy znaków jak i liczby. Można także podać
# metodzie kilka argumentów, nawet różnego typu, po przecinku i wszystkie zostaną
# wyświetlone (będą oddzielone spacją).
# Argumenty, które podajemy funkcji (w nawiasie) muszą być oddzielone przecinkami,
# natomiast spacje nie mają znaczenia - poprawiają jednak czytelność kodu.
text1 = 'Ala ma'
text2 = 'koty.'
num1 = 2
print(text1, num1, text2)

# bonus_string_04.py
#
# Poza dodawaniem, łańcuchy można także... mnożyć.

text1 = 'hello, '
print(text1 * 5)

# bonus_int_01.py
# Na zmiennych liczbowych możemy oczywiście także wykonywać inne działania.

num1 = 10
num2 = 4

print("Wynik dodawania liczb",num1,"i",num2,"to", num1 + num2)
print("Wynik odejmowania",num1,"od",num2,"to", num1 - num2)
print("Wynik mnożenia liczb",num1,"i",num2,"to", num1 * num2)
print("Wynik dzielenia zmiennoprzecinkowego",num1,"przez",num2,"to", num1 / num2)
print("Wynik dzielenia całkowitego",num1,"przez",num2,"to", num1 // num2)
print("Reszta z dzielenia",num1,"przez",num2,"to", num1 % num2)

# bonus_int_02.py
#
# Więcej na temat domyślnych wyjątków w Pythonie:
# https://docs.python.org/3/library/exceptions.html#concrete-exceptions
# (będziemy jeszcze do tego wracać)

# bouns_conv_01.py
#
# Metoda str() przydaje się często, kiedy chcemy zbudować łańcuch
# znaków zawierający liczbę.

text1 = 'Ala ma'
text2 = 'koty.'
num1 = 2
full_text = text1 + str(num1) + text2
print(full_text)


# bonus_if_01.py
#
# Instrukcje warunkowe mogą być zagnieżdżone w sobie nawzajem.
# To znaczy, że w bloku pod jedną instrukcją "if" może znajdować
# się kolejna instrukcja "if" i tak dalej.
# Należy pamiętać, że każdy taki blok powinien być zaznaczony
# wcięciem.

num1 = 15

if num1 > 10:
    print('wieksza niż 10')
    if num1 < 20:
        print('mniejsza niż 20')
    else:
        print('wieksza lub równa 20')
# bonus_input_01.py
#
# Inne przykłady operatorów porównania w Pythonie:
num1 = int(input('Podaj liczbe:'))

if num1 == 5:
    print('liczba jest rowna 5')
if num1 != 5:
    print('liczba nie jest rowna 5')
if num1 > 5:
    print('liczba jest wieksza niz 5')
if num1 >= 5:
    print('liczba jest wieksza lub rowna 5')
if num1 < 5:
    print('liczba jest mniejsza niz 5')
if num1 <= 5:
    print('liczba jest mniejsza lub rowna 5')

# W instrukcjach warunkowych można też stosować operatory logiczne:

# Operator "and": obydwa warunki muszą być spełnione:
if num1 > 5 and num1 < 10:
    print('liczba jest wieksza niz 5, ale mniejsza niz 10')
else:
    print('liczba jest mniejsza niz 5, rowna 5, wieksza niz 10 lub rowna 10')

# Operator "or": przynajmniej jeden warunek musi być spełniony:
if num1 > 5 or num1 == 5:
    print('liczba jest wieksza lub rowna 5')
else:
    print('liczba jest mniejsza lub wieksza niz 5')

# Operator "not" pozwala na "odwrócenie" instrukcji - zmienia
# prawdę w fałsz lub fałsz w prawdę:
if not(num1 > 5 and num1 < 10):
    print('liczba jest mniejsza niz 5, rowna 5, wieksza niz 10 lub rowna 10')
else:
    print('liczba jest wieksza niz 5, ale mniejsza niz 10')