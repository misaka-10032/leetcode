# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.countSmaller([]) == []
    assert sol.countSmaller([1]) == [0]
    assert sol.countSmaller([2, 1]) == [1, 0]
    assert sol.countSmaller([1, 2]) == [0, 0]


def test_1():
    sol = Solution()
    assert sol.countSmaller([5, 2, 6, 1]) == [2, 1, 1, 0]
    assert sol.countSmaller([2, 6, 5, 5, 1]) == [1, 3, 1, 1, 0]


def test_2():
    sol = Solution()
    assert sol.countSmaller([-1, 0]) == [0, 0]
