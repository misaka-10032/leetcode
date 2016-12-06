# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert not sol.isNumber('')
    assert sol.isNumber('1')
    assert sol.isNumber('-1')
    assert sol.isNumber('+1')
    assert sol.isNumber('-1.3 ')
    assert sol.isNumber(' +1.3e1')
    assert sol.isNumber('-1.3e-2')
    assert not sol.isNumber('-1.3e-1.2')


def test_1():
    assert sol.isNumber(' 0.1 ')
    assert not sol.isNumber('abc')
    assert not sol.isNumber('abc ')
    assert not sol.isNumber('1 a')
    assert sol.isNumber('2e10')
    assert not sol.isNumber('-e')
    assert not sol.isNumber('-1e-')
    assert sol.isNumber('-1e-2')


def test_2():
    assert not sol.isNumber('. ')
    assert not sol.isNumber('.e-1')
    assert sol.isNumber('.1e-1')
    assert sol.isNumber('-.1e-1')


def test_3():
    assert not sol.isNumber('e9')
