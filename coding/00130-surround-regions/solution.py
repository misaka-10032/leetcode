# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from collections import deque


class Solution(object):
    dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    def flood(self, i, j):
        Q = deque()
        Q.append((i, j))
        self.board[i][j] = 'F'
        while Q:
            i, j = Q.popleft()
            for di, dj in self.dirs:
                ii, jj = i+di, j+dj
                if ii < 0 or ii >= self.m:
                    continue
                if jj < 0 or jj >= self.n:
                    continue
                if self.board[ii][jj] != 'O':
                    continue
                self.board[ii][jj] = 'F'
                Q.append((ii, jj))

    def solve(self, board):
        """
        Flood from border, then reverse it.

        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        self.board = board
        self.m, self.n = len(board), len(board[0])
        if self.m == 0 or self.n == 0:
            return

        for j in xrange(self.n):
            if board[0][j] == 'O':
                self.flood(0, j)
            if board[-1][j] == 'O':
                self.flood(self.m - 1, j)
        for i in xrange(self.m):
            if board[i][0] == 'O':
                self.flood(i, 0)
            if board[i][-1] == 'O':
                self.flood(i, self.n - 1)

        for i in xrange(self.m):
            for j in xrange(self.n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'F':
                    board[i][j] = 'O'
