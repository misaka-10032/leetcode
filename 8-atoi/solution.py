# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'


class Solution(object):
    TMAX = 2147483647
    TMIN = -2147483648

    def _wrap(self, sign, val):
        r = sign * val
        if r < self.TMIN:
            return self.TMIN
        elif r > self.TMAX:
            return self.TMAX
        else:
            return r

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        met_sign = False
        met_num = False
        sign = 1
        val = 0
        for c in str:
            if not met_sign and c == ' ':
                continue
            elif not met_sign and c == '+':
                met_sign = True
            elif not met_sign and c == '-':
                met_sign = True
                sign = -1
            elif '0' <= c <= '9':
                met_sign = met_num = True
                val *= 10
                val += ord(c) - ord('0')
                r = self._wrap(sign, val)
                if r == self.TMIN or r == self.TMAX:
                    return r
            elif met_num and (c < '0' or c > '9'):
                return self._wrap(sign, val)
            else:
                return 0
        return self._wrap(sign, val)
