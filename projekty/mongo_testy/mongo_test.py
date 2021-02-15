import pymongo  # biblioteka mongo
import json
import pandas as pd  # python -m pip install pandas

# instalacja mongo ubuntu https://tecadmin.net/install-mongodb-on-ubuntu/

client = pymongo.MongoClient("localhost", 27017)  # postawilam mongo lokalnie
db = client.irs
print(db.name)  # sprawdzenie (test) jak sie nazywa nasza baza

print(db.list_collection_names())  # na razie mamy tylko domyslna koleckcje my_collection

#  dodajemy nowa kolekcje dla danych https://www.irs.gov/charities-non-profits/exempt-organizations-business-master-file-extract-eo-bmf
#  kolekcje tworza sie dopiero wtedy kiedy cos do nich dodamy

irs_col = db["northeast_area_test"]

#  dodane dokumentu
northeast_1 = {"EIN": 19818,
               "NAME": "PALMER SECOND BAPTIST CHURCH",
               "STREET": "1050 THORNDIKE ST"}

x = irs_col.insert_one(northeast_1)

print(db.list_collection_names())  # mamy dwie kolekcje - northeast_area i my_collection

#  wypisanie tego co mamy w northeast_ares

print(irs_col.find_one())  # pierwszy rekord

print(irs_col.find_one({"EIN": 19818}))  # Po konkretnych danych

#  wypisanie wszystkich elementow
cursor = irs_col.find({})
#for document in cursor:
#    print(document)

#  update konkretnego rekordu (zmiana danych)

update_query = {"EIN": 19818}
new_values = {"$set": {"EIN": 19888}}

irs_col.update_one(update_query, new_values)
print(irs_col.find_one())  # pierwszy rekord

#  update konkretnego rekordu (usuniecie danych)

irs_col.delete_one({"EIN": 19888})
print(irs_col.find_one())


#  dodanie calego pliku csv

def csv_to_json(filename, header=None):
    data = pd.read_csv(filename)
    data['ID'] = range(1, len(data) + 1)  #  dodaje id
    return data.to_dict('records')

irs_col2 = db["northeast_area2"]
irs_col2.insert_many(csv_to_json('eo4.csv'))

print(irs_col2.find_one())
