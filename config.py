import json
from types import SimpleNamespace

with open('config.json') as _f:
    config = SimpleNamespace(**json.load(_f))
