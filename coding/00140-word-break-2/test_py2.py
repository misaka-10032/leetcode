# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.wordBreak('', ['cat']) == []
    assert sol.wordBreak('cat', []) == []
    assert sol.wordBreak('cat', ['dog']) == []
    assert sorted(sol.wordBreak('cat', ['cat', 'c', 'at'])) == sorted(['cat', 'c at'])


def test_1():
    sol = Solution()
    s = 'catsanddog'
    d = ['cat', 'cats', 'and', 'sand', 'dog']
    tgt = ['cats and dog', 'cat sand dog']
    assert sorted(sol.wordBreak(s, d)) == sorted(tgt)


def test_2():
    sol = Solution()
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
        "aaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaa" \
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    d = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa",
         "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    assert sol.wordBreak(s, d) == []
