# -*- coding:utf-8 -*-
import re
import os
from pyltp import Segmentor
import jieba


basepath = os.path.abspath('.')
LTP_DATA_DIR = os.path.join(basepath, '\model\\') # ltp模型目录的路径
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')


def effient_cut(string):
    return  " ".join(jieba.cut(string))

def cut_word(string):
    segmentor = Segmentor()
    segmentor.load(cws_model_path)
    words = segmentor.segment(string)
    segmentor.release()

    return ' '.join(words)


def token(string):
    pat = re.compile('\\\\n|\\u3000|;|\\n|\s+')
    string = re.sub(pat, '', string)
    return ''.join(string)


def clean_word(string):
    # if not string: return ''
    return effient_cut(token(string))


if __name__ == '__main__':
    string = '  ' \
             '\n这是一个测试\\n\u3000'
    cleaned = clean_word((string))
    print(cleaned,type(cleaned))
