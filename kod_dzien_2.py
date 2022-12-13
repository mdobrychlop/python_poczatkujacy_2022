# list_01.py
#
# Lista to typ danych, który pozwala na
# przechowywanie wielu elementów rożnego typu.
# Odwołujemy się do nich za pomocą indeksów.
#
# indeksy:   0     1      2       3       4
animals = ['dog','cat','bird','hamster','bat']

print(animals[0])
print(animals[2])

animals[3] = 'mouse'
print(animals)

# list_02.py
#
# Lista to typ danych, który pozwala na
# przechowywanie wielu elementów rożnego typu.
# Odwołujemy się do nich za pomocą indeksów.
#
# indeksy:   0     1      2       3       4
animals = ['dog','cat','bird','hamster','bat']

print(animals[0])
print(animals[2])

animals[3] = 'mouse'
print(animals)

print('[-1]', animals[-1])
print('[2:5]', animals[2:5])

# list_slicing_01.py
#
# Zasady wykrawania list:
#
# lista[pierwszy_element:ostatni_element+1]
#
# przykład: lista[2:5]:
# - element 2 będzie uwzględniony
# - element 5 nie będzie uwzględniony


# indeks:    0     1     2        3       4     5
animals = ['dog','cat','bird','hamster','bat','cow']
# od końca: -6    -5    -4       -3      -2    -1


print(animals[2:5])  # -> 2, 3, 4 
print(animals[2:])   # -> 2, 3, 4, 
print(animals[1:4])  # -> 1, 2, 3
print(animals[:4])   # -> 0, 1, 2, 3
print(animals[-3:])  # -> 3, 4, 5

# string_index_01.py
#
# Za pomocą indeksów można również odwoływać się
# do kolejnych znaków w łańcuchu znaków.


#       012345
name = 'Janusz'
print(name[2])


# string_index_02.py
#
# Za pomocą indeksów można również odwoływać się
# do kolejnych znaków w łańcuchu znaków.


#       012345
name = 'Janusz'
print(name[2])

animals = ['dog','cat','bird','hamster','bat']
print(animals[2][-1])


# append_01.py
#
# Metoda append() pozwala na dodawanie elementów do listy.
# Metoda remove() pozwala na usuwanie elementów z listy.
# Metoda len() pozwala na sprawdzenie długości listy.


# indeksy:   0     1      2       3       4
animals = ['dog','cat','bird','hamster','bat']

animals.append('cat')
print(animals)

animals.remove('cat') # usuwa pierwszy znaleziony przykład
print(animals)

print(len(animals))


# while_01.py
#
# Pętle to niezwykle istotny aspekt programowania.
# Pętla while pozwala powtarzać pewną instrukcję, dopóki
# zdefiniowany przez nas warunek jest spełniony.


# indeksy:   0     1      2       3       4
animals = ['dog','cat','bird','hamster','bat']

counter = 0
list_length = len(animals)

while counter < list_length:
    print(animals[counter])
    counter += 1  # to znaczy to samo co: counter = counter + 1


# while_02.py
#
# Pętle to niezwykle istotny aspekt programowania.
# Pętla while pozwala powtarzać pewną instrukcję, dopóki
# zdefiniowany przez nas warunek jest spełniony.


# indeksy:   0     1      2       3       4
animals = ['dog','cat','bird','hamster','bat']

counter = 0
list_length = len(animals)

while counter < list_length:
    print(animals[counter])
    # counter += 1  # to znaczy to samo co: counter = counter + 1


# for_01.py
#
# Pętla for pozwala na iterowanie po elementach sekwencji
# - na przykład listy lub łańcucha znaków.


# indeksy:   0     1      2       3       4
animals = ['dog','cat','bird','hamster','bat']

counter = 0
list_length = len(animals)

for a in animals: 
    print(a)
    # counter += 1  # to znaczy to samo co: counter = counter + 1


# file_reading_01.py
#
# Funkcja open() przyjmuje ścieżkę do pliku oraz informację o trybie,
# w jakim plik zostanie otwarty ('r' -> 'read' -> tryb odczytu).
# Tworzy ona tzw. uchwyt do pliku, który pozwala na wykonywanie dalszych
# operacji na jego zawartości.

file = open('trna_sequence.fasta','r')

file_contents = file.read() # Odczyt całej zawartości jako string

print(file_contents)


