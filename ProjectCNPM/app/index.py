from flask import render_template, request
import dao
from ProjectCNPM.app import app

@app.route('/')
def index():
    checkin = request.args.get('checkInDate')
    checkout = request.args.get('checkOutDate')
    cates = dao.load_categories()
    kw = request.args.get('kw')
    products = dao.load_products(kw=kw)
    room = dao.load_rooms(checkin=checkin, checkout=checkout)
    return  render_template('index.html', cate=cates, product=products, room=room)

@app.route('/details')
def details():
    return render_template('details.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')


if __name__ == '__main__':
    app.run(debug=True)


