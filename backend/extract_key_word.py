# coding:utf-8

from sklearn.feature_extraction.text import TfidfVectorizer
# import numpy as np
from clean_word import clean_word

def get_key_word(articles):
    articles = articles.split('。')
    articles = [clean_word(n) for n in articles]

    tfidf_model = TfidfVectorizer().fit(articles)
    key_word = sorted(tfidf_model.vocabulary_.items(), key=lambda x: x[1], reverse=True)[0:8]
    key_word = [w[0] for w in key_word]
    return key_word

if __name__ == '__main__':
    test = '''
    此外，自本周（6月12日）起，除小米手机6等15款机型外，其余机型已暂停更新发布（含开发版/体验版内测，稳定版暂不受影响），以确保工程师可以集中全部精力进行系统优化工作。有人猜测这也是将精力主要用到MIUI 9的研发之中。\r\nMIUI 8去年5月发布，距今已有一年有余，也是时候更新换代了。\r\n当然，关于MIUI 9的确切信息，我们还是等待官方消息。\r\n
    '''

    print(get_key_word(test))