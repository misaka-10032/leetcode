# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle or not triangle[0]:
            return 0
        n = len(triangle)
        inf = 999999999
        prev = [triangle[0][0]]
        for i in xrange(1, n):
            curr = [0] * (i+1)
            for j in xrange(i+1):
                t1 = prev[j] if j < i else inf
                t2 = prev[j-1] if j > 0 else inf
                curr[j] = triangle[i][j] + min(t1, t2)
            prev = curr
        return min(prev)
