import requests

URL = 'http://localhost:8080/TA_SKM/common/selectCommonCodeList.do'
params = {'param1': 'value1', 'param2': 'value'}
res = requests.get(URL, params=params)
print(res.status_code)
print(res.text)

data = {'param1': 'value1', 'param2': 'value'}
res = requests.post(URL, data=data)
print(res.status_code)
print(res.text)

