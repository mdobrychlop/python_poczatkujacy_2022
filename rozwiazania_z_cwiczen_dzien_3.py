# cwiczenie_02.py
# Dokończ kod poniżej. Kod ma wykorzystywać pętlę for tak, żeby dane z listy people
# znalazły się w słowniku out_dictionary. 
# Następnie zaimplementuj pętlę while, która przyjmie od użytkownika dwa kolejne
# imiona i dwie kolejne liczby i doda te dane do słownika (pierwsze imię : pierwsza liczba,
# drugie imię : druga liczba). Wprowadź zabezpieczenie, uniemożliwiające wprowadzenie liczby
# większej niż 150 (niech program pyta o liczbę aż nie dostanie mniejszej lub równej 150).
# Na końcu wypisz słownik.


people = [['Mary', 33], ['John', 25], ['Anna', 56]]

out_dictionary = {}

for a, b in people:
   out_dictionary[a] = b  

imie1 = input("Wprowadz pierwsze imie: ")

wiek1 = 151

while wiek1 > 150:
	liczba = int(input("Wprowadz pierwsza liczbe: "))
	wiek1 = liczba

imie2 = input("Wprowadz drugie imie: ")

wiek2 = 151

while wiek2 > 150:
	liczba = int(input("Wprowadz druga liczbe: "))
	wiek2 = liczba

out_dictionary[imie1] = wiek1
out_dictionary[imie2] = wiek2

print(out_dictionary)

# cwiczenie_02.py
# Wykorzystując pakiet pandas, odczytaj plik 'coronavirus_cases_13-03-2020.xlsx' (lub
# 'coronavirus_cases_13-03-2020.csv'). Oblicz i wypisz na ekranie:
# - średni wiek zarażonych obywateli Chin
# - średni wiek zarażonych obywateli Chin pochodzących z Wuhan (kolumna R - from Wuhan)
# - liczbę zarażonych kobiet z Japonii
# - liczbę zarażonych mężczyzn z Japonii

import pandas

df = pandas.read_excel('coronavirus_cases_13-03-2020.xlsx', 'Line-list')
# df = pandas.read_csv('coronavirus_cases_13-03-2020.csv', sep=';')

chiny_wiek_suma = 0
chiny_licznik = 0
chiny_wuhan_wiek_suma = 0
chiny_wuhan_licznik = 0

kobiety_japonia = 0
mezczyzni_japonia = 0


for index ,row in df.iterrows():
	if row['country'] == 'China':
		chiny_wiek_suma += row['age']
		chiny_licznik += 1
		if row['from Wuhan'] == 1:
			chiny_wuhan_wiek_suma += row['age']
			chiny_wuhan_licznik += 1
	elif row['country'] == 'Japan':
		if row['gender'] == 'male':
			mezczyzni_japonia += 1
		elif row['gender'] == 'female':
			kobiety_japonia += 1

print('średni wiek zarażonych obywateli Chin: ', chiny_wiek_suma / chiny_licznik)
print('średni wiek zarażonych obywateli Chin pochodzących z Wuhan: ', chiny_wuhan_wiek_suma / chiny_wuhan_licznik)
print('liczba zarażonych kobiet z Japonii: ', kobiety_japonia)
print('liczba zarażonych mężczyzn z Japonii: ', mezczyzni_japonia)

