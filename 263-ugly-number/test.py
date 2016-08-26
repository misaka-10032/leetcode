# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert not sol.isUgly(0)
    assert sol.isUgly(1)
    assert sol.isUgly(2)
    assert sol.isUgly(3)
    assert sol.isUgly(4)
    assert sol.isUgly(5)
    assert sol.isUgly(6)


def test_1():
    sol = Solution()
    assert not sol.isUgly(7)
    assert sol.isUgly(8)
    assert not sol.isUgly(-8)
    assert not sol.isUgly(-14)


def test_2():
    sol = Solution()
    assert not sol.isUgly(-2147483648)
