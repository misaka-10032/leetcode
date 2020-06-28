# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert sol.lengthOfLIS([]) == 0
    assert sol.lengthOfLIS([1]) == 1
    assert sol.lengthOfLIS([1, 2]) == 2
    assert sol.lengthOfLIS([2, 1]) == 1


def test_1():
    assert sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
