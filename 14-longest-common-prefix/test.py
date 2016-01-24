# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'

from solution import Solution


def test():
    sol = Solution()
    strs = ['aaabc', 'aadd', 'abaa']
    assert sol.longestCommonPrefix(strs) == 'a'
    strs = ['absd', 'abab', '']
    assert sol.longestCommonPrefix(strs) == ''
    strs = []
    assert sol.longestCommonPrefix(strs) == ''
    strs = ['abcd', 'eft']
    assert sol.longestCommonPrefix(strs) == ''
    strs = ['abcdef', 'abcabc', 'abckllsdf']
    assert sol.longestCommonPrefix(strs) == 'abc'
