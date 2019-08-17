from app import db
from flask import url_for


class Pagination(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **kwargs):
        resources = query.paginate(page, per_page, False)
        data = {
            'items': [item.to_dict() for item in resources.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resources.pages,
                'total_items': resources.total
            },
            '_links': {
                'self': url_for(endpoint, page=page, per_page=per_page,
                                **kwargs),
                'next': url_for(endpoint, page=page + 1, per_page=per_page,
                                **kwargs) if resources.has_next else None,
                'prev': url_for(endpoint, page=page - 1, per_page=per_page,
                                **kwargs) if resources.has_prev else None
            }
        }
        return data


class News(Pagination, db.Model):
    __tablename__ = "news_chinese"

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(32))
    source = db.Column(db.String(32))
    content = db.Column(db.String(1000))
    feature = db.Column(db.String(256))
    title = db.Column(db.String(32))
    url = db.Column(db.String(32))

    def to_dict(self):
        data = {
            'id': self.id,
            'author': self.author,
            'source': self.source,
            'content': "        " + self.content[:150].replace("\\n", "") + "...",# 前端展示没必要显示全部内容，减少不要流量开销
            'feature': self.feature,
            'title': self.title,
            'url': self.url,
            '_links': {
                'self': url_for('api.search', id=self.id)
            }
        }

        return data

    def from_dict(self, data):
        for field in data.item():
            setattr(self, field, data[field])
