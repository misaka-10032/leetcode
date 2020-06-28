# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.longestConsecutive([]) == 0
    assert sol.longestConsecutive([3]) == 1
    assert sol.longestConsecutive([2, 1]) == 2


def test_1():
    sol = Solution()
    assert sol.longestConsecutive(range(100000)[::-1]) == 100000
