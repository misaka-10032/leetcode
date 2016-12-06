# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert sol.maxEnvelopes([]) == 0
    assert sol.maxEnvelopes([[1, 2]]) == 1
    assert sol.maxEnvelopes([[1, 2], [3, 4]]) == 2
    assert sol.maxEnvelopes([[3, 4], [1, 2]]) == 2
    assert sol.maxEnvelopes([[1, 4], [2, 3]]) == 1
    assert sol.maxEnvelopes([[1, 1], [1, 1], [1, 1]]) == 1

def test_1():
    assert sol.maxEnvelopes([[5, 4], [6, 5], [6, 7], [2, 3]]) == 3
