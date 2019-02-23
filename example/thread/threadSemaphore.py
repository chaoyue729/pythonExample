import threading

sem = threading.Semaphore(3)      # 세마포 객체 생성, 3개의 쓰레드로 제한

class RestrictedArea(threading.Thread):
    def run(self):
        for x in range(500):
            msg = 'Threading Semaphore TEST : %s' % self.getName()
            sem.acquire()
            print(msg)                  # 3개의 쓰레드만이 존재할수 있는 영역
            sem.release()

threads = []

for i in range(100):
    threads.append(RestrictedArea())

for th in threads:
    th.start()          # 쓰레드 시작

for th in threads:
    th.join()           # 종료대기

print('Finish All Threading')
