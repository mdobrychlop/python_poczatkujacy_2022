# double_for_loop_01.py
#
# Kiedy iterujemy pętlą for po liście mniejszych sekwencji, to możemy bezpośrednio
# korzystać z elementów tych podrzędnych sekwencji, podając pętli for więcej niż
# jedną zmienną tuż po słowie kluczowym for.

people = [['Mary', 33], ['John', 25], ['Anna', 56]]

for p in people:
    print(a)

for a, b in people:
    print('name:', a, ', age:', b)


# dictionary_01
#
# Słownik jest bardzo przydatnym typem danych, który pozwala nam uporządkować
# dane w parach klucz:wartość. Klucze w słowniku muszą być unikalne, wartości
# niekoniecznie.

people = {'Mary':33, 'John':25, 'Anna':56}

print(people['John'])

for key in people:
    print(key, people[key])

people['Paul'] = 45

print('Po dodaniu Paula:')

for key in people:
    print(key, people[key])


# dictionary_02.py
#
# Słownik jest bardzo przydatnym typem danych, który pozwala nam uporządkować
# dane w parach klucz:wartość. Klucze w słowniku muszą być unikalne, wartości
# niekoniecznie.

sequence = 'GGCCCCAUCGUCUAGCGGUUAGGACG'

comp_dict = {'A':'U', 'G':'C', 'U':'A', 'C':'G'}

comp_sequence = ''

for s in sequence:
    comp_sequence += comp_dict[s]

print(sequence)
print(comp_sequence)


# reading_xlsx_01a.py
#
# Pandas to biblioteka służąca do analizy danych, pozwalająca na przetwarzanie
# danych w strukturach zwanych Data Frames. 
# W Pythonie część funkcji nie jest domyślnie dostępna do wykorzystania w kodzie
# - czasami, żeby wykorzystać funkcję, należy ją zaimportować (lub importować
# cały moduł, którego jest częścią). Służy do tego instrukcja import.
# Wiele modułów dostępnych do zaimportowania jest instalowana razem z Pythonem
# w systemie. Niektóre moduły, takie jak (obecnie) pandas, wymagają dodatkowej
# instalacji.

import pandas

df = pandas.read_excel('fertilisation.xlsx', 'f_data')  # Data Frame

print(df)


# reading_xlsx_01b.py
#
# Pandas to biblioteka służąca do analizy danych, pozwalająca na przetwarzanie
# danych w strukturach zwanych Data Frames. 
# W Pythonie część funkcji nie jest domyślnie dostępna do wykorzystania w kodzie
# - czasami, żeby wykorzystać funkcję, należy ją zaimportować (lub importować
# cały moduł, którego jest częścią). Służy do tego instrukcja import.
# Wiele modułów dostępnych do zaimportowania jest instalowana razem z Pythonem
# w systemie. Niektóre moduły, takie jak (obecnie) pandas, wymagają dodatkowej
# instalacji.
 
import pandas as pd

df = pd.read_excel('fertilisation.xlsx', 'f_data')

print(df)


# reading_xlsx_01c.py
#
# Pandas to biblioteka służąca do analizy danych, pozwalająca na przetwarzanie
# danych w strukturach zwanych Data Frames. 
# W Pythonie część funkcji nie jest domyślnie dostępna do wykorzystania w kodzie
# - czasami, żeby wykorzystać funkcję, należy ją zaimportować (lub importować
# cały moduł, którego jest częścią). Służy do tego instrukcja import.
# Wiele modułów dostępnych do zaimportowania jest instalowana razem z Pythonem
# w systemie. Niektóre moduły, takie jak (obecnie) pandas, wymagają dodatkowej
# instalacji.

from pandas import read_excel

df = read_excel('fertilisation.xlsx', 'f_data')

print(df)


# reading_csv_01.py
#
# Pandas to biblioteka służąca do analizy danych, pozwalająca na przetwarzanie
# danych w strukturach zwanych Data Frames. 
# W Pythonie część funkcji nie jest domyślnie dostępna do wykorzystania w kodzie
# - czasami, żeby wykorzystać funkcję, należy ją zaimportować (lub importować
# cały moduł, którego jest częścią). Służy do tego instrukcja import.
# Wiele modułów dostępnych do zaimportowania jest instalowana razem z Pythonem
# w systemie. Niektóre moduły, takie jak (obecnie) pandas, wymagają dodatkowej
# instalacji.

import pandas

# DLA OSOB PRACUJACYCH NA PLIKACH XLSX:
# df = pandas.read_excel('fertilisation.xlsx', 'f_data')

# DLA OSOB PRACUJACYCH NA PLIKACH CSV:
df = pandas.read_csv('fertilisationcsv.csv', sep=';')


# iterating_data_frame_01.py
#
# Po wierszach struktury Data Frame można iterować, podobnie jak po liście.
# Do konkretnych kolumn każdego wiersza odnosimy się z kolei podobnie jak do kluczy
# w słowniku.

import pandas

df = pandas.read_excel('fertilisation.xlsx', 'f_data')
# df = pandas.read_csv('fertilisationcsv.csv', sep=';')

for index, row in df.iterrows():
    print(row['eggs'])


# iterating_data_frame_02.py
#
# Po wierszach struktury Data Frame można iterować, podobnie jak po liście.
# Do konkretnych kolumn każdego wiersza odnosimy się z kolei podobnie jak do kluczy
# w słowniku.

import pandas

df = pandas.read_excel('fertilisation.xlsx', 'f_data')
# df = pandas.read_csv('fertilisationcsv.csv', sep=';')

for index, row in df.iterrows():
    eggs_value = row['eggs']
    if eggs_value > 20.0:
        print(eggs_value)

# iterating_data_frame_03.py
#
# Po wierszach struktury Data Frame można iterować, podobnie jak po liście.
# Do konkretnych kolumn każdego wiersza odnosimy się z kolei podobnie jak do kluczy
# w słowniku.

import pandas

df = pandas.read_excel('fertilisation.xlsx', 'f_data')
# df = pandas.read_csv('fertilisationcsv.csv', sep=';')

for index, row in df.iterrows():
     if row['group'] == 2:
        print(row['eggs'])

# iterating_data_frame_04.py
#
# Po wierszach struktury Data Frame można iterować, podobnie jak po liście.
# Do konkretnych kolumn każdego wiersza odnosimy się z kolei podobnie jak do kluczy
# w słowniku.

import pandas

df = pandas.read_excel('fertilisation.xlsx', 'f_data')
# df = pandas.read_csv('fertilisationcsv.csv', sep=';')

group_sum = 0.0
group_count = 0

for index, row in df.iterrows():
     if row['group'] == 2:
        group_sum += row['eggs']
        group_count += 1

group_mean = group_sum / group_count

print(group_mean)


# iterating_data_frame_05.py
#
# Pandas udostępnia wiele wbudowanych funkcji, umożliwiających na szybkie obliczenia i inne
# operacje na danych. 
# Funkcja groupby() pozwala nam grupować wartości kolumn na podstawie wartości jednej 
# z nich.
# Funkcja mean() liczy średnią wszystkich elementów danej grupy.
 
import pandas

df = pandas.read_excel('fertilisation.xlsx', 'f_data')
# df = pandas.read_csv('fertilisationcsv.csv', sep=';')

print(df.groupby(['group']).mean())


# iterating_data_frame_06.py
#
# Możemy zawęzić działanie funkcji groupby() do jednej kolumny.


import pandas

df = pandas.read_excel('fertilisation.xlsx', 'f_data')
# df = pandas.read_csv('fertilisationcsv.csv', sep=';')

print(df.groupby(['group'])['eggs'].mean())
