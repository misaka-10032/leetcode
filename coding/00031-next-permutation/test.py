# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    a = []
    sol.nextPermutation(a)
    assert a == []

    a = [12]
    sol.nextPermutation(a)
    assert a == [12]

    a = [1, 2]
    sol.nextPermutation(a)
    assert a == [2, 1]

    a = [2, 1]
    sol.nextPermutation(a)
    assert a == [1, 2]

    a = [5, 4, 3]
    sol.nextPermutation(a)
    assert a == [3, 4, 5]


def test_1():
    sol = Solution()
    a = [1, 2, 3]
    sol.nextPermutation(a)
    assert a == [1, 3, 2]

    a = [9, 2, 5, 4, 3, 1]
    sol.nextPermutation(a)
    assert a == [9, 3, 1, 2, 4, 5]


def test_2():
    sol = Solution()
    a = [2, 3, 1, 3, 3]
    sol.nextPermutation(a)
    assert a == [2, 3, 3, 1, 3]
