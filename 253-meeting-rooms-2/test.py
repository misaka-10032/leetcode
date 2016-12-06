# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution, Interval
sol = Solution()


def solve(times):
    intervals = [Interval(s, e) for s, e in times]
    return sol.minMeetingRooms(intervals)


def test_0():
    assert solve([]) == 0
    assert solve([[1, 2]]) == 1


def test_1():
    assert solve([[0, 30], [5, 10], [15, 20]]) == 2
    assert solve([[0, 5], [5, 6]]) == 1
