# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    a = []
    sol.wiggleSort(a)
    assert a == []

    a = [1]
    sol.wiggleSort(a)
    assert a == [1]

    a = [2, 1]
    sol.wiggleSort(a)
    assert a == [1, 2]

    a = [1, 2, 3]
    sol.wiggleSort(a)
    assert a == [1, 3, 2]


def test_1():
    a = [3, 5, 2, 1, 6, 4]
    sol.wiggleSort(a)
    assert a == [1, 6, 2, 5, 3, 4]
