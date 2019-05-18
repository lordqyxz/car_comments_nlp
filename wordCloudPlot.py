# -*- coding: utf-8 -*-
from os import path
import os
from PIL import Image
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt

IMG_SRC = "cartest.png"

import pymysql

# MySQL配置
host = "47.102.131.233"
port = 3306
user = "root"
password = "ShiYuzhu.18"
db = "car"

# 连接MySQL
connect = pymysql.Connect(
    host=host,
    port=port,
    user=user,
    password=password,
    db=db,
    charset="utf8"
)
cursor = connect.cursor()


def dbClose():
    cursor.close()
    connect.close()


def getWordCount(car_id, feature):
    """
    返回对应车型和特征的分词和数量
    :param car_id: 车型ID 
    :param feature: 特征
    :return item:分词数字典
    """
    sql = "SELECT word, count FROM word_count WHERE car_id = '%s' AND feature = '%s' ORDER BY count DESC LIMIT 200"
    data = (car_id, feature)
    cursor.execute(sql % data)

    results = cursor.fetchall()
    item = {}
    for result in results:
        item[result[0]] = result[1]
    # print(item)
    return item


def plot(wordCloud):
    plt.figure(figsize=(20, 20))
    plt.imshow(wordCloud, interpolation="bilinear")
    plt.title("deafault")
    plt.axis("off")
    plt.show()


car_id = '卡罗拉'
feature = 1
mask = np.array(Image.open(IMG_SRC))
frequencies = getWordCount(car_id, feature)
wordCloud = WordCloud(background_color="aliceblue",font_path='C:\Windows\Fonts\simkai.ttf', max_font_size=50,
                      relative_scaling=.5, max_words=200,mask=mask)
wordCloud.generate_from_frequencies(frequencies)
plot(wordCloud)
dbClose()
