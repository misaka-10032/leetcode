# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from collections import deque

inf = 2147483647


class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        m = len(rooms)
        n = len(rooms[0])

        q = deque()
        for i in xrange(m):
            for j in xrange(n):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while q:
            i, j, d = q.popleft()
            for di, dj in dirs:
                ii = i + di
                jj = j + dj
                if ii < 0 or ii >= m or \
                   jj < 0 or jj >= n or \
                   rooms[ii][jj] != inf:
                    continue
                rooms[ii][jj] = d+1
                q.append((ii, jj, d+1))
