# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def _is_row_valid(self, board, i):
        appear = [False] * 9
        for j in xrange(9):
            c = board[i][j]
            if c == '.':
                continue
            cv = ord(c) - ord('1')
            if not 0 <= cv < 9:
                return False
            if appear[cv]:
                return False
            else:
                appear[cv] = True
        return True

    def _is_col_valid(self, board, j):
        appear = [False] * 9
        for i in xrange(9):
            c = board[i][j]
            if c == '.':
                continue
            cv = ord(c) - ord('1')
            if not 0 <= cv < 9:
                return False
            if appear[cv]:
                return False
            else:
                appear[cv] = True
        return True

    def _is_block_valid(self, board, io, jo):
        appear = [False] * 9
        for ii in xrange(3):
            for jj in xrange(3):
                i = io * 3 + ii
                j = jo * 3 + jj
                c = board[i][j]
                if c == '.':
                    continue
                cv = ord(c) - ord('1')
                if not 0 <= cv < 9:
                    return False
                if appear[cv]:
                    return False
                else:
                    appear[cv] = True
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in xrange(9):
            if not self._is_row_valid(board, i):
                return False

        for j in xrange(9):
            if not self._is_col_valid(board, j):
                return False

        for io in xrange(3):
            for jo in xrange(3):
                if not self._is_block_valid(board, io, jo):
                    return False

        return True
