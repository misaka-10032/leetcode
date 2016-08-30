# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_1():
    sol = Solution()
    assert sol.firstMissingPositive([]) == 1
    assert sol.firstMissingPositive([1]) == 2
    assert sol.firstMissingPositive([1, 1]) == 2
    assert sol.firstMissingPositive([2, 3]) == 1
    assert sol.firstMissingPositive([1, 2, 3, 2, 5]) == 4
    assert sol.firstMissingPositive([1, 2, 3, 5, 6, 7]) == 4
    assert sol.firstMissingPositive([1, 3, 2, 5]) == 4
    assert sol.firstMissingPositive([1, 2, 0]) == 3
    assert sol.firstMissingPositive([3, 4, -1, 1]) == 2
