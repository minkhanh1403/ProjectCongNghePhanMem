from flask import render_template, request
import  dao
from ProjectCNPM.app import app


@app.route('/index')
def index():
    return  render_template('index.html')
@app.route('/')
def start():
    return  render_template('index.html')


@app.route('/details')
def details():
    kw = request.args.get('kw')

    cates = dao.load_categories()
    products = dao.load_products(kw=kw)

    return render_template('details.html', cate=cates, product=products)
if __name__ == '__main__':
    app.run(debug=True)


