import pandas as pd
import os
import json
from sys import exit

# # csv to excel 
# df = pd.read_csv('callWordCsv1.txt', sep='|', index_col=None) # can replace with df = pd.read_table('input.txt') for '\t'
# df.to_excel('output.xlsx', 'Sheet1')


# list to excel
# sales = [{'account': 'Jones LLC', 'Jan': 150, 'Feb': 200, 'Mar': 140},
#          {'account': 'Alpha Co',  'Jan': 200, 'Feb': 210, 'Mar': 215},
#          {'account': 'Blue Inc',  'Jan': 50,  'Feb': 90,  'Mar': 95 }]
# df = pd.DataFrame(sales)
# print(df)
# df.to_excel('output.xlsx', 'Sheet1')


# json file to excel
sales = []
testFileDir = '/Users/whitexozu/dev/project/lgu+/data/callHst/20190221'
fileNames = os.listdir(testFileDir)
for fileIdx, fileName in enumerate(fileNames):
    fullFileName = os.path.join(testFileDir, fileName)
    ext = os.path.splitext(fullFileName)[-1]
    # baseName = os.path.splitext(fileName)[0]
    if ext == '.json':
        # print(fullFileName)
        f = open(fullFileName, 'r', encoding='utf-8')
        while True:
            line = f.readline()
            if not line: break
            j = json.loads(line)
            for p in j['pending']:
                for o in p['prcLog']:
                    if o['name'] == 'scrt':
                        temp = {'uid': '', 'state': '', 'type': '', 'secod': 0}
                        temp['uid'] = o['uid']
                        temp['state'] = 'pending'
                        temp['type'] = '스크립크 검사'
                        temp['secod'] = o['tTime']
                        sales.append(temp)

            # for p in j['pending']:
            #     for o in p['prcLog']:
            #         if o['name'] == 'kwd':
            #             temp = {'uid': '', 'state': '', 'type': '', 'secod': 0}
            #             temp['uid'] = o['uid']
            #             temp['state'] = 'pending'
            #             temp['type'] = '민원 키워드 검사'
            #             temp['secod'] = o['tTime']
            #             sales.append(temp)

            # for p in j['finish']:
            #     for o in p['prcLog']:
            #         if o['name'] == 'cslType':
            #             temp = {'uid': '', 'state': '', 'type': '', 'secod': 0}
            #             temp['uid'] = o['uid']
            #             temp['state'] = 'finish'
            #             temp['type'] = '분류'
            #             temp['secod'] = o['tTime']
            #             sales.append(temp)

            # for p in j['finish']:
            #     for o in p['prcLog']:
            #         if o['name'] == 'smrz':
            #             temp = {'uid': '', 'state': '', 'type': '', 'secod': 0}
            #             temp['uid'] = o['uid']
            #             temp['state'] = 'finish'
            #             temp['type'] = '요약'
            #             temp['secod'] = o['tTime']
            #             sales.append(temp)

            # for p in j['finish']:
            #     for o in p['prcLog']:
            #         if o['name'] == 'cpltDtt':
            #             temp = {'uid': '', 'state': '', 'type': '', 'secod': 0}
            #             temp['uid'] = o['uid']
            #             temp['state'] = 'finish'
            #             temp['type'] = '민원 감지'
            #             temp['secod'] = o['tTime']
            #             sales.append(temp)
df = pd.DataFrame(sales)
print(df)
df.to_excel('output.xlsx', 'Sheet1', columns=['uid', 'state', 'type', 'secod'])
