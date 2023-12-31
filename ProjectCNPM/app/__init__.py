from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import cloudinary


app = Flask(__name__)

<<<<<<< HEAD
app.secret_key = 'GHFGH&*%^$^*(JHFGHF&Y*R%^$%$^&*TGYGJHFHGVJHGY' #minh
app.config["SQLALCHEMY_DATABASE_URI"] ='mysql+pymysql://root:%s@localhost/saledbv1?charset=utf8mb4' % quote('23082002')
=======

<<<<<<< HEAD
app.config["SQLALCHEMY_DATABASE_URI"] ='mysql+pymysql://root:%s@localhost/saledbv1?charset=utf8mb4' % quote('Admin@123')
=======
app.config["SQLALCHEMY_DATABASE_URI"] ='mysql+pymysql://root:%s@localhost/saledbv1?charset=utf8mb4' % quote('Minhhuy2003@')
>>>>>>> df15d6d16bd57f13e543e1eb10febf652c7eb702
>>>>>>> 2fc5ee3e7533aa421ba2b927e249e9562f1fc04f
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 6


db = SQLAlchemy(app=app)
login = LoginManager(app=app)


cloudinary.config(
    cloud_name="drmkk6w5t",
    api_key="885974914618116",
    api_secret="kFcVOl_dt9Ewa1tcXPn-jzH9dMg"
)
