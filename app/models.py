from datetime import datetime
from flask.ext.mongoengine import mongoengine
from mongoengine import *


class Blogger(Document):
    screen_name = StringField(max_length=255)


class Dictionary(Document):
    type = StringField(max_length=255)
    word = StringField(max_length=255)
    data = IntField()
    addtime = DateTimeField(default=datetime.now)
