from flask import request, jsonify
from app.api import bp
from app.database.models import News
from flask import current_app


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
    opinions = [
            {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
            {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
            {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
            {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
            {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
            {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
            {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
            {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"}
        ]

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
    opinions = [
        {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
        {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
        {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
        {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
        {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
        {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
        {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"},
        {"name": "张三", "action": "说", "words": "可是当减肥了看时间的"}
    ]

    resp = {
        "news": content,
        "opinions": opinions
    }
    return jsonify(resp)
