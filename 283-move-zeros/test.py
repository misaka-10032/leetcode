# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    a = []
    sol.moveZeroes(a)
    assert a == []

    a = [0]
    sol.moveZeroes(a)
    assert a == [0]

    a = [0, 1]
    sol.moveZeroes(a)
    assert a == [1, 0]


def test_1():
    sol = Solution()
    a = [0, 1, 0, 3, 12]
    sol.moveZeroes(a)
    assert a == [1, 3, 12, 0, 0]
