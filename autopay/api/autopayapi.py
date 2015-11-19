# -*- encode utf-8 -*-
from api_base import RESTClientJSONBase
import requests
import json
from autopay.models.db import User
from autopay import login_manager

api_url = 'http://localhost:7000/api/v1'


class AutopayClient(RESTClientJSONBase):

    def __init__(self, app=None, recipe_id=None):
        super(AutopayClient, self).__init__(None, None)
        self.timeout = 10000
        self.init_app()

    def init_app(self):
        self.api_url = 'http://localhost:7000/api/v1'
    
    def auth_user(self, username, password):
        data = {'username': username,
                'password': password}
        req = requests.get(self.api_url+'/userauth', data=data)
        return json.loads(req.text)

    def get_events_by_org_tag(self, user_id):
        data = {'user_id': user_id}
        req = requests.get(self.api_url+"/event", data=data)
        return json.loads(req.text)

    @login_manager.user_loader
    def load_user(user_id):
        data = {'user_id': user_id}
        registered_user = json.loads(requests.get(api_url+'/user', data=data).text)
        user = User(registered_user['id'], registered_user['name'],
                    registered_user['role'])
        return user

    def get_user_tags(self, user_id):
        data = {'user_id': user_id}
        tags = json.loads(requests.get(api_url+'/tag', data=data).text)

        return tags

    def create_tag(self, user_id, org_id, tag):
        data = {'user_id': user_id,
                'org_id': org_id,
                'tag': tag}
        return json.loads(requests.post(api_url+'/tag', data=data).text)
