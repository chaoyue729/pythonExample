import random

class Subscription:
    sc = []

    sc.append('SSC1')
    for i in range(1, 55):
        sc.append('SSC2')


    def __init__(self):
        pass

    def getLen(self):
        return len(self.sc)

    def getRandomSsc(self):
        rn = random.randrange(0, self.getLen())
        rSc = self.sc[rn]
        return rSc

