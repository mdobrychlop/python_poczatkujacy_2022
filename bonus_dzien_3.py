# DUŻY BONUS: DEFINIOWANIE WŁASNYCH FUNKCJI
#
# Definiowanie własnych funkcji jest niezmiernie przydatną
# umiejętnością. Pozwala na wielokrotne wykonywanie złożonych
# operacji bez konieczności powtarzania dużych bloków kodu.

# Poniżej znajduje się kod odpowiedzialny za definicję funkcji
# sum_of_squares, która przyjmuje dwie liczby i zwraca sumę
# kwadratów tych liczb.

# W pierwszej linii korzystamy ze słowa kluczowego def, które
# oznacza, że zaczynamy definicję funkcji.
# Następnie podajemy nazwę funkcji, a w nawiasie okrągłym
# możemy (choć nie musimy) zdefiniować, ile funkcja będzie
# przyjmować argumentów. Poniższy przykład to funkcja, która
# przyjmuje dwa argumenty. To, jak je w tym miejscu nazwiemy,
# nie ma znaczenia - z tych nazw będziemy korzystać jedynie
# w samej definicji. Korzystamy z nich, żeby móc w naszej
# definicji określić, jak podawane przy wywołaniu funkcji
# dane będą przez naszą funkcję przetwarzane.
def sum_of_squares(x, y):
  # W kolejnych trzech liniach przeprowadzamy działania na
  # argumentach. Liczby, które podamy wywołując funkcję w
  # przyszłości zostaną podstawione pod zmienne x i y widoczne
  # w niniejszej definicji. Obydwie zostaną zatem:

  # Podniesione do kwadratu (** oznacza podnoszenie do potęgi)
  x_squared = x ** 2
  y_squared = y ** 2
  # Następnie wyniki podnoszenia liczb zostaną zsumowane.
  result = x_squared + y_squared

  # Na końcu funkcji pojawia się słowo kluczowe return, a po
  # nim następuje nazwa zmiennej, której wartość będzie zwracana
  # przez funkcję po jej wywołaniu. W przypadku niniejszej
  # funkcji, będzie to obliczona wyżej suma kwadratów.
  return result

# Poniższy kod wywoła zatem funkcję sum_of_squares, podając jej
# jako argumenty liczby 3 i 4.
s_o_s = sum_of_squares(3, 4)


# Powyższy kod możemy zrozumieć wyobrażając sobie, że w momencie
# wywołania kodu sum_of_squares(3,4), liczba 3 wędruje do naszej
# definicji wyżej, i zastępuje zmienną x. Podobnie, liczba 4
# zastępuje zmienną y. Należy pamiętać, że kolejność podawanych
# argumentów jest oczywiście istotna.
# Wartość "zwracana" z funkcji dzięki instrukcji return, to
# wartość, która zostanie wyrzucona poza funkcję i odłożona do
# zmiennej, jeżeli wywołanie funkcji poprzedza znak równości.
# W naszym wypadku wartość zwracana przez return zostanie zapisana
# w zmiennej s_o_s. Możemy ją następnie wypisać za pomocą print:
print(s_o_s)  # wyświetli 25

# Jak wiemy z zajęć, możemy też bezpośrednio wywołać naszą funkcję
# przed wywołaniem printa, dzięki takiemu kodowi:
print(sum_of_squares(2,5)) # wyświetli 29

# Ważne:
# - Instrukcja return ZAWSZE kończy działanie funkcji, nawet
#   jeśli zostaje wywołana wewnątrz pętli
# - Wszelkie zmienne będące definicją funkcji, takie jak x, y,
#   x_squared, y_squared czy result w powyższym przykładzie,
#   są zmiennymi lokalnymi, tzn. Wykorzystywanymi jako
#   "placeholdery" wewnątrz definicji. Korzystanie z nich poza
#   definicją funkcji nie jest możliwe. Na przykład, jeżeli
#   w programie takim jak powyższy spróbujemy wyprintować
#   zmienną x, lub y_squared itd. gdziekolwiek poza definicją
#   funkcji, to Python zwróci wyjątek, że taka zmienna
#   nie istnieje. Jeżeli chcemy, możemy nazwać jakieś zmienne
#   w reszcie kodu tak samo jak w definicji funkcji, ale
#   będą to zupełnie niezależne zmienne.
# - Definicja funkcji musi występować wcześniej w kodzie, niż
#   linia, w której tę funkcję wywołujemy. Dobrą praktyką jest
#   umieszczanie wszystkich definicji na początku kodu.
# - Sama definicja funkcji nie spowoduje żadnego widocznego
#   wpływu na działanie programu po jego uruchomieniu. Python
#   przeczyta definicję i zapamięta "ok, jeżeli ktoś postanowi
#   uruchomić funkcję o nazwie sum_of_squares, to mam wykonać
#   takie i takie działania."
# - Funkcja może nie przyjmować żadnego argumentu, może też
#   przyjmować ich bardzo wiele.
#
#
# Poniżej przykład innej funkcji, rozwiązującej problem podobny
# do jednego z niedawnych zadań domowych. Funkcja przyjmuje
# argument n, a następnie pyta użytkownika o podanie liczby n
# razy. Następnie zwraca średnią wszystkich podanych liczb.


