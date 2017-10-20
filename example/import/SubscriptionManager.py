import random

class Subscription:
    campaign = []
    date = []
    insurer = []
    center = []
    sc = []

    campaign.append('CAMP1')

    date.append('201706')
    date.append('201707')

    insurer.append('LN')

    center.append('CTR01')
    center.append('CTR02')
    center.append('CTR03')

    for i in range(1, 2):
        sc.append('SSC1')

    for i in range(1, 8):
        sc.append('SSC2')


    def __init__(self):
        pass

    def getLen(self, col):
        if col == 'campaign':
            return len(self.campaign)
        elif col == 'date':
            return len(self.date)
        elif col == 'insurer':
            return len(self.insurer)
        elif col == 'center':
            return len(self.center)
        else:
            return len(self.sc)

    def getRandom(self, col):
        if col == 'campaign':
            rn = random.randrange(0, self.getLen('campaign'))
            rs = self.campaign[rn]
            return rs
        elif col == 'date':
            rn = random.randrange(0, self.getLen('date'))
            rs = self.date[rn]
            return rs
        elif col == 'insurer':
            rn = random.randrange(0, self.getLen('insurer'))
            rs = self.insurer[rn]
            return rs
        elif col == 'center':
            rn = random.randrange(0, self.getLen('center'))
            rs = self.center[rn]
            return rs
        else:
            rn = random.randrange(0, self.getLen('sc'))
            rs = self.sc[rn]
            return rs

