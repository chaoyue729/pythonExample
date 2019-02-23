import datetime, json 
def json_default(value):
    # if isinstance(value, datetime.date):
        # return value.strftime('%Y-%m-%d')
    return 'AAA'
    # raise TypeError('not JSON serializable')
data = {'date': datetime.date.today()}
json_data = json.dumps(data, ensure_ascii=False, default=json_default)
print(json_data)