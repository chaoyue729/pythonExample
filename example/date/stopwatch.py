import time
import datetime
import json
from bson import json_util
from sys import exit

class stopWatch:
    def __init__(self):
        self.timer = []
        
    def start(self, name=''):
        self.timer.append({'name': name, 'sTime': datetime.datetime.now()})

    def stop(self, name=''):
        it = [t for t in self.timer if t['name'] == name][0]
        it['eTime'] = datetime.datetime.now()
        it['tTime'] = it['eTime'] - it['sTime']
    
    def getTotalTime(self, name=''):
        it = [t for t in self.timer if t['name'] == name][0]
        return it['tTime']

    def getTotalReport(self):
        for t in self.timer:
            t['sTime'] = t['sTime'].strftime('%Y-%m-%d %H:%M:%S')
            t['eTime'] = t['eTime'].strftime('%Y-%m-%d %H:%M:%S')
            t['tTime'] = t['tTime'].total_seconds()
        return self.timer

    def prettyPrint(self):
        st = sum([t['tTime'].total_seconds() for t in self.timer])
        print('{0}\t\t\t{1}\t\t\t{2}'.format('ms', '%', 'Task name'))
        print('==================================================================')
        for t in self.timer:
            print('{0}\t\t\t{1:.2f}%\t\t\t{2}'.format(t['tTime'], (t['tTime'].total_seconds() / st * 100), t['name']))

if __name__ == '__main__':
    sw = stopWatch()

    # 측정결과 평군값 구하기
    div = []    # 측정 데이터 저장 list
    temp = datetime.timedelta(0)    # 측정 합을 위한 변수
    print(temp)
    # 전체 측정
    sw.start()
    # B 측정
    sw.start('B')
    time.sleep(1)
    sw.stop('B')
    print(sw.getTotalTime('B'))
    div.append(sw.getTotalTime('B'))
    # A 측정
    sw.start('A')
    time.sleep(1)
    sw.stop('A')
    print(sw.getTotalTime('A'))
    div.append(sw.getTotalTime('A'))
    sw.stop()
    print(sw.getTotalTime())
    div.append(sw.getTotalTime())
    # 평군 구하기
    for t in div:
        print(t)
        temp += t
    dTime = temp / len(div)
    print(dTime.total_seconds())
    print(str(dTime))
    # exit()

    # # 측정결과 출력
    # sw.start('B')
    # time.sleep(1)
    # sw.stop('B')
    # sw.prettyPrint()

    # # 측정결과 전체 구하기
    # print(sw.getTotalReport)
    # for t in sw.getTotalReport():
    #     print(t)

    # # 측정 데이터 직접 입력 (기다리는 시간을 줄이기 위해)
    # t1 = datetime.datetime.now()
    # t2 = datetime.datetime.now().replace(minute=20)
    # print(t1)
    # print(t2)
    # print(t2.timestamp())
    # t3 = t2 - t1
    # print(t3)
    # print(t3.total_seconds())
    # exit()

    # # 다른 방법의 시간 측정
    # st = time.time()
    # time.sleep(1) 
    # et = time.time()
    # print(st, et, et - st)
    # print(datetime.datetime.now())

    # # datetime.datetime formrat 변경
    # t1 = datetime.datetime.now()
    # time.sleep(1)
    # t2 = datetime.datetime.now()
    # t3 = t2 - t1
    # print(t1.strftime('%Y-%m-%d %H:%M:%S'))
    # print(t2.strftime('%Y-%m-%d %H:%M:%S'))
    # print(t3)