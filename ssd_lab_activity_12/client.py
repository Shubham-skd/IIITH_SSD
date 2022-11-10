from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import (LoginManager,login_manager,login_user,logout_user,login_required,UserMixin)

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///ssdlast13/ssd lab 12/user.db'
app.config['SECRET_KEY']='secretkey'
db=SQLAlchemy(app)
login_manager=LoginManager()
login_manager.init_app(app)
class user(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=False, nullable=False)
    password = db.Column(db.String(20), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.ge(int(user_id))
@app.route("/Hello")
def get_hello():
    return "Hello World"
if"__main__"==__name__:
    app.run(host="127.0.0.1",port="5000",debug="True")