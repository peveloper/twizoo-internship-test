from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask_modus import Modus
app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "test"}
app.config["SECRET_KEY"] = "secretpassword"
modus = Modus(app)
db = MongoEngine(app)
from app import views

