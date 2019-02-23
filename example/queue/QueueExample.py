'''
https://sarangyik.tistory.com/entry/Pythonmodule-queue
'''

import queue

def GetItemList(q):
    ret=[]
    n=q.qsize()
    while n > 0:
        ret.append(q.get())
        n -= 1
    return ret

l='apple,banana,orange'

# Queue
q=queue.Queue()
for x in l.split(','):
    q.put(x)
print(GetItemList(q))

# LifoQueue
q=queue.LifoQueue()
for x in l.split(','):
    q.put(x)
print(GetItemList(q))

# PriorityQueue
q=queue.PriorityQueue()
q.put((5,'apple'))
q.put((10,'banana'))
q.put((1,'orange'))
print(GetItemList(q)) #인자로 전달된 우선순위대로 출력

# wait
q=queue.Queue(2) #아이템이 2개만 저장가능하도록 설정
q.put('a')
q.put('b') #큐의 저장 한계
# q.put('c') #다른 스레드가 아이템을 가지고 갈때까지 무한 대기

# put_nowait
q=queue.Queue(2)
try:
    q.put_nowait('a')
    q.put_nowait('b')
    q.put_nowait('c') #큐 객체가 꽉찬 경우
except queue.Full as e:
    print(e)

# get_nowait
q=queue.Queue(2)
try:
    q.get_nowait()
    q.get_nowait()
    q.get_nowait() #큐 객체가 빈 경우
except queue.Empty as e:
    print(e)