# -*- encode utf-8 -*-
from flask import Blueprint, render_template, request, abort, json, flash, redirect, url_for
from autopay.api.autopayapi import AutopayClient
from autopay.models.db import User
from flask.ext.login import login_user, logout_user, current_user, login_required

login = Blueprint('login', __name__, template_folder='templates')
fast_food = AutopayClient()
client = AutopayClient()


@login.route('/login', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('login/index.html', title='Home')

    username = request.form['username']
    password = request.form['password']
    registered_user = client.auth_user(username, password)

    if registered_user is None:
        flash('Username or Password is invalid', 'error')
        return redirect(url_for('login'))

    user = User(registered_user['id'], registered_user['name'],
                registered_user['organization'], registered_user['role'],
                registered_user['rfid'])

    login_user(user)
    flash('Logged in successfully')
    return redirect(request.args.get('next') or url_for('main.index'))
