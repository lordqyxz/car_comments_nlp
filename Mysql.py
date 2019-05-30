import pymysql
import  iconfig

host = iconfig.mysql['host']
port = iconfig.mysql['port']
user = iconfig.mysql['user']
passwd = iconfig.mysql['password']

schema = "car"
err = "数据库错误"

db = pymysql.connect(host, user, passwd, schema)
cursor = db.cursor()


def close():
    db.close()


def getAllCar():
    sql = "select car_id,car_name from car "
    cursor.execute(sql)
    data = cursor.fetchall()
    # db.close()
    return data


def getAllCar2(limit):
    sql = "select car_id,car_name from car " + limit
    cursor.execute(sql)
    data = cursor.fetchall()
    # db.close()
    return data


def getCarIdByName(str):
    sql = "select car_id from car where car_name = '%s'"
    # str = str.replace('(', '').replace(')', '')
    dt = (str,)
    cursor.execute(sql % dt)
    result = cursor.fetchone()
    return result


def getCoarseFeatureIdByName(str):
    sql = "select coarse_grained_feature_id from coarse_grained_featureset where coarse_grained_feature_name = '%s'"
    dt = (str,)
    cursor.execute(sql % dt)
    result = cursor.fetchone()
    # db.close()
    return result


def addCoarseFeature(str):
    sql = "INSERT INTO `car_test`.`coarse_grained_featureset` (`coarse_grained_feature_name`) VALUES ('%s');"
    dt = (str,)
    try:
        cursor.execute(sql % dt)
        db.commit()
    except:
        db.rollback()


def addCarCommentCount(list):
    for dic in list:
        sql = """INSERT INTO `car`.`comment_count` (`car_type`, `count`) VALUES (%s, %s);"""
        cursor.execute(sql, [dic['_id'], dic['total_num']])
    try:
        db.commit()
    except:
        db.rollback()
        print(err)
        close()


def addWordCount(dic):
    for feature in dic:
        for word in dic[feature]:
            sql = """INSERT INTO `car`.`word_count` (`car_id`, `feature`, `word`, `count`) VALUES (%s, %s, %s, %s);"""
            cursor.execute(sql, ["卡罗拉",feature, word, dic[feature][word]])
    try:
        db.commit()
    except:
        db.rollback()
        print(err)
        close()
