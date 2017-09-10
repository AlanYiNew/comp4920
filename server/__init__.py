from flask import Flask
from flasgger import Swagger

from flask_mongoengine import MongoEngine


app = Flask(__name__,instance_relative_config=True)
app.config.from_object('config.default')
app.config.from_pyfile('config.py')

db = MongoEngine(app)

from server.user.controllers import user
# blueprint register
app.register_blueprint(user, url_prefix='/user')



# swagger
swagger = Swagger(app)
# app.config.from_envvar('APP_CONFIG_FILE')