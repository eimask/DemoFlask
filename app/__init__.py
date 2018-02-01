from flask import Flask, render_template, url_for, redirect
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')

app.config.from_object('config')

from app.mod_phones.controllers import mod_phones as phones_module

app.register_blueprint(phones_module)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')
