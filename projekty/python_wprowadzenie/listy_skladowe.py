#  Poza operacjami na typach sekwencyjnych i metodami obiektów listy Python obsługuje bardziej zaawansowane operacje, znane pod nazwą wyrażeń
#  list składanych (ang. list comprehension expressions; inaczej wyrażenia listowe), które świetnie nadają się do przetwarzania struktur
# takich jak nasza macierz. Przypuśćmy na przykład, że chcemy pobrać drugą kolumnę naszej
# prostej macierzy. Za pomocą zwykłego indeksowania łatwo jest pobierać wiersze, ponieważ
# macierze przechowywane są wierszami. Podobnie łatwo jest pobrać kolumnę za pomocą wyrażenia listy składanej:

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

col2 = [row[1] for row in M]  # Zebranie elementów z drugiej kolumny

print(col2)

print([row[1] + 1 for row in M])   # dodanie 1 do kazdego elementu w drugiej kolumnie

print([row[1] for row in M if row[1] % 2 == 0])  # Odfiltrowanie elementów nieparzystych

print(M)  # macierz wciaz bez zmian

diag = [M[i][i] for i in [0, 1, 2]]  # Pobranie przekątnej z macierzy

print(diag)

doubles = [c * 2 for c in 'mielonka']  # Powtórzenie znaków w łańcuchu

#  stworzenie generatora
print(M)
G = (sum(row) for row in M)  # Utworzenie generatora sum wierszy 1 + 2 + 3
print(G)
print(next(G))
print(next(G)) #  Wykonanie iteracji, obliczenie kolejnej sumy i wyświetlenie wyniku


