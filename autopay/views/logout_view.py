# -*- encode utf-8 -*-
from flask import Blueprint, render_template, request, abort, json, flash, redirect, url_for
from flask.ext.login import login_user, logout_user, current_user, login_required

logout = Blueprint('logout', __name__, template_folder='templates')


@logout.route('/logout', methods=['GET', 'POST'])
def logout_user_route():
    logout_user()
    return redirect(url_for('main.index'))
