import CallTextManager
import SubscriptionManager
import random

if __name__ == "__main__":
    callDataFile = open("/Users/whitexozu/dev/data/test/python/callDataFile", 'w')
    subscriptionDataFile = open("/Users/whitexozu/dev/data/test/python/subscriptionDataFile", 'w')
    customerDataFile = open("/Users/whitexozu/dev/data/test/python/customerDataFile", 'w')

    colSep = '^'
    arrSep = ','
    newLine = '\n'

    dAlp = 'D'
    cAlp = 'C'

    callMaxCount = 21

    # call text data 생성
    ct = CallTextManager.CallText()
    for i in range(1, callMaxCount):
        did = dAlp + '%07d' % i;
        callDataFile.write(did + colSep + ct.getRandomStt() + newLine)

    cs = SubscriptionManager.Subscription()
    for i in range(1, callMaxCount):
        did = dAlp + '%07d' % i;
        cid = cAlp + '%07d' % i;
        subscriptionDataFile.write(did + colSep + cid + colSep + cs.getRandomSsc() + newLine)

    callDataFile.close()
    subscriptionDataFile.close()
    customerDataFile.close()

