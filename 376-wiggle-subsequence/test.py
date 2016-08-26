# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.wiggleMaxLength([]) == 0
    assert sol.wiggleMaxLength([2]) == 1
    assert sol.wiggleMaxLength([1, 2]) == 2
    assert sol.wiggleMaxLength([2, 1]) == 2


def test_1():
    sol = Solution()
    assert sol.wiggleMaxLength([1, 7, 4, 9, 2, 5]) == 6
    assert sol.wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]) == 7
    assert sol.wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2


def test_2():
    sol = Solution()
    assert sol.wiggleMaxLength([0, 0]) == 1
