import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.app_context().push()

app_settings = os.getenv(
    'APP_SETTINGS',
    'project.server.config.DevelopmentConfig'
)
app.config.from_object(app_settings)

db = SQLAlchemy(app)

from project.server.endpoints.auth_usr.reg_usr import auth_blueprint

app.register_blueprint(auth_blueprint)