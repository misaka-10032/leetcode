# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.trap([]) == 0
    assert sol.trap([23]) == 0


def test_1():
    sol = Solution()
    assert sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert sol.trap([5, 3, 2, 1, 0, 4, 3, 3, 2, 3]) == 11
