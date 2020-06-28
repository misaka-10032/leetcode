# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert sol.lengthOfLongestSubstringTwoDistinct('') == 0
    assert sol.lengthOfLongestSubstringTwoDistinct('a') == 1


def test_1():
    assert sol.lengthOfLongestSubstringTwoDistinct('eceba') == 3
    assert sol.lengthOfLongestSubstringTwoDistinct('ececbab') == 4
    assert sol.lengthOfLongestSubstringTwoDistinct('babecece') == 5
