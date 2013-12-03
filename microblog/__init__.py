import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from microblog import settings
from settings import basedir
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(settings)
db = SQLAlchemy(app)

lm = LoginManager()
lm.setup_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))


from microblog import views, models