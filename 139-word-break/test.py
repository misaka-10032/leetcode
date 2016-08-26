# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.wordBreak('', [])
    assert sol.wordBreak('', ['a'])
    assert not sol.wordBreak('a', [])
    assert sol.wordBreak('a', ['a'])
    assert sol.wordBreak('abc', ['bc', 'abc'])
    assert not sol.wordBreak('abc', ['ac', 'bc'])


def test_1():
    sol = Solution()
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
        "aaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaa" \
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    d = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa",
         "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    assert not sol.wordBreak(s, d)


def test_2():
    sol = Solution()
    s = 'catsanddog'
    d = ['cat', 'cats', 'and', 'sand', 'dog']
    assert sol.wordBreak(s, d)
