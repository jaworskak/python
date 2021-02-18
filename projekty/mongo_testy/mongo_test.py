import pymongo  # biblioteka mongo
import pandas as pd  # python -m pip install pandas

client = pymongo.MongoClient("localhost", 27017) #  lokalne mongo

#  nowa baza danych

db = client.testymb

#  dodawanie pojedynczego rekordu do bazy

irs_col_sing = db["northeast_area_test_sing"] #  dodajemy nowa kolekcje danych

northeast_1 = {"EIN": 19818,
               "NAME": "PALMER SECOND BAPTIST CHURCH",
               "STREET": "1050 THORNDIKE ST"}

x = irs_col_sing.insert_one(northeast_1)

northeast_2 = {"EIN": 73102,
               "NAME": "THINK TANK ROMANIA INC",
               "STREET": "1050 THORNDIKE ST"}

x = irs_col_sing.insert_one(northeast_2)

northeast_3 = {"EIN": 73102,
               "NAME": "THINK TANK ROMANIA INC",
               "STREET": "1000 ST"}

x = irs_col_sing.insert_one(northeast_3)

print('zawartosc kolekcji irs_col_sing')

#  wypisanie wszystkich elementow
cursor = irs_col_sing.find({})
for document in cursor:
    print(document)


#  update konkretnego rekordu (zmiana danych)

update_query = {"EIN": 19818}
new_values = {"$set": {"EIN": 19888}}

irs_col_sing.update_one(update_query, new_values)
print('rekord po zmianach:')
print(irs_col_sing.find_one({"EIN": 19888}))  # pierwszy rekord

# szukanie wszystkich, ktore
streets = irs_col_sing.find({"STREET": "1050 THORNDIKE ST"})
print("szukanie po ulicy")
for document in streets:
    print(document)

#  usuwanie elementu
irs_col_sing.delete_one({"EIN": 19888})

print("wiersze po usunieciu:")
#  wypisanie wszystkich elementow
cursor = irs_col_sing.find({})
for document in cursor:
    print(document)

