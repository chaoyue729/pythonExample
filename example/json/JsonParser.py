#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
from sys import exit

baseDir = os.path.dirname(os.path.abspath(__file__))

f = open(baseDir + '/' + 'test.json', 'r', encoding='euc-kr')
line = f.read()

print(type(line))
print(line)

customer = {
    'type': 'data',
    'id': '0',
    'body': 'abcde',
    'date': '2018-05-30T13:34:56.978807',
    'hangul': '한글'
}

# dict to str
s = json.dumps(customer)

# str to dict
j = json.loads(s)

with open(baseDir + '/' + 'test.json', 'w') as fp:
	# fp.write(j) #exception
	# fp.write(s)
    fp.write(json.dumps(customer, ensure_ascii=False))