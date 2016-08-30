# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.canJump([])
    assert sol.canJump([10])


def test_1():
    sol = Solution()
    assert sol.canJump([2, 3, 1, 1, 4])
    assert not sol.canJump([3, 2, 1, 0, 4])
