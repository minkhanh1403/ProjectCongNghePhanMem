from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.testing.pickleable import User
# <<<<<<< HEAD
from datetime import datetime
# =======
# >>>>>>> 082d9d2436d96c5384187d9317800bc9a5b59d42
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
    email = Column(String(100), nullable=False)
    avatar = Column(String(100),
                    default='https://t4.ftcdn.net/jpg/02/29/75/83/360_F_229758328_7x8jwCwjtBMmC6rgFzLFhZoEpLobB6L8.jpg')
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)

    # receipts = relationship('Receipt', backref='user', lazy=True)
    comments = relationship('Comment', backref='user', lazy=True)
    def __str__(self):
        return self.name

# <<<<<<< HEAD

class Customer(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    phone = Column(Integer, nullable=False)
    booking = relationship('Booking', backref='customer', lazy=True)
    def __str__(self):
        return self.name


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_date = Column(DateTime, default=datetime.now())
    active = Column(Boolean, default=True)
# =======
# >>>>>>> 082d9d2436d96c5384187d9317800bc9a5b59d42

class Category(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)


class Product(db.Model):
    __tablename__ = 'Product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    active = Column(Boolean, default=True, nullable=False)
    roomdetail = relationship('Room_detail', backref='product', lazy=True)
    comments = relationship('Comment', backref='Product', lazy=True)
    booking = relationship('Booking', backref='product', lazy=True)
    def __str__(self):
        return self.name

# <<<<<<< HEAD
class Room_detail(db.Model):
    _tablename_ = 'RoomDetails'
    id = Column(Integer, primary_key=True, autoincrement=True)
    price  = Column(Integer, nullable=False)
    maxpeople = Column(Integer, nullable=False)
    detail_id = Column(Integer, ForeignKey(Product.id), nullable=False)

class Booking(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    roomtype  = Column(String(50),nullable=False)
    email = Column(String(50), nullable=False)
    phone = Column(Integer, nullable=False)
    checkin = Column(DateTime)
    checkout = Column(DateTime)
    price = Column(Integer, nullable=False)
    comments = Column(String(300))
    roomid = Column(Integer, ForeignKey(Product.id), nullable=False)
    customerid = Column(Integer, ForeignKey(Customer.id), nullable=False)


class Interaction(BaseModel):
    __abstract__ = True

    product_id = Column(Integer, ForeignKey(Product.id), nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)


class Comment(Interaction):
    content = Column(String(255), nullable=False)
    created_date = Column(DateTime, default=datetime.now())


class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_date = Column(DateTime, default=datetime.now())
    active = Column(Boolean, default=True)


class Receipt(BaseModel):
    customerid = Column(Integer, ForeignKey(User.id), nullable=False)
    receipt_details = relationship('ReceiptDetails', backref='receipt', lazy=True)


class ReceiptDetails(BaseModel):
    price = Column(Float, default=0)
    receipt_id = Column(Integer, ForeignKey(Receipt.id), nullable=False)
    product_id = Column(Integer, ForeignKey(Product.id), nullable=False)

# =======


# >>>>>>> 082d9d2436d96c5384187d9317800bc9a5b59d42


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

# <<<<<<< HEAD
#
        import hashlib

        u = User(name='Admin', username='admin',
                 password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),email='admin@gmail.com',
                 user_role=UserRoleEnum.ADMIN)

        e = User(name='Employee', username='employee',
                 password=str(hashlib.md5('123'.encode('utf-8')).hexdigest()),email='minhkhanh14032003@gmail.com',
                 user_role=UserRoleEnum.EMPLOYEE)

        a = User(name='test', username='test',
                 password=str(hashlib.md5('123'.encode('utf-8')).hexdigest()),email='minhkhanh14032004@gmail.com',
                 user_role=UserRoleEnum.USER)
        db.session.add(a)
        db.session.add(u)
        db.session.add(e)
        db.session.commit()
        a1 = User(name='user2', username='user2',
                          password=str(hashlib.md5('123'.encode('utf-8')).hexdigest()),email='admin1@gmail.com',
                          user_role=UserRoleEnum.USER)
        a2 = User(name='user3', username='user3',
                  password=str(hashlib.md5('123'.encode('utf-8')).hexdigest()),email='admin2@gmail.com',
                  user_role=UserRoleEnum.USER)
        a3 = User(name='user4', username='user4',
                  password=str(hashlib.md5('123'.encode('utf-8')).hexdigest()),email='admin3@gmail.com',
                  user_role=UserRoleEnum.USER)
        db.session.add(a1)
        db.session.add(a2)
        db.session.add(a3)
        db.session.commit()
        c1 = Category(name='Single room')
        c2 = Category(name='Twin Room')
        c3 = Category(name='Double room')
        c4 = Category(name='VIP room')
        c5 = Category(name='Suit room')
        c6 = Category(name='President room')


        db.session.add(c1)
        db.session.add(c2)
        db.session.add(c3)
        db.session.add(c4)
        db.session.add(c5)
        db.session.add(c6)
        db.session.commit()

        p1 = Product(name='Single room', price=20000000, category_id=1,
                    image='https://res.cloudinary.com/drmkk6w5t/image/upload/v1703686295/single_room_vegkrk.jpg')
        p2 = Product(name='Twin Room', price=22000000, category_id=2,
                    image='https://res.cloudinary.com/drmkk6w5t/image/upload/v1703686296/twin_room_egoszp.jpg', active = False)
        p3 = Product(name='Double room', price=35000000, category_id=3,
                    image='https://res.cloudinary.com/drmkk6w5t/image/upload/v1703686300/double_room_nbouxo.jpg')
        p4 = Product(name='VIP room', price=24000000, category_id=4,
                    image='https://res.cloudinary.com/drmkk6w5t/image/upload/v1703686295/VIP_room_p1tdre.jpg')
        p5 = Product(name='Suit room', price=20000000, category_id=5,
                    image='https://res.cloudinary.com/drmkk6w5t/image/upload/v1703768551/suite_room_xri1wv.jpg')
        p6 = Product(name='President room', price=20000000, category_id=6,
                    image='https://res.cloudinary.com/drmkk6w5t/image/upload/v1703686295/president_room_vxsphc.jpg')

        db.session.add_all([p1, p2, p3, p4, p5, p6])

        d1 = Room_detail(price = 2000, maxpeople = 2, detail_id=1)
        d2 = Room_detail(price = 3000, maxpeople = 3, detail_id=2)
        d3 = Room_detail(price = 4000, maxpeople = 4, detail_id=3)
        d4 = Room_detail(price = 5000, maxpeople = 5, detail_id=4)
        d5 = Room_detail(price = 6000, maxpeople = 6, detail_id=5)
        d6 = Room_detail(price = 7000, maxpeople = 7, detail_id=6)

        m1= Customer(name='Nguyen Tran Minh Khanh',email='minhkhanh1@gmail.com', phone = '0325994934')
        m2 = Customer(name='Nguyen Tran Minh Khoa', email='minhkhanh2@gmail.com', phone='0325994935')
        m3 = Customer(name='Nguyen Tran Minh Huy', email='minhkhanh3@gmail.com', phone='0325994936')

        b1 = Booking(name='Nguyen Tran Minh Khanh',roomtype ='Single Room',email='minhkhanh1@gmail.com', phone = '0325994934',
                     checkin='2023-12-25', checkout='2023-12-26',price = 2000000,comments = 'sjadnak',roomid = 1,customerid=1 )
        b2 = Booking(name='Nguyen Tran Minh Khoa',roomtype ='Single Room', email='minhkhanh2@gmail.com', phone='0325994936',
                     checkin='2023-11-30', checkout='2023-12-4',price = 2000000, comments='sjadnak', roomid=2, customerid=2)
        b3 = Booking(name='Nguyen Tran Minh Huy',roomtype ='Single Room', email='minhkhanh3@gmail.com', phone='0325994935',
                     checkin='2023-12-21', checkout='2023-12-30',price = 2000000, comments='sjadnak', roomid=3, customerid=3)

        db.session.add_all([d1, d2, d3, d4, d5, d6,m1,m2,m3])
        db.session.add_all([b1, b2, b3])
        db.session.commit()

        r1 = Receipt(customerid=1)
        r2 = Receipt(customerid=2)
        r3 = Receipt(customerid=3)

        s1 = ReceiptDetails(price =20000,receipt_id = 1, product_id=1 )
        s2 = ReceiptDetails(price=30000, receipt_id=2, product_id=2)
        s3 = ReceiptDetails(price=40000, receipt_id=3, product_id=3)

        db.session.add_all([r1,r2,r3,s1, s2, s3])
        db.session.commit()
# =======
        # import hashlib
        #
        # u = User(name='Admin', username='admin',
        #          password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()),
        #          user_role=UserRoleEnum.ADMIN)
        # db.session.add(u)
        # db.session.commit()
        #
        #
        # c1 = Category(name='Single room')
        # c2 = Category(name='Twin Room')
        # c3 = Category(name='Double room')
        # c4 = Category(name='VIP room')
        # c5 = Category(name='President room')
        # c6 = Category(name='President room')
        #
        #
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.add(c3)
        # db.session.add(c4)
        # db.session.add(c5)
        #
        # db.session.commit()
        #
        #
        # p1 = detail(name='Single room', price=20000000, category_id=1, checkin='2023-12-25', checkout='2023-12-26',
        #              image='https://res.cloudinary.com/drmkk6w5t/image/upload/v1703686295/single_room_vegkrk.jpg')
        # p2 = detail(name='Twin Room', price=22000000, category_id=1, checkin='2023-12-27', checkout='2023-12-28',
        #              image='https://res.cloudinary.com/drmkk6w5t/image/upload/v1703686296/twin_room_egoszp.jpg')
        # p3 = detail(name='Double room', price=35000000, category_id=2, checkin='2023-12-28', checkout='2023-12-29',
        #              image='https://res.cloudinary.com/drmkk6w5t/image/upload/v1703686300/double_room_nbouxo.jpg')
        # p4 = detail(name='VIP room', price=24000000, category_id=2, checkin='2023-12-19', checkout='2023-12-20',
        #              image='https://res.cloudinary.com/drmkk6w5t/image/upload/v1703686295/VIP_room_p1tdre.jpg')
        # p5 = detail(name='President room', price=20000000, category_id=1, checkin='2023-12-21', checkout='2023-12-22',
        #              image='https://res.cloudinary.com/drmkk6w5t/image/upload/v1703686295/president_room_vxsphc.jpg')
        #
        # db.session.add_all([p1, p2, p3, p4, p5])
        # db.session.commit()
        # db.session.add(c6)
        #
        # db.session.commit()

        # b1 = Booking(name='Ngyen Van A', email='adcs@gmail.com', phone='0978544544', roomtype='Double room',
        #              comments='adsdasdasd')
        # db.session.add(b1)
        # db.session.commit()
# >>>>>>> 082d9d2436d96c5384187d9317800bc9a5b59d42
