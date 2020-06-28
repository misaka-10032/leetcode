# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert sol.isHappy(1)
    assert not sol.isHappy(2)
    assert not sol.isHappy(3)
    assert sol.isHappy(7)
    assert sol.isHappy(19)
