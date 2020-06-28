# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert sol.threeSumSmaller([], 1) == 0
    assert sol.threeSumSmaller([1], 2) == 0
    assert sol.threeSumSmaller([1, 2], 3) == 0
    assert sol.threeSumSmaller([1, 2, 3], 0) == 0
    assert sol.threeSumSmaller([1, 2, 3], 6) == 0
    assert sol.threeSumSmaller([1, 2, 3], 7) == 1


def test_1():
    assert sol.threeSumSmaller([-2, 0, 1, 3], 2) == 2
    assert sol.threeSumSmaller([1, 1, 1, 1], 4) == 4


def test_2():
    assert sol.threeSumSmaller([0, -4, -1, 1, -1, 2], -5) == 1
