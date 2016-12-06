# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert sol.convertToTitle(1) == 'A'
    assert sol.convertToTitle(2) == 'B'
    assert sol.convertToTitle(26) == 'Z'
    assert sol.convertToTitle(27) == 'AA'
    assert sol.convertToTitle(52) == 'AZ'
    assert sol.convertToTitle(53) == 'BA'
    assert sol.convertToTitle(54) == 'BB'

