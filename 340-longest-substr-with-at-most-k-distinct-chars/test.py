# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()
f = lambda s, k: sol.lengthOfLongestSubstringKDistinct(s, k)


def test_0():
    assert f('', 2) == 0
    assert f('a', 2) == 1
    assert f('ab', 2) == 2
    assert f('abc', 2) == 2
    assert f('abc', 0) == 0
    assert f('aa', 0) == 0


def test_1():
    assert f('eceba', 2) == 3
