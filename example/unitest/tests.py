import unittest
import myCalc

class MyCalcTest(unittest.TestCase):

    def test_add(self):
        c = myCalc.add(20, 10)
        self.assertEqual(c, 30)

    def test_substract(self):
        c = myCalc.substract(20, 10)
        self.assertEqual(c, 10)

if __name__ == '__main__':
    '''
    1. 먼저 unittest 모듈을 import 한 후,
    2. "unittest.TestCase"로부터 파생된 사용자 테스트 클래스를 만든다.
    3. 테스트 클래스 안에 "test" 로 시작하는 테스트 메서드를 생성한다. 테스드 메서드에서는 일반적으로 테스트하고자 하는 함수나 메서드를 호출하고 그 결과값을 self.assert*() 메서드를 사용하여 확인한다 (assertEqual, assertTrue, assertFalse, assertRaises, assertRegex 등 다양한 assert 메서들을 사용할 수 있다).
    4. 테스트 클래스가 완성되었으면, unittest.main()을 호출하여 테스트를 실행시킨다.
        $ python teste.py

    참고 : http://pythonstudy.xyz/python/article/21-%EC%9C%A0%EB%8B%9B-%ED%85%8C%EC%8A%A4%ED%8A%B8
    '''
    unittest.main()
