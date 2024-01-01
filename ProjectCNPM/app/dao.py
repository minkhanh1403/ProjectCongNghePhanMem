from ProjectCNPM.app.models import Category, detail, User
from ProjectCNPM.app import app
import hashlib
from flask_login import current_user


def load_products(kw=None, cate_id=None, page=None):
    products = detail.query

    if kw:
        products = products.filter(detail.name.contains(kw))

    if cate_id:
        products = products.filter(detail.category_id.__eq__(cate_id))

    if page:
        page = int(page)
        page_size = app.config['PAGE_SIZE']
        start = (page - 1) * page_size
        return products.slice(start, start + page_size)

    return products.all()



def load_rooms(checkin=None, checkout=None):
    products = detail.query
    if checkin is not None and checkout is not None:
        products = products.filter((checkin < detail.checkin and checkout < detail.checkin)
                                   and (checkin > detail.checkout and checkout > detail.checkout))
    return products.all()



def get_user_by_id(user_id):
    return User.query.get(user_id)


def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password)).first()



# def load_slides():
#     return Slide.query.all()
