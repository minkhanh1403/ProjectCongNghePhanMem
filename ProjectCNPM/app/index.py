from flask import render_template, request
import dao
from ProjectCNPM.app import app


@app.route('/')
def index():
    kw = request.args.get('kw')

    cates = dao.load_categories()
    products = dao.load_products(kw=kw)
    # slides = dao.load_slides()
    return  render_template('index.html',cate = cates, product=products)

@app.route('/details')
def details():
    return render_template('details.html')

if __name__ == '__main__':
    app.run(debug=True)


