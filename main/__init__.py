from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth

from settings import config

app = Flask('Vista_test')
auth = HTTPBasicAuth()

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = b'my_super_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{config["database"].get("login")}:{config["database"].get("password")}@{config["database"].get("host")}:{config["database"].get("port")}/{config["database"].get("database_name")}?charset=utf8mb4'

db = SQLAlchemy(app)

import notebook_app
