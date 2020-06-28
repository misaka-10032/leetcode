# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

import solution
sol = solution.Solution()


def test_0():
    solution.thresh = 1
    assert sol.firstBadVersion(1) == 1
    assert sol.firstBadVersion(2) == 1


def test_1():
    solution.thresh = 3
    assert sol.firstBadVersion(3) == 3
    assert sol.firstBadVersion(5) == 3
    assert sol.firstBadVersion(100) == 3
