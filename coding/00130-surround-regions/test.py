# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    board, tgt = [], []
    sol.solve(board)
    assert board == tgt
    board, tgt = [[]], [[]]
    sol.solve(board)
    assert board == tgt


def test_1():
    board = [['X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']]
    tgt = [['X', 'X', 'X', 'X'],
           ['X', 'X', 'X', 'X'],
           ['X', 'X', 'X', 'X'],
           ['X', 'O', 'X', 'X']]
    sol = Solution()
    sol.solve(board)
    assert board == tgt


def test_2():
    board = [['X', 'O', 'X'],
             ['X', 'O', 'X'],
             ['X', 'O', 'X']]
    tgt = [['X', 'O', 'X'],
           ['X', 'O', 'X'],
           ['X', 'O', 'X']]
    sol = Solution()
    sol.solve(board)
    assert board == tgt
