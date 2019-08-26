# -*- coding:utf-8 -*-
from gensim.models import Word2Vec
from collections import defaultdict


def get_related_words(init_words, model):
    unseen = init_words
    seen = defaultdict(int)
    max_size = 500

    while unseen and len(seen) < max_size:
        # if len(seen) % 50 == 0:
        #     print('seen length : {0}'.format(len(seen)))
        node = unseen.pop(0)
        new_expanding = [w for w, _ in model.wv.most_similar(node, topn=20)]
        unseen += new_expanding
        seen[node] += 1
        # 这里可以优化，利用 A* search or heuristic search
        # 加上Dynamic Programming
    return seen


def get_say(say=['说', '表示', '认为']):
    news_model = Word2Vec.load("../word2vec_model/news_content_wv")
    related_word = get_related_words(say, news_model)
    say = sorted(related_word.items(), key=lambda x: x[1], reverse=True)[:30]
    say = [i[0] for i in say]
    return say


def save_to_file():
    say = get_say()
    say = ','.join(say)
    with open('similar_word_to_say.txt', 'w') as f:
        f.write(say)
    print('Done')


def load_file(filename):
    '''
    :param filename:
    :return: string -> say word
    '''
    if filename:
        with open(filename, 'r') as f:
            string = f.readlines()
            string = string[0].split(',')
            return string


if __name__ == '__main__':
    # save_to_file()

    # print(get_say())

    # string = load_file('similar_word_to_say.txt')
    # print(string, '\n', len(string))
    news_model = Word2Vec.load("../word2vec_model/news_content_wv")
    print(news_model.wv.most_similar('说', topn=20))
