# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.isMatch('', '')
    assert not sol.isMatch('', 'a')
    assert not sol.isMatch('a', '')
    assert sol.isMatch('', '*')


def test_1():
    sol = Solution()
    assert not sol.isMatch('aa', 'a')
    assert sol.isMatch('aa', 'aa')
    assert not sol.isMatch('aaa', 'aa')
    assert sol.isMatch('aa', '*')
    assert sol.isMatch('aa', 'a*')
    assert sol.isMatch('ab', '?*')
    assert not sol.isMatch('aab', 'c*a*b')


def test_2():
    sol = Solution()
    assert sol.isMatch('ababc', 'a?a?c')
    assert sol.isMatch('ababc', '?*bc')
    assert sol.isMatch('ababc', '*c')
    assert sol.isMatch('ababc', 'ab*')


def test_3():
    sol = Solution()
    s = "babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb"
    p = "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"
    assert not sol.isMatch(s, p)


def test_4():
    sol = Solution()
    assert sol.isMatch('hi', '*?')
