from flask import Blueprint, flash, render_template, request, session, abort, \
                  redirect, url_for
from app.base import database

mod_phones = Blueprint('phones', __name__, url_prefix='/phones')


@mod_phones.route('/', methods=['GET'])
def index():
    db = database.Database()
    data = db.read(None)
    print(data)
    dic = data[1]
    print(dic)
    print(dic['name'])
    return render_template('phones/index.html', data=data)


@mod_phones.route('/add/', methods=['GET'])
def add():
    return render_template('phones/add.html')


@mod_phones.route('/addphone/', methods=['POST'])
def addphone():
    req = request.form

    name = req['name']
    phone = req['phone']
    address = req['address']
    print(name)
    print(phone)
    print(address)
    return redirect('/phones/')


@mod_phones.route('/update/<int:id>/', methods=['GET', 'POST'])
def update():
    return render_template('phones/update.html')


@mod_phones.route('/delete/')
def delete():
    return render_template('phones/delete.html')
