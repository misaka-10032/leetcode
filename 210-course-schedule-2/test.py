# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.findOrder(3, []) == range(3)
    assert sol.findOrder(2, [[1, 0]]) == [0, 1]
    assert not sol.findOrder(2, [[1, 0], [0, 1]])


def test_1():
    sol = Solution()
    ans = sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    assert ans == [0, 1, 2, 3] or ans == [0, 2, 1, 3]
