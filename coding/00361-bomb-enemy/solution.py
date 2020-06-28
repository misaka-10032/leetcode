# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

* Decompose the problem into find # enemies in a row/col
* row[i][j] = # enemies to be killed in row i if bomb is placed at (i, j)
              -1, if not possible
* similar to col[i][j]
"""


class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def num_enemies(row, j):
            n = len(row)
            k = j
            cnt = 0
            while k < n and row[k] != 'W':
                cnt += row[k] == 'E'
                k += 1
            return cnt

        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])
        grid_T = [[grid[i][j] for i in xrange(m)] for j in xrange(n)]
        row_res = [[-1] * n for _ in xrange(m)]
        col_res = [[-1] * n for _ in xrange(m)]

        for i in xrange(m):
            row = grid[i]
            j = 0
            while j < n:
                cnt = num_enemies(row, j)
                while j < n and row[j] != 'W':
                    if row[j] == '0':
                        row_res[i][j] = cnt
                    j += 1
                j += 1

        for j in xrange(n):
            col = grid_T[j]
            i = 0
            while i < m:
                cnt = num_enemies(col, i)
                while i < m and col[i] != 'W':
                    if col[i] == '0':
                        col_res[i][j] = cnt
                    i += 1
                i += 1

        best = 0
        for i in xrange(m):
            for j in xrange(n):
                if row_res[i][j] >= 0 and col_res[i][j] >= 0:
                    best = max(best, row_res[i][j] + col_res[i][j])

        return best
