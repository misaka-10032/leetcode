# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'

from solution import Solution


def test():
    sol = Solution()
    print sol.longestPalindrome('abccbabaaa')
    assert sol.longestPalindrome('abccbabaaa') == 'abccba'
    assert sol.longestPalindrome('aaaaaaaa') == 'aaaaaaaa'
    assert sol.longestPalindrome('aababcba') == 'abcba'
    assert sol.longestPalindrome('cacaaaabbaa') == 'aabbaa'
