from functools import singledispatch

@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print('Let me just say,', end=' ')
    print(arg)

@fun.register(int)
def _(arg, verbose=False):
    if verbose:
        print('Strength in numbers, eh?', end=' ')
    print(arg)

@fun.register(float)
def _(arg, verbose=False):
    if verbose:
        print('Half of your number:', end=' ')
    print(arg / 2)

@fun.register(type(None))
def _(arg):
    print('Nothing.')

"""
python 은 기본적으로 함수의 overloading 을 지원하지 않는다.
(컴파일을 하지 않으니 어찌 보면 당연한 이야기..)

다만 런타임에 타입을 구분하는 방법을 응용한 여러 가지 솔루션이 존재하는 듯하며
python3.4 이후 부터는 singledispatch 라는 것을 지원한다.
(말 그대로 첫 번째 인자의 타입을 보고 판단한다.)

>>> fun('1', verbose=True)
Let me just say, 1

>>> fun(1, verbose=True)
Strength in numbers, eh? 1

>>> fun(1.0, verbose=True)
Half of your number: 0.5

>>> fun(None)
Nothing.
"""

fun('1', verbose=True)
fun(1, verbose=True)
fun(1.0, verbose=True)
fun(None)