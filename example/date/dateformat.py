import time
import datetime
import timeit
from datetime import timedelta

# datetime format 지정
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S%f')
print(st)

# datetime 시간 지정
myDatetime = datetime.datetime.strptime('2015-04-15 12:23:38', '%Y-%m-%d %H:%M:%S')
print(myDatetime)   # 2015-04-15 12:23:38
yourDatetime = myDatetime.replace(day=16)
print(myDatetime)   # 2015-04-15 12:23:38
print(yourDatetime) # 2015-04-16 12:23:38


# 초단위 시간 비교
t1 = datetime.datetime.now()
t2 = datetime.datetime.now()
t3 = t2 - t1
print(t3.seconds)

t4 = datetime.datetime.strptime('2015-04-15 12:23:38', '%Y-%m-%d %H:%M:%S')
t5 = datetime.datetime.strptime('2015-04-15 12:23:48', '%Y-%m-%d %H:%M:%S')
print((t5-t4).seconds)

# 참고
# https://docs.python.org/3/library/datetime.html
# https://godoftyping.wordpress.com/2015/04/19/python-%EB%82%A0%EC%A7%9C-%EC%8B%9C%EA%B0%84%EA%B4%80%EB%A0%A8-%EB%AA%A8%EB%93%88/