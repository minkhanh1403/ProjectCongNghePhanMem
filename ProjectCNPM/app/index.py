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

<<<<<<< HEAD
@app.route('/')
def index():
    checkin = request.args.get('checkInDate')
    checkout = request.args.get('checkOutDate')
=======

@app.route('/index')
def index():
    return  render_template('index.html')
@app.route('/')
def start():
    return  render_template('index.html')


@app.route('/details')
def details():
    kw = request.args.get('kw')

>>>>>>> 2fc5ee3e7533aa421ba2b927e249e9562f1fc04f
    cates = dao.load_categories()
    kw = request.args.get('kw')
    products = dao.load_products(kw=kw)
<<<<<<< HEAD
    room = dao.load_rooms(checkin=checkin, checkout=checkout)
    return  render_template('index.html', cate=cates, product=products, room=room)
=======
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
>>>>>>> 2fc5ee3e7533aa421ba2b927e249e9562f1fc04f


@app.route('/booking')
def booking():
    return render_template('booking.html')


if __name__ == '__main__':
    from ProjectCNPM.app import admin #minh
    app.run(debug=True)


