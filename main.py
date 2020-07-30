#!/usr/bin/env python

from config import config
from auth import login
from sendmessage import send_message


msg = 'Segundo teste'
response = login(config)
if response != False:
    r = send_message(msg, response)
    print(r)
