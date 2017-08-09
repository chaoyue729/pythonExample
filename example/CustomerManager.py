import random

class Customer:
    area = []
    gender = []
    age = []

    area.append('SD11')
    area.append('SD21')
    area.append('SD22')
    area.append('SD23')
    area.append('SD24')
    area.append('SD25')
    area.append('SD26')
    area.append('SD29')
    area.append('SD31')
    area.append('SD32')
    area.append('SD33')
    area.append('SD34')
    area.append('SD35')
    area.append('SD36')
    area.append('SD37')
    area.append('SD38')
    area.append('SD39')

    gender.append('GENDER01')
    gender.append('GENDER02')

    age.append('AGE20')
    age.append('AGE30')
    age.append('AGE40')
    age.append('AGE50')
    age.append('AGE60')
    age.append('AGE99')

    def __init__(self):
        pass

    def getLen(self, col):
        if col == 'area':
            return len(self.area)
        elif col == 'gender':
            return len(self.gender)
        else:
            return len(self.age)

    def getRandom(self, col):
        if col == 'area':
            rn = random.randrange(0, self.getLen('area'))
            rs = self.area[rn]
            return rs
        elif col == 'gender':
            rn = random.randrange(0, self.getLen('gender'))
            rs = self.gender[rn]
            return rs
        else:
            rn = random.randrange(0, self.getLen('age'))
            rs = self.age[rn]
            return rs