def sum_of_n_numbers(n):
	# Przygotowujemy zmienną, w której będziemy sumować liczby
	suma = 0
	# Przygtowujemy licznik, który będzie kontrolował przejścia
	# pętli while
	i = 0
	# Pętla while: tak długo, jak licznik jest mniejszy, niż
	# liczba podana jako argument...
	while i < n:
		# Przyjmij liczbe od użytkownika i zamień na integer
		new_number = int(input("Podaj liczbe: "))
		# Dodaj liczbę do sumy
	    suma += n
	    # Zwiększ licznik
	    i += 1

	# na końcu zwróć średnią, czyli wynik dzielenia sumy przez
	# liczbę przyjętych liczb (czyli przez n)
	return suma / n

# Po wywołaniu poniższej linii, funkcja sum_of_numbers zapyta
# użytkownika o 3 liczby, a następnie obliczy ich średnią i
# odłoży ją w zmiennej suma_trzech_liczb.
suma_trzech_liczb = sum_of_numbers(3)
print(suma_trzech_liczb)


# Na koniec jeszcze jeden przykład, pokazujący, jak definiować
# funkcję, w której jeden z 3 argumentów ma domyślną wartość.
# Przy wywoływaniu takiej funkcji, możemy podać 2 lub 3 argumenty,
# tzn. musimy podać przynajmniej 2, ale jeżeli pominiemy trzeci,
# to automatycznie przyjmie on domyślną wartość.

# W poniższym przypadku możemy wywołać funkcję podając 3 liczby
# jako argumenty. Wtedy zwrócony zostanie ich iloczyn.
# Jeżeli jednak podamy tylko dwie liczby, to ich iloczyn zostanie
# pomnożony przez 1 - czyli przez domyślną wartość trzeciego
# argumentu c. Domyślna wartość zostaje ustalona w nawiasie,
# w pierwszej linii definicji (c = 1)
def multiply(a, b, c = 1):
	return a * b * c

print(multiply(2,5)) # wypisze 10
print(multiply(2,5,3)) # wypisze 30

# Funkcje mogą też zwracać więcej niż jedną wartość.
# Na przykład, poniższa funkcja zwróci kwadraty wszystkich
# trzech argumentów

def squares(a, b, c):
	a_sq = a**2
	b_sq = b**2
	c_sq = c**2
	return a_sq, b_sq, c_sq

# W takiej sytuacji, jeżeli chcemy odłożyć wynik działania
# funkcji squares do zmiennych, musimy albo:
# - Po lewej stronie znaku równości podać 3 zmienne:

r1, r2, r3 = squares(2,5,3)
# Wtedy każda z tych zmiennych po kolei przyjmie jedną 
# zwracaną wartość (r1=a_sq, r2=b_sq, r3=c_sq)
print(r1, r2, r3) # wypisze 4, 25, 9

# - Albo podać 1 zmienną:
all_sqs = squares(2,5,3)
# Wtedy zmienna al_sqs przyjmie KROTKĘ zawierającą 3 zwrócone
# liczby.
print(all_sqs) # wypisze (4,25,9)

# To jeszcze na sam koniec - co to jest ta krotka?
# Krotka (ang. tuple) jest typem danych podobnym do listy, tzn.
# może przechowywać sekwencję różnych obiektów, np. liczb.
# Od listy różni się tym, że krotka nie jest modyfikowalna.
# Po zdefiniowaniu krotki, nie możemy z niej usunąć ani do niej
# dodać wartości. Definiujemy ją tak jak listę, ale korzystając
# z nawiasów okrągłych

nasza_krotka = (5,10,15,20)

# Do jej elementów odnosimy się za pomocą indeksów tak samo jak
# w przypadku list, tzn. korzystając z nawiasów kwadratowych

print(nasza_krotka[0]) # wypisze 5

# Krotkę można przekonwertować w razie potrzeby na listę:

lista = list(nasza_krotka)
print(lista) # wypisze [5,10,15,20]

# Można też dokonać konwersji w drugą stronę:

nasza_lista = [2,4,6,8,10]
krotka = tuple(nasza_lista)

#
###
####