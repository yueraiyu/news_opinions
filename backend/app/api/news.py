from flask import request, jsonify
from app.api import bp
from app.database.models import News


@bp.route('/news', methods=['GET'])
def search():
    '''返回新闻集合，分页'''
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = News.to_collection_dict(News.query, page, per_page, 'api.search')
    return jsonify(data)


@bp.route('/news/<int:id>', methods=['GET'])
def content(id):
    '''返回一条新闻'''
    return jsonify(News.query.get_or_404(id).to_dict())
