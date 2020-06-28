# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert sol.calculate(' ') == 0
    assert sol.calculate('2') == 2
    assert sol.calculate('1+2') == 3
    assert sol.calculate('2*3') == 6
    assert sol.calculate('2*(1+3)') == 8


def test_2():
    exp = '(1+(4+1))*(1-3)'
    assert sol.calculate(exp) == eval(exp)


def test_3():
    exp = '(1+(((4+5)*2)+2)*(1-3))+(6+8*2)'
    assert sol.calculate(exp) == eval(exp)
