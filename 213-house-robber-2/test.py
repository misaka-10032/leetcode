# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.rob([]) == 0
    assert sol.rob([2]) == 2
    assert sol.rob([1, 2]) == 2


def test_1():
    sol = Solution()
    assert sol.rob([1, 2, 3, 4, 5, 6]) == 12
    assert sol.rob([1, 2, 3, 4, 100, 5]) == 104


def test_2():
    sol = Solution()
    assert sol.rob([1, 2, 3, 4, 5]) == 8   # 1, 3, 5
    assert sol.rob([9, 2, 3, 4, 5]) == 13  # 9, 4
    assert sol.rob([7, 2, 3, 4, 5, 8]) == 15   # 7, 3, 5
    assert sol.rob([7, 2, 3, 4, 5, 10]) == 16  # 2, 4, 10
