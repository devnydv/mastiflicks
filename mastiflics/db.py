import json
from pymongo.mongo_client import MongoClient
import os

#database config
#api = os.environ.get("mongo")
api = os.getenv('DB')
#api = "mongodb+srv://bittumail:12356789@cluster0.fqrswkj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
url = api
client = MongoClient(url)
db = client.mastiflicks
collection = db.data
def oneid ():
    return collection.find().sort('_id', -1).skip(0).limit(1)


def catedata(start, cate):
    if cate =="all":
        return list(collection.find().sort('_id', -1).skip(start).limit(12))
    else:
        data = list(collection.find({"cat": cate}).sort('_id', -1).skip(start).limit(12))
        return data

def catsize(cate):
    if cate =="all":
        return collection.count_documents({})
    else:
        #amnt= collection.find({"cat": cate}).count()
        return collection.count_documents({"cat": cate})
    
def readone(id):
    onep = collection.find_one({'id':id})
    return onep

def update(updata, id):
    collection.delete_one({"id": id})
    collection.insert_one(updata)
    


def submit(subdata):
    collection.insert_one(subdata)
    print(subdata)