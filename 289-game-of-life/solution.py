# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def curr(x):
            return x & 1

        def next(x):
            return x >> 1

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1),
                (1, 1), (1, -1), (-1, 1), (-1, -1)]

        if not board or not board[0]:
            return
        m = len(board)
        n = len(board[0])

        for i in xrange(m):
            for j in xrange(n):
                cnt = 0
                for di, dj in dirs:
                    ii = i + di
                    jj = j + dj
                    if ii < 0 or ii >= m or \
                       jj < 0 or jj >= n:
                        continue
                    cnt += curr(board[ii][jj])
                if curr(board[i][j]):
                    if 2 <= cnt <= 3:
                        board[i][j] = 3
                else:
                    if cnt == 3:
                        board[i][j] = 2

        for i in xrange(m):
            for j in xrange(n):
                board[i][j] = next(board[i][j])
