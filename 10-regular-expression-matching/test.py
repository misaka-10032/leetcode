# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""

from solution import Solution


def test_1():
    sol = Solution()
    assert not sol.isMatch('aa', 'a')
    assert sol.isMatch('aa', 'aa')
    assert not sol.isMatch('aaa', 'aa')
    assert sol.isMatch('aa', 'a*')
    assert sol.isMatch('aa', '.*')
    assert sol.isMatch('ab', '.*')
    assert sol.isMatch('aab', 'c*a*b')
    assert sol.isMatch('abcef', 'ab..*.f')
    assert not sol.isMatch('abcf', 'ab..*.f')
    assert sol.isMatch('aa', 'aab*a*')
    assert sol.isMatch('aabb', 'aab*a*')


def test_2():
    sol = Solution()
    assert sol.isMatch('aaa', 'a*a')
    assert not sol.isMatch('aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*c')
    assert not sol.isMatch('aaba', 'ab*a*c*a')
    assert sol.isMatch('a', 'ab*')


def test_3():
    sol = Solution()
    assert sol.isMatch('aaa', '.*')


def test_4():
    sol = Solution()
    assert sol.isMatch('', '.*')


def test_5():
    sol = Solution()
    assert sol.isMatch("cbaacacaaccbaabcb", "c*b*b*.*ac*.*bc*a*")


def test_6():
    sol = Solution()
    assert not sol.isMatch('ab', 'a*c')


def test_7():
    sol = Solution()
    assert not sol.isMatch("bb", "..*c")
