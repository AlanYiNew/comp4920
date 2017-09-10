from server import db
from bson.objectid import ObjectId
import datetime
import json
import uuid


class Serializable(json.JSONEncoder):
    def serialize(self):
        return json.dumps(self.__dict__)


class User(db.Document):
    username = db.StringField(unique=True, required=True, max_length=20)
    password = db.StringField(required=True, max_length=20)
    time = db.DateTimeField(default=datetime.datetime.now())
    status = db.IntField(default=0)
    _id = db.StringField(default=uuid.uuid4().hex,primary_key=True);

