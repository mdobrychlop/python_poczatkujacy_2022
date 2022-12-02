# string_01.py
#
#-*- coding: utf-8 -*-
#
# Metoda print() pozwala na wyświetlenie tekstu w #  konsoli. Jako argument przyjmuje dowolny obiekt.
# Przed wyświetleniem obiekt zostaje 
# przekonwertowany na łańcuch znaków.

print('hello, world!')

#  string_02.py
#
# Tym razem deklarujemy zmienną text, do której
# przekazujemy łańcuch znaków. Następnie,
# tę zmienną przekazujemy metodzie print().

text = 'hello, world!'
print(text)

#  string_03.py
#
# Na zmiennych możemy wykonywać działania.
# Spróbujmy połączyć dwa krótsze łańcuchy
# w jeden dłuższy.

text1 = 'hello, '
text2 = 'world!'
full_text = text1 + text2
print(full_text)

# string_04.py
#
# Na zmiennych możemy wykonywać działania.
# Spróbujmy połączyć dwa krótsze łańcuchy
# w jeden dłuższy.

text1 = 'hello, '
text2 = 'world!'
print(text1 + text2)

# int_01.py
# Zmienne liczbowe (takie jak integery, czyli
# liczby całkowite) można wykorzystywać w
# działaniach matematycznych

text1 = 'hello, '
text2 = 'world!'
num1 = 13
num2 = 7
print(num1 + num2)

# int_02.py
#
# Spróbujmy dodać lancach znaków do
# liczby całkowitej.

text1 = 'hello, '
text2 = 'world!'
num1 = 13
num2 = 7
print(text1 + num2)

# conv_01.py
#
# Metoda str() konwertuje dane rożnego typu na
# lancach znaków, a metoda int() na liczbę
# całkowitą. Metoda float() konwertuje liczbę
# całkowitą na zmiennoprzecinkowa.

text1 = '3'
num1 = 13
num_to_text = str(num1)
text_to_num = int(text1)
print(text1 + num_to_text)
print(num1 + text_to_num)
print(float(num1))
print(text1, num1, num_to_text, text_to_num)

# if_01.py
#
# Instrukcja warunkowa if (jeżeli warunek jest
# spełniony, to…)

num1 = 15

if num1 > 10:
    print('true!')

print('done.')

# else_01.py
#
# Instrukcja warunkowa if (jeżeli warunek jest
# spełniony, to…) / else (w innym wypadku…)

num1 = 15

if num1 == 10:
    print('true!')
else:
    print('not true!')

print('done.')

# elif_01.py
#
# Instrukcja elif (sprawdź kolejny warunek,
# jeśli ten powyżej nie jest spełniony)

num1 = 15
num2 = 20

if num1 > num2:
    print('pierwsza liczba jest wieksza')
elif num1 == num2:
    print('liczby sa rowne')
else:
    print('druga liczba jest wieksza')

print('done.')

# input_01.py
#
# Metoda input() pozwala na wprowadzenie tekstu
# po uruchomieniu programu. Jako argument
# przyjmuje komunikat dla użytkownika.
num1 = int(input('Podaj pierwsza liczbe:'))
num2 = int(input('Podaj druga liczbe:'))

if num1 > num2:
    print('pierwsza liczba jest wieksza')
elif num1 == num2:
    print('liczby sa rowne')
else:
    print('druga liczba jest wieksza')

print('done.')
