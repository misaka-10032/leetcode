# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(i, j, k):
            if word[k] != board[i][j]:
                return False
            if k == len(word)-1:
                return True
            for di, dj in dirs:
                ii = i + di
                jj = j + dj
                if 0 <= ii < m and 0 <= jj < n and not visited[ii][jj]:
                    visited[ii][jj] = True
                    if dfs(ii, jj, k+1):
                        return True
                    visited[ii][jj] = False
            return False

        if not word:
            return True
        if not board or not board[0]:
            return False

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                visited[i][j] = True
                if dfs(i, j, 0):
                    return True
                visited[i][j] = False
        return False
