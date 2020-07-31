#!/usr/bin/env python

import json
import requests
from types import SimpleNamespace

def login(config):
    url = f'https://login.microsoftonline.com/{config.tenant_id}/oauth2/v2.0/token'
    payload = {
        'client_id': config.app_id,
        'grant_type': 'password',
        'username': config.email,
        'password': config.password,
        'scope': 'ChannelMessage.Send user.read openid profile offline_access',
        'client_secret': config.client_secret
    }

    r = requests.post(url, data=payload)

    if r.status_code == 200:
        data = r.json()
        return SimpleNamespace(token_type=data['token_type'], access_token=data['access_token'])
    else:
        return False
