# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import SummaryRanges


def test_1():
    sol = SummaryRanges()
    assert sol.getIntervals() == []
    sol.addNum(1)
    assert sol.getIntervals() == [[1, 1]]
    sol.addNum(3)
    assert sol.getIntervals() == [[1, 1], [3, 3]]
    sol.addNum(7)
    assert sol.getIntervals() == [[1, 1], [3, 3], [7, 7]]
    sol.addNum(2)
    assert sol.getIntervals() == [[1, 3], [7, 7]]
    sol.addNum(6)
    assert sol.getIntervals() == [[1, 3], [6, 7]]
    sol.addNum(3)
    sol.addNum(4)
    sol.addNum(5)
    sol.addNum(6)
    assert sol.getIntervals() == [[1, 7]]
    sol.addNum(6)
    sol.addNum(8)
    assert sol.getIntervals() == [[1, 8]]
