# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from collections import deque


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0

        best = heights[0]
        n = len(heights)
        S = deque()  # stack of INDICES
        S.append(0)
        for i in xrange(1, n):
            h = heights[i]
            while S and heights[S[-1]] >= h:
                j = S.pop()
                leftmost = S[-1]+1 if S else 0
                area = heights[j] * (i-leftmost)
                best = max(best, area)
            S.append(i)
        # Last cohort
        while S:
            j = S.pop()
            leftmost = S[-1]+1 if S else 0
            area = heights[j] * (n-leftmost)
            best = max(best, area)
        return best
