#!/usr/bin/env python

import argparse
import requests

from config import config
import auth


def send_message(message, authorization, group=config.group, channel=config.default_channel):
    url = f'https://graph.microsoft.com/v1.0/teams/{group}/channels/{channel}/messages'
    headers = {
        'Authorization': f'{authorization.token_type} {authorization.access_token}',
    }
    data = {
        'body': { 'content': message }
    }
    r = requests.post(url, headers=headers, json=data)
    if r.status_code == 201:
        return { 'ok': True  }
    else:
        return { 'ok': False, 'message': r.text  }
