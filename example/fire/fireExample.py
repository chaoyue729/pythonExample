import fire

class Calculator(object):

    def add(self, x, y):
        return x + y

    def multiply(self, x, y):
        return x * y

if __name__ == '__main__':
    fire.Fire(Calculator)

'''
$ python fireExample.py add 10 20
30
$ python fireExample.py multiply 10 20
200

https://github.com/google/python-fire/blob/master/docs/guide.md
'''