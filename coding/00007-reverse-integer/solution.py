# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'


class Solution(object):
    TMAX = int((1 << 31) - 1)
    TMIN = int(-(1 << 31))

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            sign = 1
        else:
            x = -x
            sign = -1
        y = 0
        while x:
            y *= 10
            y += x % 10
            x /= 10
        r = sign * y
        return r if self.TMIN <= r <= self.TMAX else 0
