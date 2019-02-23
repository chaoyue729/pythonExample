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