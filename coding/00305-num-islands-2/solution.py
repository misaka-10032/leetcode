# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        def find_root(i, j):
            """ assumes parents[i][j] != 0 """
            cnt = 0
            while parents[i][j] != (i, j):
                cnt += 1
                i, j = parents[i][j]
            return (i, j), cnt

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        tot = 0
        parents = [[None] * n for _ in xrange(m)]
        res = []
        for i, j in positions:

            # duplicate island
            if parents[i][j]:
                continue

            tot += 1
            parents[i][j] = (i, j)

            # check neighbors
            roots = []
            cnts = []
            neighbors = []
            for di, dj in dirs:
                ii = i + di
                jj = j + dj
                if ii < 0 or ii >= m or \
                   jj < 0 or jj >= n:
                    continue
                if not parents[ii][jj]:
                    continue

                root, cnt = find_root(ii, jj)
                if root in roots:
                    continue

                neighbors.append((ii, jj))
                roots.append(root)
                cnts.append(cnt)

            if len(cnts) == 0:
                res.append(tot)
                continue

            # assign that of most cnt as master
            idx = max(range(len(cnts)), key=lambda k: cnts[k])
            # roots[idx] would be the master root
            parents[i][j] = roots[idx]
            tot -= len(cnts)
            for k in xrange(len(cnts)):
                rii, rjj = roots[k]
                parents[rii][rjj] = roots[idx]

            res.append(tot)

        return res
