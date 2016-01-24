# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'

from solution import Solution


def test():
    sol = Solution()
    assert not sol.isPalindrome(-12321)
    assert not sol.isPalindrome(123)
    assert sol.isPalindrome(12321)
    assert sol.isPalindrome(123321)
