# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'

from solution import Solution


def test():
    sol = Solution()
    assert sol.reverse(100) == 1
    assert sol.reverse(-10) == -1
    assert sol.reverse(123) == 321
    assert sol.reverse(-123) == -321
    assert sol.reverse(1000000003) == 0
    assert sol.reverse(-1000000003) == 0