# file_reading_02a.py
#
# Funkcja readlines() zamiast łańcucha znaków zwraca listę,
# przechowującą wszystkie linie pliku jako oddzielne elementy.

file = open('trna_sequence.fasta','r')

file_lines = file.readlines()

print(file_lines)


# file_reading_02b.py
#
# Możemy wykorzystać pętlę for, aby wyświetlić zawartość
# linia po linii.

file = open('trna_sequence.fasta','r')

file_lines = file.readlines()

for line in file_lines:
    print(line)


# file_reading_03.py
#
# Dzielenie listy linii na mniejsze listy może pozwolić nam na
# szybkie uporządkowanie zawartości, przynajmniej dla niektórych
# formatów plików.

file = open('trna_sequence.fasta','r')

file_lines = file.readlines()

header = file_lines[0]
sequence = file_lines[1:]

print('NAGLOWEK:', header)
print('SEKWENCJA:', sequence)


# file_reading_04.py
#
# Metoda join() pozwala na połączenie łańcuchów zawartych w liście
# w jeden łańcuch. Metoda ta jest metodą łańcucha, a nie listy – 
# w związku z tym składnia stosowania tej metody może wydawać się nietypowa.
# Składnia jest następująca: separator_elementow_listy.join(lista_do_polaczenia).

file = open('trna_sequence.fasta','r')

file_lines = file.readlines()

header = file_lines[0]
sequence = file_lines[1:]
full_sequence = ''.join(sequence)

print('NAGLOWEK:', header)
print('SEKWENCJA:', full_sequence)


# file_reading_05a.py
#
# Metoda replace() pozwala zastąpić wszystkie wystąpienia jakiegoś znaku
# w danym łańcuchu, na inny znak. 

file = open('trna_sequence.fasta','r')

file_lines = file.readlines()

header = file_lines[0]
sequence = file_lines[1:]
sequence[0] = sequence[0].replace('\n','')
full_clean_sequence = ''.join(sequence)

print('NAGLOWEK:', header)
print('SEKWENCJA:', full_clean_sequence)


# file_reading_05b.py
#
# Metoda strip() usuwa z początku i z końca łańcucha białych znaków, takich
# jak spacje, tabulatory czy symbole nowej linii.

file = open('trna_sequence.fasta','r')

file_lines = file.readlines()

header = file_lines[0]
sequence = file_lines[1:]
sequence[0] = sequence[0].strip()
full_clean_sequence = ''.join(sequence)

print('NAGLOWEK:', header)
print('SEKWENCJA:', full_clean_sequence)


# file_reading_06.py
# Funkcja split() pozwala na podzielenie łańcucha w miejscach
# występowania konkretnego znaku. Zwraca listę łańcuchów.

file = open('trna_sequence.fasta','r')

file_lines = file.readlines()

header = file_lines[0]
sequence = file_lines[1:]

header_information = header.split('|')

pdb_id = header_information[0]
chain_id = header_information[1]
molecule_type = header_information[2]
organism = header_information[3]

print(pdb_id)
print(chain_id)
print(molecule_type)
print(organism)


# file_reading_07.py
#
# Funkcja split() pozwala na podzielenie łańcucha w miejscach
# występowania konkretnego znaku. Zwraca listę łańcuchów.

file = open('trna_sequence.fasta','r')

file_lines = file.readlines()

header = file_lines[0]
sequence = file_lines[1:]

header_information = header.split('|')

pdb_id = header_information[0].replace('>','')
chain_id = header_information[1]
molecule_type = header_information[2]
organism = header_information[3]

print(pdb_id)
print(chain_id)
print(molecule_type)
print(organism)


# file_writing_01.py
#
# Podanie metodzie open() argumentu 'w' otworzy nowy plik i pozwoli nam zapisywać
# w nim dane.
# Znak \t oznacza tabulację.

infile = open('trna_sequence.fasta','r')
outfile = open('trna_in_columns.txt','w')

infile_lines = infile.readlines()

header = infile_lines[0]
sequence = infile_lines[1:]

header_information = header.split('|')

pdb_id = header_information[0].replace('>','')
chain_id = header_information[1]
molecule_type = header_information[2]
organism = header_information[3]

outfile.write('PDB ID\tLANCUCH\tTYP CZASTECZKI\tORGANIZM\n')
outfile.write(pdb_id+'\t'+chain_id+'\t'+molecule_type+'\t'+organism+'\n')
