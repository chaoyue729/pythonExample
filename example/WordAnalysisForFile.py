import CallTextManager
import SubscriptionManager
import CustomerManager
import random
import time

if __name__ == "__main__":
    start = time.time()

    callDataFile = open("/Users/whitexozu/dev/data/test/python/callDataFile", 'w')
    subscriptionDataFile = open("/Users/whitexozu/dev/data/test/python/subscriptionDataFile", 'w')
    customerDataFile = open("/Users/whitexozu/dev/data/test/python/customerDataFile", 'w')

    colSep = '^'
    arrSep = ','
    newLine = '\n'

    dAlp = 'D'
    cAlp = 'C'

    callMaxCount = 600000

    # call text data 생성
    ct = CallTextManager.CallText()
    for i in range(1, callMaxCount):
        did = dAlp + '%07d' % i;
        callDataFile.write(did + colSep + ct.getRandomStt() + newLine)

    cs = SubscriptionManager.Subscription()
    for i in range(1, callMaxCount):
        did = dAlp + '%07d' % i;
        cid = cAlp + '%07d' % i;
        subscriptionDataFile.write(did + colSep + cid + colSep + cs.getRandom('campaign') + colSep + cs.getRandom('date') + colSep + cs.getRandom('insurer') + colSep + cs.getRandom('center') + colSep + cs.getRandom('sc') + newLine)

    cc = CustomerManager.Customer()
    for i in range(1, callMaxCount):
        cid = cAlp + '%07d' % i;
        customerDataFile.write(cid + colSep + cc.getRandom('age') + colSep + cc.getRandom('gender') + colSep + cc.getRandom('area') + newLine)

    callDataFile.close()
    subscriptionDataFile.close()
    customerDataFile.close()

    end = time.time() - start
    print(end)