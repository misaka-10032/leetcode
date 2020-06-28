# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution

sol = Solution()


def test_0():
    assert sol.fractionToDecimal(0, 1) == '0'
    assert sol.fractionToDecimal(1, 1) == '1'
    assert sol.fractionToDecimal(2, 1) == '2'
    assert sol.fractionToDecimal(1, 2) == '0.5'
    assert sol.fractionToDecimal(1, 3) == '0.(3)'


def test_1():
    assert sol.fractionToDecimal(-5, 3) == '-1.(6)'
    assert sol.fractionToDecimal(10, -7) == '-1.(428571)'
    assert sol.fractionToDecimal(23, 5) == '4.6'
    assert sol.fractionToDecimal(12, 2) == '6'
    assert sol.fractionToDecimal(-1, -13) == '0.(076923)'
    assert sol.fractionToDecimal(1, 1300) == '0.00(076923)'


def test_2():
    assert sol.fractionToDecimal(7, -12) == '-0.58(3)'
