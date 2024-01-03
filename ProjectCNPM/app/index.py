from flask import render_template, request, redirect
from flask_login import login_user
import dao
from ProjectCNPM.app import app, login


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/')
def start():
    checkin = request.form.get('checkInDate')
    checkout = request.form.get('checkOutDate')
    room = dao.load_rooms(checkin=checkin, checkout=checkout)
    # kw = request.args.get('kw')
    # products = dao.load_products(kw=kw)
    return render_template('index.html', room=room)


@app.route('/details')
def details():
    kw = request.args.get('kw')
    products = dao.load_products(kw=kw)
    return render_template('details.html',  product=products)

@app.route("/login")
def process_user_login():
    # if request.method.__eq__('POST'):
    #     username = request.form.get('username')
    #     password = request.form.get('password')
    #     user = dao.auth_user(username=username, password=password)
    #     if user:
    #         login_user(user=user)
    #
    #     next = request.args.get('net')
    #     return redirect("/" if next is None else next)

    return render_template('login.html')


@app.route('/admin/login', methods=['post'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user=user)

    return redirect('/admin')


@app.route('/employee/login', methods=['post'])
def employee_login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user=user)

    return redirect('/employee')

@app.route('/employee')
def employee_login_process():
    return render_template('index_employee.html')


@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)

    # slides = dao.load_slides()

@app.route('/booking', methods=['get', 'post'])
def booking():
    if request.method == 'POST':
        name = request.args.get('name')
        email = request.args.get('email')
        phone = request.args.get('phone')
        roomtype = request.args.get('roomtype')
        comments = request.args.get('comments')
        dao.add_booking(name=name,email=email,phone=phone,roomtype=roomtype,comments=comments)
        return render_template('index.html')

    return render_template('booking.html')


if __name__ == '__main__':
    from ProjectCNPM.app import admin #minh
    app.run(debug=True)


