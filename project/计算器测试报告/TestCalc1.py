'''
    单元测试框架：
        unittest
    1.子类继承TestCase类


    2.测试方法必须test开头。testxxxx

'''

from unittest import TestCase
from Calc import Calc


class TestCalc(TestCase):  # TestCalc是测试体系中的一员

    def testAdd1(self):
        a = 6
        b = 5
        c = 1

        calc = Calc()
        s = calc.minus(a, b)

        self.assertEqual(s, c)

    def testAdd2(self):
        a = -6
        b = -5
        c = -1

        calc = Calc()
        s = calc.minus(a, b)

        self.assertEqual(s, c)

    def testAdd3(self):
        a = -6
        b = 5
        c = -11

        calc = Calc()
        s = calc.minus(a, b)

        self.assertEqual(s, c)

    def testAdd4(self):
        a = 6
        b = -5
        c = 11

        calc = Calc()
        s = calc.minus(a, b)

        self.assertEqual(s, c)

