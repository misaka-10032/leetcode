# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_1():
    sol = Solution()
    a = []
    assert sol.removeDuplicates(a) == 0 and a == []
    a = [1]
    assert sol.removeDuplicates(a) == 1 and a[:1] == [1]


def test_2():
    sol = Solution()
    a = [1, 1, 1, 2, 2, 3]
    assert sol.removeDuplicates(a) == 5 and a[:5] == [1, 1, 2, 2, 3]


def test_3():
    sol = Solution()
    a = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 5]
    assert sol.removeDuplicates(a) == 9 and \
           a[:9] == [1, 1, 2, 2, 3, 3, 4, 5, 5]
