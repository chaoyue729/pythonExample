# from __future__ import print_function
# f1=open('./testfile', 'w+')
# print >>f1, 'This is a test'
# print >>f1, 'This is a test2'
# print >>f1, '333333'

with open('./out.txt', 'w') as f:
    print >> f, 'Filename:', 'aaaa'
    print >> f, 'Filename: 111111'
    print >> f, 'Filename: 222222'
