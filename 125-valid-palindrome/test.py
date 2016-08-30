# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.isPalindrome('')
    assert sol.isPalindrome('a')
    assert sol.isPalindrome(',,.*(#&@$')
    assert sol.isPalindrome('a,!a')


def test_1():
    sol = Solution()
    assert sol.isPalindrome('A man, a plan, a canal: Panama')
    assert not sol.isPalindrome('race a car')


def test_2():
    sol = Solution()
    assert not sol.isPalindrome('0P')
