import requests
import json
import os

#adres rapidAPI
url = "https://imdb8.p.rapidapi.com/title/find"

print('Podaj film')
movie_title = input()


querystring = {"q": movie_title}

headers = {
    'x-rapidapi-key': os.environ['rapid_key'],  # zmienna środowiskowa
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

if response:
    x = json.loads(response.content)  # zamieniam response na jsona
    y = [z for z in x["results"] if "title" in z and z["titleType"] == "movie"]  # wybieram wiersze które reprezentuja filmy (nie np odcinki serialu)
    for z in y:
        if movie_title.lower() in z["title"].lower(): 
            print(z["title"])
            if "year" in z:
                print("rok produkcji: "+str(z["year"]))
            else:
                print("rok produkcji: brak danych")
            if "runningTimeInMinutes" in z:
                print("czas trwania: " + str(z["runningTimeInMinutes"]))
            else:
                print("czas trwania: brak danych")
            if "principals" in z:
                a = z["principals"]
                print("wystepuja:")
                for aa in a:
                    if "category" in aa and "cha":
                        if aa["category"] == "actor":
                            print(aa["name"]+" jako "+aa["characters"][0])
            print("\n")

else:
    print('Nie ma takiego filmu')
