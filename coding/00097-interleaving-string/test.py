# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert not sol.isInterleave('', '', 'a')
    assert sol.isInterleave('', 'bc', 'bc')
    assert not sol.isInterleave('', 'cb', 'bc')
    assert sol.isInterleave('a', 'b', 'ab')
    assert sol.isInterleave('b', 'a', 'ab')


def test_1():
    sol = Solution()
    assert sol.isInterleave('aabcc', 'dbbca', 'aadbbcbcac')
    assert not sol.isInterleave('aabcc', 'dbbca', 'aadbbbaccc')


def test_2():
    sol = Solution()
    assert sol.isInterleave('bc', 'bc', 'bcbc')
