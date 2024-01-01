from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, Boolean, DateTime
from sqlalchemy.orm import relationship
from ProjectCNPM.app import db, app
import enum
from flask_login import UserMixin



class UserRoleEnum(enum.Enum):
    USER = 1
    ADMIN = 2
    EMPLOYEE = 3


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    avatar = Column(String(100),
                    default='https://res.cloudinary.com/dxxwcby8l/image/upload/v1688179242/hclq65mc6so7vdrbp7hz.jpg')
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)
    # receipts = relationship('Receipt', backref='user', lazy=True)

    def __str__(self):
        return self.name


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)




class detail(db.Model):
    __tablename__ = 'detail'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name


if __name__ == '__main__':


    with app.app_context():
        db.create_all()

        import hashlib

        u = User(name='Admin', username='admin',
                 password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
                 user_role=UserRoleEnum.ADMIN)

        e = User(name='Employee', username='employee',
                 password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
                 user_role=UserRoleEnum.EMPLOYEE)

        db.session.add(u)
        db.session.add(e)
        db.session.commit()



        c1 = Category(name='Single room')
        c2 = Category(name='Twin Room')
        c3 = Category(name='Double room')
        c4 = Category(name='VIP room')
        c5 = Category(name='Suite room')
        c6 = Category(name='President room')

        db.session.add(c1)
        db.session.add(c2)
        db.session.add(c3)
        db.session.add(c4)
        db.session.add(c5)
        db.session.add(c6)

        db.session.commit()

        p1 = detail(name='Single room', price=20000000, category_id=1,
                     image='https://res.cloudinary.com/drmkk6w5t/image/upload/v1703686295/single_room_vegkrk.jpg')
        p2 = detail(name='Twin Room', price=22000000, category_id=2,
                     image='https://res.cloudinary.com/drmkk6w5t/image/upload/v1703686296/twin_room_egoszp.jpg')
        p3 = detail(name='Double room', price=35000000, category_id=3,
                     image='https://res.cloudinary.com/drmkk6w5t/image/upload/v1703686300/double_room_nbouxo.jpg')
        p4 = detail(name='VIP room', price=24000000, category_id=4,
                     image='https://res.cloudinary.com/drmkk6w5t/image/upload/v1703686295/VIP_room_p1tdre.jpg')
        p5 = detail(name='Suite room', price=20000000, category_id=5,
                     image='https://res.cloudinary.com/drmkk6w5t/image/upload/v1703768551/suite_room_xri1wv.jpg')
        p6 = detail(name='President room', price=20000000, category_id=6,
                    image='https://res.cloudinary.com/drmkk6w5t/image/upload/v1703686295/president_room_vxsphc.jpg')
        db.session.add_all([p1, p2, p3, p4, p5,p6])
        db.session.commit()
