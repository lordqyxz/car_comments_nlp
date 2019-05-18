import Mongo
import Mysql
import re

def commentCount():
    cursor = Mongo.sortAndCount()
    commentCount = [doc for doc in cursor]
    Mongo.close()
    print(type(commentCount[0]))
    Mysql.addCarCommentCount(commentCount)
    Mysql.close()

def carNameConvert():
    data=Mongo.getAll(20)
    for item in data:
        carType=re.match(r'^[\w]*', item['data']['购买车型']).group(0)
        collection=Mongo.connect()
        myquery = {"_id": item['_id']}
        newvalues = {"$set": {"data.车型": carType}}
        collection.update_one(myquery, newvalues)
    Mongo.close()

carNameConvert()