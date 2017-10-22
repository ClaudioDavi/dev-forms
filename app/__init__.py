from flask import Flask
from flask_mail import Mail
from .config import config

app = Flask(__name__)
app.config.from_object(config['prod'])
mail = Mail(app)
from app import views, models
