import os
from pathlib import Path

import wtforms_json
from flask import Flask
from flask_cors import CORS
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from dotenv import load_dotenv

envvars = Path().cwd() / '.env.local'
load_dotenv()

if os.path.exists(envvars):
    load_dotenv(envvars, override=True, verbose=True)

app = Flask('app')
app.debug = os.environ.get("DEBUG")
app.secret_key = os.environ.get("JWT_KEY")
wtforms_json.init()

toolbar = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
print(os.environ.get("DATABASE_URL"))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# csrf_protect = CSRFProtect(app)

cors = CORS(app, resources={'/api/*': {'origins': os.environ.get("CORS_ORIGIN")}})
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.controllers import *
from app.models import *
