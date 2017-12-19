import threading
from time import sleep, ctime

loops = [8,2]

def loop(nloop,nsec):
    print 'start loop', nloop, 'at:',ctime()
    sleep(nsec)
    print 'loop', nloop, 'at:', ctime()


def test() :
    print 'starting at:', ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop,args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print 'all Done at: ', ctime()

if  __name__ == '__main__' :
   test()
