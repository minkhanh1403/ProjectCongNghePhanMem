

def load_categories():
    return[{
        'id ': 1,
        'name':'Mobile'
    },{
        'id ': 2,
        'name':'Tablet'
    }]


def load_products(kw=None):
    products = [{
        'id':1,
        'name':'ipad 02 promax',
        'price':2000000,
        'image':"https://www.apple.com/newsroom/images/2023/09/apple-debuts-iphone-15-and-iphone-15-plus/article/Apple-iPhone-15-lineup-hero-230912_inline.jpg.large.jpg"
    },{
        'id':2,
        'name':'iphone 15 promax',
        'price':2000000,
        'image':"https://www.apple.com/newsroom/images/2023/09/apple-debuts-iphone-15-and-iphone-15-plus/article/Apple-iPhone-15-lineup-hero-230912_inline.jpg.large.jpg"
    },{
        'id':1,
        'name':'iphone 15 promax',
        'price':2000000,
        'image':"https://www.apple.com/newsroom/images/2023/09/apple-debuts-iphone-15-and-iphone-15-plus/article/Apple-iPhone-15-lineup-hero-230912_inline.jpg.large.jpg"
    },{
        'id':1,
        'name':'iphone 15 promax',
        'price':2000000,
        'image':"https://www.apple.com/newsroom/images/2023/09/apple-debuts-iphone-15-and-iphone-15-plus/article/Apple-iPhone-15-lineup-hero-230912_inline.jpg.large.jpg"
    },{
        'id':1,
        'name':'iphone 15 promax',
        'price':2000000,
        'image':"https://www.apple.com/newsroom/images/2023/09/apple-debuts-iphone-15-and-iphone-15-plus/article/Apple-iPhone-15-lineup-hero-230912_inline.jpg.large.jpg"
    }]

    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]

    return products
