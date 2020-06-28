# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        def _div(r, d):
            while r % d == 0:
                r /= d
            return r

        r = num
        if r <= 0:
            return False

        r = _div(r, 2)
        r = _div(r, 3)
        r = _div(r, 5)
        if r > 5:
            return False
        else:
            return True
