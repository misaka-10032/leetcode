# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution, Interval


def test_0():
    sol = Solution()
    assert sol.merge([]) == []
    assert sol.merge([Interval(1, 3)]) == [Interval(1, 3)]


def test_1():
    sol = Solution()
    intervals = [Interval(8, 10), Interval(2, 6),
                 Interval(15, 18), Interval(1, 3)]
    ans = [Interval(1, 6), Interval(8, 10), Interval(15, 18)]
    assert ans == sol.merge(intervals)
