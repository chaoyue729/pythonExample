'''
http://avilos.codes/programming/python/python-thread/
'''
# Threading 상속클래스 및 LOCK객체를 이용한 Thread간 상호 배제 잠금(뮤텍스) 1
import threading

g_count = 0

class MutexThread(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
    def run(self):
        global g_count      # 클래스 외부에 선언되어 있는 Global 변수접근 선언
        for i in range(20):
            lock.acquire()      # Thread접근시 Lock 획득
            # print('thred', i, ' : ', g_count)
            g_count += 1        # Thread가 거의 동시에 접근해도 Lock을 걸고 원자적으로 연산
            lock.release()      # Thread접근 완료후 Lock 해제(이후 다른 Thread가 접근)



""" Entry Point """
if __name__ == '__main__':
    lock = threading.Lock()         # Thread 접근시 뮤텍스에 필요한 Lock객체 생성
    threadArr = []

    for i in range(10):             # Thread 객체 10개 생성 및 배열에 저장(한 쓰레드당 20을 더하므로 10개의 쓰레드가 작업하여 200 데이터가 나온다)
        thread = MutexThread(i)
        thread.start()              # Thread 클래스는 start 호출시 클래스 내부에 run() 함수가 자동실행
        threadArr.append(thread)    # Thread 배열에 저장

    for thread in threadArr:
        thread.join()               # 다른 Thread가 모든 종료되기를 대기


    print('All threads finished : ', g_count)