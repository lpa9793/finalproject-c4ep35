import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb+srv://thanhnp:FEiM0OT3GTVUuhgO@cluster0-cqmi3.mongodb.net/test?retryWrites=true&w=majority")

db = client.team2

def search_all_food():
    return list(db.ff.find())

def search_food(keyword):
    return list(db.ff.find({'kw': keyword}))
