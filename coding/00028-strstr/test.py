# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test():
    sol = Solution()
    assert sol.strStr('a', 'abc') == -1
    assert sol.strStr('abcd', 'ef') == -1
    assert sol.strStr('', '') == 0
    assert sol.strStr('a', 'a') == 0
    assert sol.strStr('efef', '') == 0
    assert sol.strStr('abcdeef', 'cde') == 2
