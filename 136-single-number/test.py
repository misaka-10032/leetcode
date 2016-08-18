# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test():
    sol = Solution()
    assert sol.singleNumber([101]) == 101
    assert sol.singleNumber([23, 23, 45]) == 45
