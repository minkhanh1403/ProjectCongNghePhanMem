from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
import cloudinary


app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] ='mysql+pymysql://root:%s@localhost/saledbv1?charset=utf8mb4' % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 6


db = SQLAlchemy(app=app)



cloudinary.config(
    cloud_name="drmkk6w5t",
    api_key="885974914618116",
    api_secret="kFcVOl_dt9Ewa1tcXPn-jzH9dMg"
)