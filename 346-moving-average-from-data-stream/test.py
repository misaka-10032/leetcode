# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import MovingAverage


def test_0():
    sol = MovingAverage(3)
    assert sol.next(1) == 1
    assert sol.next(10) == 11./2
    assert sol.next(3) == 14./3
    assert sol.next(5) == 18./3
