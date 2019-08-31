# -*- coding:utf-8 -*-
import re
import jieba
from app import segmentor


def effient_cut(string):
    return  " ".join(jieba.cut(string))

def cut_word(string):
    words = segmentor.segment(string)
    return ' '.join(words)


def token(string):
    pat = re.compile('\\\\n|\\u3000|;|\\n|\s+|\t+')
    string = re.sub(pat, '', string)
    return ''.join(string)


def clean_word(string):
    # if not string: return ''
    return effient_cut(token(string))


# if __name__ == '__main__':
#     string = '  ' \
#              '\n这是一个测试\\n\u3000'
#     cleaned = clean_word((string))
#     print(cleaned,type(cleaned))
