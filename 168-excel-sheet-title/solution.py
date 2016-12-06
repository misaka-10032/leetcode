# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = []
        while n > 0:
            n -= 1
            res.append(chr((n % 26) + ord('A')))
            n /= 26
        return ''.join(reversed(res))
