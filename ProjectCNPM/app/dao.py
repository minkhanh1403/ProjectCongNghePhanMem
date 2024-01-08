import cloudinary.uploader
from ProjectCNPM.app.models import Category, Product, User, Comment, Customer, Booking, Receipt, ReceiptDetails
from ProjectCNPM.app import app, db
import hashlib
import random
from flask_login import current_user
from sqlalchemy import func

def load_products(kw=None, cate_id=None, page=None):
    products = Product.query

    if kw:
        products = products.filter(Product.name.contains(kw))

    if cate_id:
        products = products.filter(Product.category_id.__eq__(cate_id))

    if page:
        page = int(page)
        page_size = app.config['PAGE_SIZE']
        start = (page - 1) * page_size
        return products.slice(start, start + page_size)

    return products.all()


def load_customer():
    customer = Customer.query
    if customer:
        return customer.all()


def load_available_products(active=False):
    products = Product.query
    if products:
        products = products.filter(Product.active.__eq__(active))

    return products.all()


def load_notavailable_products(active=True):
    products = Product.query
    if products:
        products = products.filter(Product.active.__eq__(active))

    return products.all()


def load_rooms(checkin=None, checkout=None):
    booking = Booking.query
    product = Product.query
    if checkin is not None and checkout is not None:
        if booking.filter((checkin < booking.checkin and checkout < booking.checkin)
                          or (checkin > booking.checkout and checkout > booking.checkout)):
            return booking.all()

    if booking:
        product = Product.query.filter(Product.id.__eq__(booking.id))

    return product.all()


def add_booking(name, email, phone, roomtype, comments, checkin, checkout):
    # u = User.query.filter(User.id.eq(current_user))
    if roomtype == 'singleroom':
        roomid = 1
        price=20000000
    elif roomtype == 'twinroom':
        roomid = 2
        price=22000000
    elif roomtype == 'doubleroom':
        roomid = 3
        price=35000000
    elif roomtype == 'viproom':
        roomid = 4
        price=24000000
    elif roomtype == 'suiteroom':
        roomid = 5
        price=20000000
    else:
        roomid = 6
        price=20000000

    b = Booking(name=name,
                roomtype=roomtype,
                email=email,
                phone=phone,
                comments=comments,
                checkin=checkin,
                checkout=checkout,
                price=price,
                roomid=roomid,
                customerid=current_user.get_id())
    db.session.add(b)
    db.session.commit()


def load_booking():
    booking = Booking.query
    if booking:
        return booking.all()


def add_receipt(customerid, price, product_id):
    r = Receipt(customerid)
    db.session.add(r)
    d = ReceiptDetails(price=price,
                       receip_id=r, product_id=product_id)
    db.session.add(d)
    db.session.commit()


def new_password(user):
    user.password = [random.randint(0, 9) for _ in range(6)]
    return user.password


def get_user_by_id(user_id):
    return User.query.get(user_id)


def auth_user_admin(username, password, user_role='ADMIN'):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password),
                             User.user_role.__eq__(user_role)).first()


def auth_user_employee(username, password, user_role='EMPLOYEE'):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password),
                             User.user_role.__eq__(user_role)).first()


def auth_user(username, password, user_role='USER'):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password),
                             User.user_role.__eq__(user_role)).first()


def add_user(name, username, password,email, avatar):
    password = str(hashlib.md5(password.strip().encode('utf8')).hexdigest())
    u = User(name=name, username=username, password=password,email=email)
    if avatar:
        res = cloudinary.uploader.upload(avatar)
        print(res)
        u.avatar = res['secure_url']

    db.session.add(u)
    db.session.commit()


def get_comments_by_prod_id(id):
    return Comment.query.filter(Comment.product_id.__eq__(id)).all()


def get_product_by_id(id):
    return Product.query.get(id)

def count_products_by_cate():
    return db.session.query(Category.id, Category.name, func.count(Product.id))\
                     .join(Product, Product.category_id == Category.id, isouter=True).group_by(Category.id).all()
def revenue_stats(kw=None):
    query = db.session.query(Product.id, Product.name, func.sum(ReceiptDetails.price))\
                     .join(ReceiptDetails, ReceiptDetails.product_id == Product.id).group_by(Product.id)
    if kw:
        query = query.filter(Product.name.contains(kw))

    return query

def revenue_stats_by_month(year=2024):
    return db.session.query(func.extract('month', Receipt.created_date),
                            func.sum(ReceiptDetails.price))\
                        .join(ReceiptDetails, ReceiptDetails.receipt_id == Receipt.id)\
                        .filter(func.extract('year', Receipt.created_date) == year)\
                        .group_by(func.extract('month', Receipt.created_date)).all()

def add_comment(product_id, content):
    c = Comment(user=current_user, product_id=product_id, content=content)
    db.session.add(c)
    db.session.commit()

    return c

# def load_slides():
#     return Slide.query.all()

if __name__ == '__main__':
    with app.app_context():
        print(count_products_by_cate())
# def load_slides():
#     return Slide.query.all()
