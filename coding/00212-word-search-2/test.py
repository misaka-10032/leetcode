# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.findWords([], ['a', 'b']) == []
    assert sol.findWords([[]], ['a', 'b']) == []
    assert sol.findWords([['a']], ['a', 'b']) == ['a']


def test_1():
    board = [['o', 'a', 'a', 'n'],
             ['e', 't', 'a', 'e'],
             ['i', 'h', 'k', 'r'],
             ['i', 'f', 'l', 'v']]
    words = ["oath", "pea", "eat", "rain"]
    tgt = ["eat", "oath"]
    ans = Solution().findWords(board, words)
    assert sorted(ans) == sorted(tgt)


def test_2():
    board = [['a', 'a']]
    words = ['aaa']
    tgt = []
    ans = Solution().findWords(board, words)
    assert sorted(ans) == sorted(tgt)


def test_3():
    board = [['a', 'a']]
    words = ['aa', 'bb']
    tgt = ['aa']
    ans = Solution().findWords(board, words)
    assert sorted(ans) == sorted(tgt)
