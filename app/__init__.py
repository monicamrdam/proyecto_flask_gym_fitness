from flask import Flask
from flask_migrate import Migrate
from app.models import db
from app.init_db import fill_users
from config import Config

app = Flask(__name__, static_url_path='/static')
app.app_context().push()
app.config.from_object(Config)
db.init_app(app)
db.drop_all()
db.create_all()
# Fill DB
fill_users()

migrate = Migrate(app, db)

from app import routes