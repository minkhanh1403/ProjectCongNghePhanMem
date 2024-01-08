from flask import render_template, request, redirect, jsonify, session
from flask_login import login_user, logout_user, login_required
import dao, utils
from ProjectCNPM.app import app, login




@app.route('/')
def start():
    return render_template('index.html')


@app.route('/show', methods =['get'])
def check_room():
    checkin = request.form.get('checkInDate')
    checkout = request.form.get('checkOutDate')
    room = dao.load_rooms(checkin=checkin, checkout=checkout)
    return  render_template('index.html', room=room,checkin = checkin)


@app.route('/Product')
def product():
    kw = request.args.get('kw')
    products = dao.load_products(kw=kw)

    return render_template('Product.html', product=products)


@app.route("/login", methods=['get', 'post'])
def process_user_login():
    if request.method.__eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user=user)

        next = request.args.get('net')
        return redirect("/" if next is None else next)

    return render_template('login.html')


@app.route('/logout')
def process_logout_user():
    logout_user()
    return redirect("/login")


@app.route('/admin/login', methods=['post'])
def admin_login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = dao.auth_user_admin(username=username, password=password)
    if user:
        login_user(user=user)

    return redirect('/admin')


@app.route('/employee/login', methods=['post'])
def employee_login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = dao.auth_user_employee(username=username, password=password)
    if user:
        login_user(user=user)
    else:
        return redirect('/employee')

    return render_template('index_employee.html')

@app.route('/employee')
def employee_login_process():
    return render_template('loginemployee.html')


@app.route('/user/login', methods=['post'])
def user_login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = dao.auth_user(username=username, password=password)
    if user:
        login_user(user=user)
    else:
        return redirect('/user')

    return redirect('/')



@app.route('/user')
def user_login_process():
    return render_template('index_user.html')


@app.route('/products/<id>')
def details(id):
    comments = dao.get_comments_by_prod_id(id)
    return render_template('details.html', product=dao.get_product_by_id(id), comments=comments)


@app.route('/api/products/<id>/comments', methods=['post'])
@login_required
def add_comment(id):
    content = request.json.get('content')

    try:
        c = dao.add_comment(product_id=id, content=content)
    except:
        return jsonify({'status': 500, 'err_msg': 'Hệ thống đang có lỗi!'})
    else:

        return jsonify({'status': 200, "c": {'content': c.content, "user": {"avatar": c.user.avatar}}})


@app.route('/signup', methods=['get', 'post'])
def signup_user():
    err_msg = ""
    if request.method.__eq__('POST'):
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        email = request.form.get('email')
        if password.__eq__(confirm):
            try:
                dao.add_user(name=request.form.get('name'),
                             username=request.form.get('username'),
                             password=password,
                             email=email,
                             avatar=request.files.get('avatar'))
            except:
                err_msg = 'Hệ thống đang bị lỗi!'
            else:
                return redirect('/login')
        else:
            err_msg = 'Mật khẩu KHÔNG khớp!'

    return render_template('signup.html', err_msg=err_msg)


@app.route('/employee/manageroom')
def manageroom():
    return render_template('manageroom.html')


@app.route('/employee/available')
def available():
    products = dao.load_available_products()
    return render_template('manageroom.html',product=products)

@app.route('/employee/notavailable')
def notavailable():
    products = dao.load_notavailable_products()
    return render_template('manageroom.html',product=products)


@app.route('/employee/customerif')
def loadcustomer():
    customers = dao.load_customer()
    return render_template('managecustomer.html',customer=customers)

@app.route('/employee/manageroomif', methods =['get','post'])
def receipt():
    booking = dao.load_booking()
    return render_template('manageroomif.html',booking = booking)


@app.route('/employee/pay',methods =['get','post'])
def pay():
     price = request.form.get('price')
     roomid = request.form.get('roomid')
     customerid = request.form.get('customerid')
     dao.add_receipt(customerid = customerid, price = price, product_id = roomid)
     return redirect("/employee")

@app.route('/history')
def history():
    return render_template('history.html')


@app.route('/api/cart', methods=['post'])
def add_cart():
    """
    {
    "cart": {
            "1": {
                "id": 1,
                "name": "ABC",
                "price": 12,
                "quantity": 2
            }, "2": {
                "id": 2,
                "name": "ABC",
                "price": 12,
                "quantity": 2
            }
        }
    }
    :return:
    """
    cart = session.get('cart')
    if cart is None:
        cart = {}

    data = request.json
    id = str(data.get("id"))

    if id in cart: # san pham da co trong gio
        cart[id]["quantity"] = cart[id]["quantity"] + 1
    else: # san pham chua co trong gio
        cart[id] = {
            "id": id,
            "name": data.get("name"),
            "price": data.get("price"),
            "quantity": 1
        }

    session['cart'] = cart

    return jsonify(utils.count_cart(cart))


@app.route('/booking', methods=['get', 'post'])
def booking():
    err_msg = ""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        checkin = request.form.get('checkin')
        checkout = request.form.get('checkout')
        roomtype = request.form.get('roomtype')
        comments = request.form.get('comments')
        # try:
        dao.add_booking(name=name, email=email, phone=phone, roomtype=roomtype, comments=comments
                            ,checkin=checkin, checkout=checkout)
        return render_template('index.html')
        # except Exception as ex:
        #     err_msg = 'Hệ thống đang bị lỗi!'

    return render_template('booking.html')


@app.route('/forgot', methods=['get', 'post'])
def forgot():
    err_msg = ""
    if request.method == 'POST':
        email = request.form.get('email')
        user = dao.auth_email(email=email)
        if user:
            password = dao.new_password(user)

    return render_template('forgot.html')


@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    from ProjectCNPM.app import admin  # minh

    app.run(debug=True)
