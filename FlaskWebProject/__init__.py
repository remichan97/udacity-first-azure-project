"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
import FlaskWebProject.filehandler

app = Flask(__name__)
app.config.from_object(Config)
app.logger.setLevel(logging.WARNING)
streamHandler = logging.StreamHandler()
app.logger.addHandler(streamHandler)
Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'
storage = FlaskWebProject.filehandler.Storage(Config.STORAGE_CONNECTION_STRING, "images")

import FlaskWebProject.views
