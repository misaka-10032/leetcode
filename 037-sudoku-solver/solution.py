# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def _fill_appear_row(self, appear, board, i):
        for j in xrange(9):
            c = board[i][j]
            if c == '.':
                continue
            cv = ord(c) - ord('1')
            appear[cv] = True

    def _fill_appear_col(self, appear, board, j):
        for i in xrange(9):
            c = board[i][j]
            if c == '.':
                continue
            cv = ord(c) - ord('1')
            appear[cv] = True

    def _fill_appear_blk(self, appear, board, io, jo):
        for ii in xrange(3):
            for jj in xrange(3):
                i = io * 3 + ii
                j = jo * 3 + jj
                c = board[i][j]
                if c == '.':
                    continue
                cv = ord(c) - ord('1')
                appear[cv] = True

    def _next(self, io, jo, ii, jj):
        if not hasattr(self, '_next_map'):
            self._next_map = {}
            prev = (2, 2, 2, 2)
            for _io in xrange(3):
                for _jo in xrange(3):
                    for _ii in xrange(3):
                        for _jj in xrange(3):
                            self._next_map[prev] = _io, _jo, _ii, _jj
                            prev = _io, _jo, _ii, _jj
            self._next_map[(2, 2, 2, 2)] = (3, 3, 3, 3)
        return self._next_map[(io, jo, ii, jj)]

    def _solve(self, board, io, jo, ii, jj):
        if io == jo == ii == jj == 3:
            self._solved = True
            return
        i = io * 3 + ii
        j = jo * 3 + jj
        io_, jo_, ii_, jj_ = self._next(io, jo, ii, jj)
        c = board[i][j]
        if c == '.':
            appear = [False] * 9
            self._fill_appear_row(appear, board, i)
            self._fill_appear_col(appear, board, j)
            self._fill_appear_blk(appear, board, io, jo)
            for v in xrange(9):
                if self._solved:
                    break
                if appear[v]:
                    continue
                board[i][j] = chr(v+ord('1'))
                appear[v] = True
                self._solve(board, io_, jo_, ii_, jj_)
                if not self._solved:
                    appear[v] = False
                    board[i][j] = '.'
        else:
            self._solve(board, io_, jo_, ii_, jj_)

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # no validity check is needed, as we know there's unique solution
        self._solved = False
        self._solve(board, 0, 0, 0, 0)
