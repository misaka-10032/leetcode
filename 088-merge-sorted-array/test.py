# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    a = []
    b = []
    sol.merge(a, 0, b, 0)
    assert a == []

    a = [1]
    b = []
    sol.merge(a, 1, b, 0)
    assert a == [1]

    a = [0]
    b = [1]
    sol.merge(a, 0, b, 1)
    assert a == [1]

    a = [1, 0]
    b = [2]
    sol.merge(a, 1, b, 1)
    assert a == [1, 2]

    a = [2, 0]
    b = [1]
    sol.merge(a, 1, b, 1)
    assert a == [1, 2]


def test_1():
    sol = Solution()
    a = [1, 2, 2, 4, 6, 6, 7] + [0]*6
    b = [2, 3, 5, 7, 9, 10]
    sol.merge(a, 7, b, 6)
    assert a == [1, 2, 2, 2, 3, 4, 5, 6, 6, 7, 7, 9, 10]
