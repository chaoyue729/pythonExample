#-*- coding: utf-8 -*-
import re
import requests
import time
import datetime
import json

# URL = 'http://localhost:8080/TA_SKM/ta/openApi/selectBatchDt.do'
# data = {'stateCd': 'S', 'serviceKey': 'b7a9dce1-9a39-4382-8b94-910220b5'}
# res = requests.post(URL, data=data)
# data = json.loads(res.text)
# print("batchDt={0}".format(data['batchDt']))

mor = []
URL = 'http://localhost:28080/nlp'
data = {'sttText': u'5시 30분기상 쉬다가 로스트아크  취침 10시에 일어나서 씻고 다이퀘스트 출근 5시 30분 퇴근'}
res = requests.get(URL, params=data)
temp = res.text
ms = re.findall('[\S]+', temp)
for m in ms:
    pos = re.findall('\w+', m)
    # print(pos)
    mor.append(tuple(pos))

print(mor)



    