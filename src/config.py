import json

with open('../config.json') as _f:
    data = json.load(_f)

for k, v in data.items():
    exec(f'{k}=v')

del data, k, v
