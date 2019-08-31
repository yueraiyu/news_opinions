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
    opinions = present_data(news.content)
    current_app.logger.info("analyze opinions {%s}", opinions)
    resp = {
        "news": news.to_detail(),
        "opinions": opinions
    }
    return jsonify(resp)


@bp.route('/news/analyze', methods=['POST'])
def analyze_txt():
    '''根据文本解析'''
    data = request.get_json()
    content = data.get('content', None)
    current_app.logger.info("analyze content {%s}", content)
    opinions = present_data(content)
    current_app.logger.info("analyze opinions {%s}", opinions)
    resp = {
        "news": content,
        "opinions": opinions
    }
    return jsonify(resp)
