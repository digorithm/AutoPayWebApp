# -*- encode utf-8 -*-
from flask import Blueprint, render_template, request, abort, json
from autopay.api.autopayapi import AutopayClient
from flask.ext.login import login_user, logout_user, current_user, login_required

historico = Blueprint('historico', __name__, template_folder='templates')
api = AutopayClient()


@historico.route('/', methods=['GET', 'POST'])
@historico.route('/historico', methods=['GET', 'POST'])
@login_required
def index():
    events = api.get_events_by_org_tag(current_user.id)
    return render_template('historico/index.html', title='Home', events=events)
