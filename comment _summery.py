import Mongo
import Mysql


def commentCount():
    cursor = Mongo.sortAndCount()
    commentCount = [doc for doc in cursor]
    Mongo.close()
    print(type(commentCount[0]))
    Mysql.addCarCommentCount(commentCount)
    Mysql.close()
