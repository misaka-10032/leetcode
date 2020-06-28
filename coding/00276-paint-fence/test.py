# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert sol.numWays(0, 3) == 0
    assert sol.numWays(1, 3) == 3
    assert sol.numWays(2, 3) == 9


def test_1():
    assert sol.numWays(10, 3) == 27408
    assert sol.numWays(10, 5) == 7348480
