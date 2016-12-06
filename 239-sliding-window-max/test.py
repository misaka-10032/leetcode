# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert sol.maxSlidingWindow([1, 2], 3) == []
    assert sol.maxSlidingWindow([1, 2], 2) == [2]
    assert sol.maxSlidingWindow([1, 2], 1) == [1, 2]
    assert sol.maxSlidingWindow([1, 2], 0) == []


def test_1():
    a = [1, 3, -1, -3, 5, 3, 6, 7]
    t = [3, 3, 5, 5, 6, 7]
    assert sol.maxSlidingWindow(a, 3) == t


def test_2():
    a, k = [7, 2, 4], 2
    t = [7, 4]
    assert sol.maxSlidingWindow(a, k) == t


def test_3():
    a, k = [1, 3, 1, 2, 0, 5], 3
    t = [3, 3, 2, 5]
    assert sol.maxSlidingWindow(a, k) == t
