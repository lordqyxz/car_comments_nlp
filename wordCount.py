import Mongo
import Mysql
import re
import jieba

def getComments():
    carName = "卡罗拉 2014款 1.6L GL-i 手动"
    return Mongo.getCommentsByCarName(carName)


def removePunctuation(str):
    return re.sub(r'(\W|\d+?)', '', str)


def stopWordsList(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


def segComment(str):
    str = removePunctuation(str)
    seg_list = []
    seg_list = jieba.lcut(str, cut_all=False)
    return seg_list


def wordCounts(word_dict):
    count = list(word_dict.items())
    count.sort(key=lambda x: x[1], reverse=True)
    return count


def wordCount(data):
    word_count = {}
    for doc in data:
        comments = doc['data']
        comment_dic = {}
        for feature in comments['评价']:
            seg_list = segComment(comments['评价'][feature])
            stop_words = stopWordsList('stop_words.txt')
            word_dict = {}
            for item in seg_list:
                if item not in stop_words:
                    if item not in word_dict:
                        word_dict[item] = 1
                    else:
                        word_dict[item] += 1
            comment_dic[feature] = word_dict
        for feature in comment_dic:
            if feature in word_count:
                for word in comment_dic[feature]:
                    if word in word_count[feature]:
                        word_count[feature][word] += comment_dic[feature][word]
                    else:
                        word_count[feature][word] = 1
            else:
                word_count[feature] = {}
    print("-" * 60)
    return word_count


if __name__ == '__main__':
    import os
    fin = ["Dictionary/%s" % (fname,) for fname in os.listdir("Dictionary")]
    jieba.load_userdict(fin)
    # data = getComments()
    # word_count_dic = wordCount(data)
    # Mysql.addWordCount(word_count_dic)
    # Mysql.close()
