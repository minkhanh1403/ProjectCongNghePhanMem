<<<<<<< HEAD
from flask import render_template, request, redirect, session, jsonify
import dao
from ProjectCNPM.app import app, login
from flask_login import login_user
=======
from flask import render_template, request
import dao
from ProjectCNPM.app import app
>>>>>>> df15d6d16bd57f13e543e1eb10febf652c7eb702


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
<<<<<<< HEAD

    return render_template('details.html', cate=cates, product=products)

@app.route("/login")
def process_user_login():
    return render_template('login.html')

@app.route('/admin/login', methods=['post'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user=user)

    return redirect('/admin')

@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)
=======
    # slides = dao.load_slides()
    return  render_template('index.html',cate = cates, product=products)
>>>>>>> df15d6d16bd57f13e543e1eb10febf652c7eb702


if __name__ == '__main__':
    from ProjectCNPM.app import admin #minh
    app.run(debug=True)


