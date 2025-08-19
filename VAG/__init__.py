from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_fontawesome import FontAwesome
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)
FontAwesome(app)

app.config['SECRET_KEY'] =  '1e38c0543f25816fefb7fee8a51282ac3e9189af86ae707a7d787627ebc3b3bcv'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///VAG.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
bcrypt = Bcrypt()
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
from VAG import routes
