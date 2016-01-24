# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'

from solution import Solution


def test():
    sol = Solution()
    assert sol.lengthOfLongestSubstring('') == 0
    assert sol.lengthOfLongestSubstring('abcabcbb') == 3
    assert sol.lengthOfLongestSubstring('bbbbb') == 1
    assert sol.lengthOfLongestSubstring('abcdeeabcd') == 5
