import os
import json
import datetime
import ast

dictResult = {}

def strToJson(filename, body, datetime):
    # JSON 인코딩
    # customer = {
    #     'id': filename,
    #     'body': body,
    #     'date': datetime
    # }
    # jsonString = json.dumps(customer)

    jsonString = "{{'id':'{0}', 'body':'{1}', 'data':'{2}'}}".format(filename, body, datetime)

    # 문자열 출력
    # print(jsonString)
    # print(type(jsonString))  # class str
    return jsonString


def searchDirFile(dirname):
    dictResult = {}

    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                searchDirFile(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.TXT':
                    f = open(full_filename, 'r', encoding='euc-kr')

                    # text = f.read()
                    lines = f.readlines()
                    text = ','.join(str(s.strip()) for s in lines)

                    # print(text)

                    dictResult[filename] = strToJson(filename, text, datetime.datetime.now().isoformat())
                    f.close()

    except PermissionError:
        pass

    return dictResult

# temp = searchDirFile('/Users/whitexozu/dev/data/richandco')
temp = searchDirFile('/Users/whitexozu/dev/data/temp2')
print(temp)
# temp = ast.literal_eval(temp)
# print(temp)