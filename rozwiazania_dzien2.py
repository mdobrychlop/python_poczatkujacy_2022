
# Napisz program, który przyjmie od użytkownika 10 liczb całkowitych
# i wyświetli sumę wszystkich elementów. Niech przyjmowanie
# kolejnych liczb odbywa się w pętli, a liczby będą odkładane do
# listy.

lista_liczb = []

while len(lista_liczb) < 10:
    liczba = int(input("Podaj liczbe: "))
    lista_liczb.append(liczba)

print(sum(lista_liczb))


# Stwórz w kodzie listę przechowującą 15 liczb. Napisz program,
# który stworzy nową listę, która będzie zawierać jedynie liczby
# parzyste z pierwszej listy. Wypisz listę wynikową

lista_15_liczb = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

lista_parzystych = []

for l in lista_15_liczb:
    if l % 2 == 0:
        lista_parzystych.append(l)

print(lista_parzystych)

# Napisz program, który:
# - odczyta plik FASTA z wcześniejszych przykładów
# - stworzy nowy plik FASTA
# - do nowego pliku przeniesie zawartość wejściowego pliku
# - dodatkowo, stworzy kolejny rekord w wyjściowym pliku (nowy nagłówek, nowa sekwencja),
#   który będzie zawierał pierwotny nagłówek z dopiskiem ’complementary’, oraz sekwencję
#   komplementarną do sekwencji wejściowej.
# Aby obliczyć sekwencję komplementarną, należy zamienić każdy znak na jego odpowiednik
# z tabeli par komplementarnych, tj. A na U, U na A, C na G oraz G na C. W ten sposób
# otrzymujemy sekwencję komplementarną dla danej sekwencji RNA.

infile = open('trna_sequence.fasta','r')
outfile = open('trna_complementary.fasta','w')

original_record = infile.read()

new_record_lines = original_record.split('\n')

new_header = new_record_lines[0] + '|complementary'

new_record_sequence = ''.join(new_record_lines[1:])

complementary_sequence = ''

for n in new_record_sequence:
    if n == 'A':
        complementary_sequence += 'U'
    elif n == 'U':
        complementary_sequence += 'A'
    elif n == 'C':
        complementary_sequence += 'G'
    else:
        complementary_sequence += 'C'

outfile.write(original_record + '\n')
outfile.write(new_header + '\n')
outfile.write(complementary_sequence[:60] + '\n')
outfile.write(complementary_sequence[60:] + '\n')


# Napisz program, który odczyta plik multiple_seqs.fasta, a następnie wyświetli na ekranie
# wszystkie sekwencje z tego pliku, które są dłuższe niż podany próg długości.
# Niech próg podaje użytkownik.

infile = open('multiple_seqs.fasta','r')

all_lines = infile.readlines()

length_threshold = int(input('Podaj maksymalna dlugosc sekwencji:'))

for l in all_lines:
    if l[0] != '>':
        if len(l) <= length_threshold:
            print(l)


# Stwórz plik tekstowy zawierający jeden akapit dowolnego artykułu z internetu. Napisz
# program, który stworzy i wyświetli łańcuch znaków, w którym znajdą się wszystkie
# słowa z wejściowego tekstu, ale w odwrotnej kolejności. Niech wyjściowy tekst nie
# zawiera żadnych znaków interpunkcyjnych.

infile = open('akapit.txt','r')

contents = infile.read()

# string.punctuation

punctuation = ['!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[','\\',']','^','_','`','{','|','}','~']

words = contents.split()

clean_words = []

for w in words:
    for p in punctuation:
        w.replace(p,'')
    clean_words.append(w)

print(clean_words)
clean_words.reverse()

print(clean_words)



# Napisz program, który odczyta plik multiple_seqs.fasta, a następnie:
# - stworzy plik tekstowy, w którym w kolumnach zapisze dla każdej sekwencji RNA:
# - - - wszystkie informacje z nagłówka pliku
# - - - długość sekwencji
# - - - liczbę wystąpień każdego z nukleotydów (A,C,G,U)
# - - - (sekwencje białkowe niech nie będą brane pod uwagę w tym pliku)
# - stworzy nowy plik FASTA, w którym zapisze tylko sekwencje białkowe

infile = open('multiple_seqs.fasta','r')
out_rna = open('MD_rna_info.txt','w')
out_protein = open('MD_protein_seqs.fasta','w')

out_rna.write('PDB ID\tCHAIN ID\tMOL TYPE\tORGANISM\tSEQ LEN\tA COUNT\tC COUNT\tG COUNT\tU COUNT\n')

in_lines = infile.readlines()

for l in in_lines:
    if l[0] == '>':
        header_info = l.split('|')
        pdb_id = header_info[0].replace('>','')
        chain_id = header_info[1].replace('Chain ','')
        mol_type = header_info[2]
        organism = header_info[3].replace('\n','')

        if mol_type != 'Protein':
            out_rna.write(pdb_id+'\t'+chain_id+'\t'+mol_type+'\t'+organism+'\t')
        else:
            out_protein.write(l)
    else:
        if mol_type != 'Protein':
            seq_len = str(len(l)-1)
            a_count = str(l.count('A'))
            c_count = str(l.count('C'))
            g_count = str(l.count('G'))
            u_count = str(l.count('U'))
            out_rna.write(seq_len+'\t'+a_count+'\t'+c_count+'\t'+g_count+'\t'+u_count+'\n')
        else:
            out_protein.write(l)
