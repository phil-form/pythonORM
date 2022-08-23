from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

app = Flask('app')
app.debug = True
app.secret_key = 'superSecretKey01@'

toolbar = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://app:1234@127.0.0.1:5435/app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
csrf_protect = CSRFProtect(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.controllers import *
from app.models import *
