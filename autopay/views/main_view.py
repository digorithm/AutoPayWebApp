# -*- encode utf-8 -*-
from flask import Blueprint, render_template, request, abort, json
from autopay.api.autopayapi import AutopayClient
from flask.ext.login import login_user, logout_user, current_user, login_required

main = Blueprint('main', __name__, template_folder='templates')
fast_food = AutopayClient()


@main.route('/', methods=['GET', 'POST'])
@main.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('main/index.html', title='Home')
