# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

starting from 1, 3, 7, 9 are the same,
so as to 2, 4, 6, 8;
the remaining is 5.

hard-code skip list (rather than next jump, 1->3 is valid when 2 is touched)
keep track of history

maintain counters for number of steps that we are interested in.
"""


class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        def dfs(curr, step):
            if m <= step <= n:
                ctr[0] += 1
            if step >= n:
                return
            for next in xrange(1, 10):
                if visited[next] or not visited[skip[curr][next]]:
                    continue
                visited[next] = True
                dfs(next, step + 1)
                visited[next] = False

        visited = [False] * 10
        visited[0] = True
        skip = [[0] * 10 for _ in xrange(10)]
        # rows
        skip[1][3] = skip[3][1] = 2
        skip[4][6] = skip[6][4] = 5
        skip[7][9] = skip[9][7] = 8
        # cols
        skip[1][7] = skip[7][1] = 4
        skip[2][8] = skip[8][2] = 5
        skip[3][9] = skip[9][3] = 6
        # diagonals
        skip[1][9] = skip[9][1] = 5
        skip[3][7] = skip[7][3] = 5

        ctr = [0]
        cnt = 0

        # starting from 1, 3, 7, 9
        ctr[0] = 0
        visited[1] = True
        dfs(1, 1)
        cnt += ctr[0] * 4
        visited[1] = False

        # starting from 2, 4, 6, 8
        ctr[0] = 0
        visited[2] = True
        dfs(2, 1)
        cnt += ctr[0] * 4
        visited[2] = False

        # starting from 5
        ctr[0] = 0
        visited[5] = True
        dfs(5, 1)
        cnt += ctr[0]
        visited[5] = False

        return cnt
