# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.minPatches([], 5) == 3
    assert sol.minPatches([], 7) == 3
    assert sol.minPatches([], 8) == 4
    assert sol.minPatches([1], 1) == 0
    assert sol.minPatches([1], 2) == 1


def test_1():
    sol = Solution()
    assert sol.minPatches([1, 3], 6) == 1
    assert sol.minPatches([1, 5, 10], 20) == 2
    assert sol.minPatches([1, 2, 2], 5) == 0
    assert sol.minPatches([1, 2, 4, 13, 43], 100) == 2
