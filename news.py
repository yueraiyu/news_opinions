from flask import request, jsonify
from app.api import bp
from app.database.models import News
from flask import current_app
from app.utils.extract_algorithm import present_data

@bp.route('/news', methods=['GET'])
def search():
    '''返回新闻集合，分页'''
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    search_value = request.args.get('search_value', '', type=str)
    data = News.to_collection_dict(News.query.filter(News.content.like("%" + search_value + "%")),
                                   search_value, page, per_page, 'api.search')
    return jsonify(data)


@bp.route('/news/<int:id>', methods=['GET'])
def content(id):
    '''返回一条新闻'''
    return jsonify(News.query.get_or_404(id).to_detail())


@bp.route('/news/analyze/<int:id>', methods=['GET'])
def analyze(id):
    '''根据新闻ID解析'''
    news = News.query.get_or_404(id)
    current_app.logger.info("analyze news content {%s}", news.content)

    # todo 调用正式解析函数获得正式返回
    # opinions = [
    #         {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
    #         {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
    #         {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
    #         {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
    #         {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
    #         {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
    #         {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
    #         {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"}
    #     ]
    opinions = present_data(news.content)
    resp = {
        "news": news.to_detail(),
        "opinions": opinions
    }
    return jsonify(resp)


@bp.route('/news/analyze', methods=['POST'])
def analyze_txt():
    '''根据文本解析'''
    content = request.args.get('content', '', type=str)
    current_app.logger.info("analyze content {%s}", content)

    # todo 调用正式解析函数获得正式返回
    # opinions = [
    #     {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
    #     {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
    #     {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
    #     {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
    #     {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
    #     {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
    #     {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
    #     {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"}
    # ]
    opinions = present_data(content)
    resp = {
        "news": content,
        "opinions": opinions
    }
    return jsonify(resp)


test_string = '''
    特区行政会议当天复会。林郑月娥在出席会议前对传媒表示，过去一星期，大规模恶意破坏行动在香港各区蔓延，包括堵塞铁路、瘫痪机场、围堵过海隧道、攻击各区警署等，使市民出行和上下班受到影响。有人使用汽油弹、烟雾弹等升级武器攻击警务人员，导致
    警员受伤。她指出，一些人以自由或正义的名义，但其实不断做出破坏行为，目无法纪，损害香港法治。小芳表示理解。
    '''
print(present_data(test_string))
