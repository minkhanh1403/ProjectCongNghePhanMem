from ProjectCNPM.app.models import Category, detail
from ProjectCNPM.app import app

def load_categories():
    return[{
        'id ': 1,
        'name':'Mobile'
    },{
        'id ': 2,
        'name':'Tablet'
    }]

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



