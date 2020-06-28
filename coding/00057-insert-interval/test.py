# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution, Interval


def test_0():
    sol = Solution()
    assert sol.insert([], Interval(1, 3)) == [Interval(1, 3)]
    assert sol.insert([Interval(1, 3)], Interval(4, 6)) == \
           [Interval(1, 3), Interval(4, 6)]
    assert sol.insert([Interval(4, 6)], Interval(1, 3)) == \
           [Interval(1, 3), Interval(4, 6)]
    assert sol.insert([Interval(1, 3)], Interval(2, 4)) == [Interval(1, 4)]


def test_1():
    sol = Solution()
    intervals = [Interval(1, 2), Interval(3, 5), Interval(6, 7),
                 Interval(8, 10), Interval(12, 16)]
    new = Interval(4, 9)
    ans = [Interval(1, 2), Interval(3, 10), Interval(12, 16)]
    assert sol.insert(intervals, new) == ans


def test_2():
    sol = Solution()
    intervals = [Interval(1, 5)]
    new = Interval(0, 3)
    ans = [Interval(0, 5)]
    assert sol.insert(intervals, new) == ans
