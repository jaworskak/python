# program wypisuje slowo wspak, sprawdza czy jest palindromem i wypisuje anagramy
import webbrowser

print('Podaj słowo')
word = input()
word = word.lower().replace(" ", "")

# odwrocony string
rev_word = word[::-1]

print(rev_word)

# czy slowo jest palindormem?
if rev_word == word:
    print("Palindrom")
else:
    print("Słowo nie jest palindromem")

webbrowser.open("https://poocoo.pl/scrabble-slowa-z-liter/" + word)