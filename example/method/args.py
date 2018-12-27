#!/usr/bin/env python
# -*- coding: utf-8 -*-

def foo(di):
	print('1 : ' + str(di))
	di['c'] = 3
	print('2 : ' + str(di))

if __name__ == '__main__':
	di = {'a':1, 'b':2}
	foo(di)
	print('3 : ' + str(di))
