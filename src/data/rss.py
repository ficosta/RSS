import mongoengine
import datetime


class Item(mongoengine.Document):
    publisher = mongoengine.StringField(required=True)
    section = mongoengine.StringField(required=True)
    title = mongoengine.StringField(required=True)
    language = mongoengine.StringField(required=True)
    link = mongoengine.URLField(required=False)
    mediaUrl = mongoengine.URLField(required=False)
    timestamp = mongoengine.DateTimeField(required=True, default=datetime.datetime.now)

    meta = {
        'db_alias': 'core',
        'collection': 'rss'
    }