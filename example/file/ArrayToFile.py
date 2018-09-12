#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import random

def main():
    print('{0}'.format('1'))
    n=10
    size = 1500
    initial = numpy.zeros([n,3], dtype=numpy.float64)
    print('{0}'.format(initial))
    filename = './initialpositions.txt'
    for i in range(n):
        for j in range(0,3):
            initial[i,j]=random.randrange(0,size)
    file = open(filename,'w')
    file.write(initial)
    file.close()

if __name__ == '__main__':
    main()
