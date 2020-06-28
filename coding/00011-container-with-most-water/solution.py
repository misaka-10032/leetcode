# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p = 0
        q = len(height) - 1
        max_a = 0
        while p < q:
            h = min(height[p], height[q])
            a = (q - p) * h
            if a > max_a:
                max_a = a
            while p < q and height[p] <= h:
                p += 1
            while p < q and height[q] <= h:
                q -= 1
        return max_a
