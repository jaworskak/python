import pymongo  # biblioteka mongo
import pandas as pd  # python -m pip install pandas

client = pymongo.MongoClient("localhost", 27017) #  lokalne mongo

#  nowa baza danych

db = client.baza_test

print('nazwa bazy')
print(db.name)

print('dodane kolekcje')
print(db.list_collection_names())  #  na razie nic nie ma bo nic nie dodalismy

irs_col = db["northeast_area_test"] #  dodajemy nowa kolekcje danych

print(db.list_collection_names())  #  na razie nic nie ma bo nic nie dodalismy
#  kolekcja pojawia sie dopiero po dodaniu do niej danych!

#  dodanie calego pliku csv
def csv_to_json(filename, header=None):
    data = pd.read_csv(filename)
    data['ID'] = range(1, len(data) + 1)  #  dodaje id - musi byc id
    return data.to_dict('records')

irs_col.insert_many(csv_to_json('eo4.csv')) #  dodaje do kolekcji caly plik eo4.csv zamieniony na

print('zawartosc kolekcji irs_col - pierwszy element')
print(irs_col.find_one())

print('zawartosc kolekcji irs_col - wszystkie elementy')
print(irs_col.estimated_document_count())
