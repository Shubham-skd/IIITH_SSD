from flask import Flask, request, redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.debug = True
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
 
# Creating an SQLAlchemy instance
db = SQLAlchemy(app)
 
# Models
class Profile(db.Model):
   
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=False, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
 
    def __repr__(self):
        return f"Name : {self.first_name}, Age: {self.age}"
@app.route('/do_signin',method=['POST'])
def do_sigin():
    if(request.method=='POST'):
        req=request.get_json()
        username=req['username']
        password=req['password']
        check_user=User.query.filter_by(username=username).first()
        if(check_user is not None):
            login_user(check_user)
            return "LOGIN SUCCESSFULL"
        else:
            return "Incorrect password"
    else:
        return "No such user exists"
        

db.create_all()
if __name__ == '__main__':
    app.run()
