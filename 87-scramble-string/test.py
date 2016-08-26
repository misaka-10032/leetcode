# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.isScramble('', '')
    assert not sol.isScramble('', 'a')
    assert not sol.isScramble('a', '')
    assert sol.isScramble('a', 'a')
    assert not sol.isScramble('a', 'b')
    assert sol.isScramble('ab', 'ba')
    assert sol.isScramble('ba', 'ab')


def test_1():
    sol = Solution()
    assert sol.isScramble('great', 'rgeat')
    assert sol.isScramble('rgeat', 'great')
    assert sol.isScramble('great', 'rgtae')
    assert sol.isScramble('rgtae', 'great')
    assert not sol.isScramble('great', 'trage')
