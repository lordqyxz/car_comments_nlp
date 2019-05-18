from pymongo import MongoClient

url = "mongodb://47.102.131.233:27017/"
client = MongoClient(url)
database = client["car"]
collection = database["comments"]
BATCH_SIZE = 200

def connect():
    return collection

def getAll(num):
    query = {}
    projection = {}
    projection["data.购买车型"] = 1.0
    cursor = collection.find(query, projection=projection, batch_size=BATCH_SIZE)
    return cursor


def getCommentsByCarName(str):
    query = {}
    projection = {}
    query["data.购买车型"] =str
    projection["data.评价"] = 1.0
    cursor = collection.find(query, projection=projection, batch_size=BATCH_SIZE)
    return cursor


def sortAndCount():
    pipeline = [
        {
            "$group": {
                "_id": u"$data.购买车型",
                "total_num": {
                    "$sum": 1.0
                }
            }
        }, {
            "$sort": {"total_num": -1}
        }
    ]
    cursor = collection.aggregate(pipeline, allowDiskUse=False)
    return cursor


def close():
    client.close()
