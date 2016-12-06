# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution

sol = Solution()


def test_0():
    assert sol.summaryRanges([]) == []
    assert sol.summaryRanges([3]) == ['3']
    assert sol.summaryRanges([2, 3]) == ['2->3']
    assert sol.summaryRanges([2, 4]) == ['2', '4']


def test_1():
    assert sol.summaryRanges([0, 1, 2, 4, 5, 7]) == \
            ['0->2', '4->5', '7']
