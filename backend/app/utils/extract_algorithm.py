# -*- coding:utf-8 -*-
import os
from app.utils.clean_word import clean_word
from app.utils.similar_word.find_related_words import load_file
from pyltp import Segmentor, SentenceSplitter, Postagger, NamedEntityRecognizer, Parser

import sys
basepath = os.path.abspath('.')
sys.path.append(basepath)
path = os.getcwd()

LTP_DATA_DIR = path + '\\app\\model\\' # ltp模型目录的路径
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型路径，模型名称为`pos.model`
par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`

def cut_sentence(string):
    '''
    分句函数
    @intput string: A long text with lots of sentences.
    @output: list[sentence1,sentence2]
    '''
    sents = SentenceSplitter.split(string)
    sentences = [s for s in sents if len(s) !=0]

    return sentences

def cut_word(sentence):
    '''
    分词函数
    @input:[sentence1,sentence2,...]
    @output: [word_1,word_2,....]
    '''
    words = []
    for sents in sentence:
        words += clean_word(sents).split(' ')
    return words

def word_pos(sents):
    '''
    词性标注函数
    @input: [sentence1, sentence2,...]
    @切词在函数内进行
    @output: [postag1, postag2, ....]
    '''
    postagger = Postagger()
    postagger.load(pos_model_path)

    words = cut_word(sents)
    postag = postagger.postag(words)

    postagger.release()
    return list(postag)


def ner(words, pos):
    '''
    命名实体识别函数
    @ input: cut_word:List  postag: List
    @ output: Name Entity Recognizer: List
    @ explanation: Nh:人名   Ni:机构名 Ns:地名 S:这个词单独构成一个NE
    '''
    recognizer = NamedEntityRecognizer()
    recognizer.load(ner_model_path)

    netags = recognizer.recognize(words, pos)
    recognizer.release()
    return list(netags)

def dependency_parsing(words, pos):
    '''
    依存句法分析函数
    @ input: cut_word-->List  pos--> List
    @ output: [(index, relationship)] -->List
      arc.head 表示依存弧的父节点词的索引，arc.relation 表示依存弧的关系。
      pyltp的算法只有一个root节点
    '''
    parser = Parser()
    parser.load(par_model_path)

    arcs = parser.parse(words, pos)
    parser.release()
    return [(arc.head, arc.relation) for arc in arcs]

def extract_news(cut_sents, say_word):
    '''
    @ input: cut_sents-->List,切分的句子； say_word-->List，相近的单词
    @ output : Result --> List 人物及观点
    '''
    result = []
    for index, sentence in enumerate(cut_sents):
        person = ''
        say = ''
        comment = ''
        word = cut_word([sentence])
        postags = word_pos([sentence])
        ner_tag = ner(word, postags)
        parser = dependency_parsing(word, postags)

        if ('S-Nh' in ner_tag) or ('S-Ni' in ner_tag) or ('S-Ns' in ner_tag):
            # 存在命名实体
            # 判断 SBV and say word 是否存在
            for i, p in enumerate(parser):
                if (p[1] == 'SBV') and word[p[0] - 1] in say_word:  # verb 位置 = p[0] -1
                    # 满足主谓， 且包含‘说’
                    person = word[i]
                    say = word[p[0] - 1]
                    if word[p[0]] == '，' or word[p[0]] == ',':
                        comment = ''.join(word[p[0] + 1:])
                    else:
                        comment = ''.join(word[p[0]:])
                else:
                    continue
        else:
            # 不存在命名实体
            continue
        result.append(('对应文中第{}句'.format(index+1), person, say, comment))
    return result



def present_data(string):
    '''
    封装函数
    @ input : string ---> text
    @ output: extractor result including: person, say_word, comment
    '''
    # path = './similar_word/'
    path = basepath + '\\app\\utils\\similar_word\\'
    say_word = load_file(path + 'similar_word_to_say.txt')
    sents = cut_sentence(string)
    res = []
    person_comment = extract_news(sents, say_word)
    for r in person_comment:
        dic1 = {}
        dic1['name'] = r[1]
        dic1['action'] = r[2]
        dic1['words'] = r[3]
        # res[r[1]] = (r[2],r[3],r[0])
        # res[r[1]] =  r[3]
        res.append(dic1)

    return res

if __name__ == '__main__':
    test_string = '''
    特区行政会议当天复会。林郑月娥在出席会议前对传媒表示，过去一星期，大规模恶意破坏行动在香港各区蔓延，包括堵塞铁路、瘫痪机场、围堵过海隧道、攻击各区警署等，使市民出行和上下班受到影响。有人使用汽油弹、烟雾弹等升级武器攻击警务人员，导致
    警员受伤。她指出，一些人以自由或正义的名义，但其实不断做出破坏行为，目无法纪，损害香港法治。小芳表示理解。
    '''
    short_test = '小明表示"这块土地是他承包的。"土地上的苹果也是他的。小芳表示她很认同。小张和小明一起去上学。'
    another_test = '小明表示"这块土地是他承包的。"'

   
   

    print(present_data(test_string))
