# -*- encode utf-8 -*-
from flask import Blueprint, render_template, request, abort, json, flash, redirect, url_for
from autopay.api.autopayapi import AutopayClient
from autopay.models.db import User
from flask.ext.login import login_user, logout_user, current_user, login_required

tags = Blueprint('tag', __name__, template_folder='templates')
client = AutopayClient()


@tags.route('/tags', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        tags = client.get_user_tags(current_user.id)
        return render_template('tags/index.html', title='Tags', tags=tags)

    org_id = request.form['orgid']
    tag = request.form['tag']
    client.create_tag(current_user.id, org_id, tag)
    tags = client.get_user_tags(current_user.id)
    return redirect(request.referrer)

