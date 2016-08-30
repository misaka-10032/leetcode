# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.exist([[]], '')
    assert not sol.exist([[]], 'w')
    assert sol.exist([['w']], 'w')
    assert not sol.exist([['a', 'a']], 'aaa')


def test_1():
    sol = Solution()
    board = [['a', 'b', 'c', 'e'],
             ['s', 'f', 'c', 's'],
             ['a', 'd', 'e', 'e']]
    assert sol.exist(board, 'abcced')
    assert sol.exist(board, 'see')
    assert not sol.exist(board, 'abcb')
