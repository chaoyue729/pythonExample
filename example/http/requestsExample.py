import requests
import time
import datetime

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S%f')
st = '20171117134617329718'

URL = 'http://localhost:8080/TA_SKM/ta/openApi/insertMntrLog.do'
data = {'jobId': st, 'key': 'IV', 'type': 'M', 'state': 'E', 'serviceKey': 'b7a9dce1-9a39-4382-8b94-910220b5'}
res = requests.post(URL, data=data)
print(res.status_code)
print(res.text)

