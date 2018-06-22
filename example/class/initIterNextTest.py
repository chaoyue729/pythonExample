# -*- coding: utf-8 -*-

class Range:
    def __init__(self, n):
        self.n = n
        self.c = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.c < self.n:
            v = self.c
            self.c += 2
            return v
        else:
            raise StopIteration
    next = __next__
for x in Range(7):
    print(x)