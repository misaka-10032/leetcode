# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        v = 0
        stack = []
        for i in xrange(len(height)):
            h = height[i]
            h_base = -1
            # pop until empty or top is greater
            while stack and height[stack[-1]] <= h:
                i_prev = stack.pop()
                h_prev = height[i_prev]
                if h_base >= 0:
                    v += (h_prev - h_base) * (i - i_prev - 1)
                h_base = h_prev
            # edge case, that stage isn't popped yet, neither is v accumulated.
            if stack and h_base >= 0:
                i_prev = stack[-1]
                v += (h - h_base) * (i - i_prev - 1)
            stack.append(i)
        return v
