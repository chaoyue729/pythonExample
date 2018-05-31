import json

f = open("/Users/whitexozu/dev/data/temp2/20180320_6534942175750352489.TXT", 'r', encoding='euc-kr')
line = f.read()

# print(line)

customer = {
    'type': 'data',
    'id': '0',
    'body': line,
    'date': '2018-05-30T13:34:56.978807'
}

msg = json.dumps(customer)

print(json.loads(msg))