# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.findDuplicate([]) == -1
    assert sol.findDuplicate([1, 1]) == 1


def test_1():
    sol = Solution()
    assert sol.findDuplicate([1, 2, 3, 2, 2]) == 2
    assert sol.findDuplicate([1, 3, 2, 4, 5, 2]) == 2
