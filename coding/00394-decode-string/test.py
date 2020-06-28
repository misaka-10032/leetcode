# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert sol.decodeString('') == ''
    assert sol.decodeString('a') == 'a'
    assert sol.decodeString('2[a]') == 'aa'


def test_1():
    assert sol.decodeString('3[a]2[bc]') == 'aaabcbc'
    assert sol.decodeString('3[a2[c]]') == 'accaccacc'
    assert sol.decodeString('2[abc]3[cd]ef') == 'abcabccdcdcdef'
