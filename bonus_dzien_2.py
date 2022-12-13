# bonus_list_01.py
#
# Python pozwala w prosty sposób sprawdzić,
# czy element znajduje się w liście.

animals = ['dog','cat','bird','hamster','bat']

if 'cat' in animals:
    print('yes, cat is one of the elements')

# Podobnie można sprawdzać łańcuchy znaków

name = 'Magdalena'

if 'x' in name:
    print('x is one of the strings characters')
else:
    print('x is not part of the string')

# Listy można też łatwo łączyć, podobnie jak łańcuchy:

animals = ['dog','cat','bird','hamster','bat']
numbers = [54, 12, 33, 2, 67, 8, 10, 2, 6]

concatenated_list = animals + numbers
print(concatenated_list)

# bonus_list_02.py
#
# Python oferuje bardzo wiele przydatnych,
# wbudowanych metod do pracy na listach.

animals = ['dog','cat','bird','hamster','bat']
numbers = [54, 12, 33, 2, 67, 8, 10, 2, 6]

# len() zwraca długość listy
print(len(animals)) 

# sorted() zwraca posortowaną listę.
# Jeżeli elementami są łańcuchy, będzie to sortowanie alfabetyczne.
print(sorted(animals))
print(sorted(animals), reverse=True) # tak odwraca się kolejność sortowania
print(sorted(numbers))

# insert() pozwala umieścić nowy element pod wybranym indeksem.
# następujące po nim elementy przesuwają się o 1
animals.insert('penguin', 2)
print(animals)

# pop() usuwa oraz zwraca ostatni element listy
ostatni_element = animals.pop()
print(ostatni_element)
print(animals)

# index() zwraca indeks pierwszego wystąpienia szukanego elementu
print(animals)
print(animals.index(3))

# count() zwraca liczbę wystąpień danego elementu w liście
print(animals.count('dog'))
animals.append('dog')
print(animals.count('dog'))

# reverse() odwraca kolejność elementów w liście.
# jest to metoda, która zmienia zawartość pierwotnej listy,
# a nie zwraca zmienioną listę!
print(animals)
print(animals.reverse())
print(animals)

# min() i max() pozwalają na znalezienie największego
# i najmniejszego elementu

# min() i max() zwracają najmniejszy i największy element listy
print(min(numbers))
print(max(numbers))

# sum() zwraca sumę wszystkich elementów listy
print(sum(numbers))

# bonus_string_index_02.py
#
# Po łańcuchu można iterować jak po liście za pomocą pętli.


#       012345
name = 'Janusz'

for letter in name:
    print(letter)


# for_01.py
#
# Metoda range() służy do tworzenia sekwencji liczb całkowitych.
# Składnia: range(start, stop, step) gdzie:
# - start: pierwsza liczba w sekwencji
# - stop: ostatnia liczba w sekwencji + 1
# - step: krok

for i in range(5,10,1):
    print(i)

# Możemy też podać tylko jeden argument. Wtedy zostanie on uznany
# za argument "stop". Przykład:

for i in range(10):
    print(i)

# Podanie dwóch argumentów wskaże z kolei start i stop:

for i in range(25,35):
    print(i)


# file_writing_01.py
#
# Metodę open() można również, między innymi, otwierać
# z argumentem "a" (od "append").
# Jeżeli w danej lokalizacji istnieje już plik o podanej nazwie, to 
# zostanie on otwarty, ale wszelkie treści, które będziemy do niego 
# dopisywać, będą dodawane na końcu pliku (w przeciwieństwie do 
# otwierania z argumentem "w", które zawsze powoduje utworzenie
# pustego pliku).
# Jeżeli plik nie istnieje, to zostaje utworzony nowy plik.
#
# Aby zamknąć plik, co umożliwia jego ponowne otwarcie w innym trybie,
# wykorzystujemy metodę close().

outfile = open('animals.txt','w')

outfile.write('dog\n')
outfile.write('cat\n')

outfile.close()

outfile = open('animals.txt','a')

outfile.write('fish\n')

outfile.close()

outfile = open('animals.txt','r')

contents = outfile.read()

print(contents)
