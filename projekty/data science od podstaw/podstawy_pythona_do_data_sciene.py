import re

my_regex = re.compile("[0-9+]", re.I)  # regex


# można przypisać funkcję do zmiennej i przekazać ją do innych funkcji w roli argumentów:

def double(x):
    return x * 2


def apply_to_one(f):
    return f(1)  # wywoluje podana funkcje z argumentem 1


my_double = double  # odwolanie do zdefiniowanej wcześniej funkcji
x = apply_to_one(my_double)
print(x)  # zwroci 2

#  anonimowe funkcje lambda

y = apply_to_one(lambda z: z + 4)

print(y)  # 5


# nie powinno sie przypisywac lambdy do zmiennych - lepiej korzystac ze słownika kluczowego def:

def another_double(x): return 2 * x


#  listy

integer_list = [1, 2, 3]

heterogeneous_list = ["String", 0.1, True]

list_of_lists = [integer_list, heterogeneous_list, []]

list_length = len(integer_list)

list_sum = sum(integer_list)

# konkatenacja powtórzeń listy

L = [123, 'mielonka', 1.23]

L + [4, 5, 6]  # Konkatenacje/powtórzenia także zwracają nową listę

LL = L * 2

# usuniecie elemenu z listy

L.pop(2)  # Zmniejszanie listy: usuwanie obiektu ze środka listy

# sortowanie list

M = ['bb', 'aa', 'cc']
M.sort()  # ['aa', 'bb', 'cc']
M.reverse()  # ['cc', 'bb', 'aa']

#  odczytywanie n-tych elementów

x = range(10)

zero = x[0]

one = x[1]

nine = x[-1]  # pobieranie ostatniego elementu

eight = x[-2]  # przedostatni element

first_three = x[:3]

three_to_end = x[3:]

one_to_four = x[1:5]  # wycinki (slice) , X[I:J], oznacza: „zwróć wszystkie znaki
# z ciągu X od przesunięcia I aż do przesunięcia J, ale bez tego ostatniego elementu”

#  S[:-1] # Wszystkie elementy bez ostatniego, ale w łatwiejszej postaci(0:-1)

#  S[1:] # Wszystko poza pierwszym znakiem (1:len(S))

last_three = x[-3:]

# nie mozna zmieniac zawartosci juz utworzonych list np S='Mielonka' potem s[0]='z' powinno byc S='z'+S[1:] 

without_first_and_last = x[1:-1]

print(x)
print(last_three)
print(without_first_and_last)

#  laczenie dwoch list

x = [1, 2, 3]
x.extend([4, 5, 6])
print(x)

#  dodawanie list

y = x + [4, 5, 6]

print(y)

#  dolaczanie do listy pojedynczego elementu

x = [1, 2, 3]
x.append(0)  # dodane na koncu listy
y = x[-1]
z = len(x)

#  rozpakowanie list

x, y = [1, 2]

# zagniezdzanie list

M = [[1, 2, 3],  # Macierz 3x3 w postaci list zagnieżdżonych
     [4, 5, 6],  # Kod może się rozciągać na kilka wierszy, jeśli znajduje się w nawiasach
     [7, 8, 9]]

M[1]  # Pobranie drugiego wiersza
M[1][2]  # Pobranie drugiego wiersza, a z niego trzeciego elementu

print(M)

print(x)  # x=1
print(y)  # y=2

#  pomijanie niepotrzebnych elementów
_, y = [1, 2]  # y=2 a pierwzy element został pominięty

print(y)

#  touple. toupli sie nie modyfikuje

moja_lista = [1, 2]
moja_toupla = (1, 2)
inna_toupla = 3, 4

#  nawiasy sa opcjonalne

print(moja_toupla)
print(inna_toupla)


#  toupole mozna wykorzystac przy zwracaniu informacji przez funkcję

def sum_and_product(x, y):
    return (x + y), (x * y)  # zwracal touple


sp = sum_and_product(2, 3)

print(sp)  # zwraca (5,6)

# słowniki

epmty_dict = {}

grades = {"Joel": 80, "Tim": 95}

joels_grade = grades["Joel"]

print(joels_grade)

try:
    kates_grade = grades["Kate"]
except KeyError:
    print("brak danych")

# czy klucz istnieje?

Joel_has_grade = "Joel" in grades
kate_has_grades = "Kate" in grades

print(Joel_has_grade)  # true
print(kate_has_grades)  # false

# definiowanie wartości

grades["Tim"] = 99
grades["Kate"] = 100
num_students = len(grades)

# słownik z bardziej złożoną strukturą

tweet = {
    "user": "joelgrus",
    "text": "Data science",
    "reetweet_count": 100,
    "hashtags": ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet_keys = tweet.keys()
print(tweet_keys)  # lista kluczy

tweet_values = tweet.values()
print(tweet_values)

tweet_items = tweet.items()  # lista par klucz-wartosc
print(tweet_items)

#  klucze słownika nie mogą byc modyfikowane

S = 'Mielonka'
print(S.find('ie'))  # Odnalezienie przesunięcia podłańcucha w S

print(S.replace('ie', 'XYZ'))  # Zastąpienie wystąpień podłańcucha innym)

line = 'aaa,bbb,ccccc,dd'
print(line.split(','))  # Podział na podciągi według znaków separatora

print(S.isalpha())  # Sprawdzenie zawartości: isalpha, isdigit itd

line = line.rstrip()  # usuniecie bialych znakow po prawej stronie
print(line)

line.rstrip().split(
    ',')  # polaczenie dwoch operacji vzyli usiniecie bialych znakow po prawej stronie i podzielenie tekstu

print(dir(S))  # LISTA ATRYBUTÓW KTÓRYCH MOŻNA UŻYĆ NA ŁAŃCUCHU ZNAKÓW!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

print(help(S.replace))  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! CO ROBI TA METODA?

S = 'A\nB\tC'  # \n oznacza znak końca wiersza, a \t to tabulator
len(S)  # Każdy z elementów składowych S to jeden znak

ord('\n')  # \n to jeden znak zakodowany jako wartość dziesiętna 10

S = 'A\0B\0C'  # \0, binarny bajt zerowy, nie kończy łańcucha znaków 5 znaków

print(len(S))

print(S)
