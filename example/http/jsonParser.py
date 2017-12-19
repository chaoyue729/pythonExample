import requests
import time
import datetime
import json

URL = 'http://localhost:8080/TA_SKM/ta/openApi/selectBatchDt.do'
data = {'stateCd': 'S', 'serviceKey': 'b7a9dce1-9a39-4382-8b94-910220b5'}
res = requests.post(URL, data=data)
data = json.loads(res.text)
print("batchDt={0}".format(data['batchDt']))
