import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import random
from flask import render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'user.login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

from app.people.routes import people
from app.posts.routes import posts
from app.main.routes import main

def quote():
    dict = {1:{'author':'Ngugidavid', 'title':'authords'},
            2:{'author':'Ngugidavid2', 'title':'authords2'}}
    res=key, val=random.choice(list(dict.items()))
    author=str(val['author'])
    render_template("quotes.html", author1="author1")

app.register_blueprint(people)
app.register_blueprint(posts)
app.register_blueprint(main)
