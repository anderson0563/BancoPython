import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["AirBNB"]
mycol = mydb["RJ"]

myquery = { "neighbourhood": "Copacabana" }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x['host_name'])