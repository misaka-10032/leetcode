# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n % 4 == 0:
            n /= 4
        while n % 9 == 0:
            n /= 9
        while n % 25 == 0:
            n /= 25

        if n % 8 == 7:
            return 4

        a = int(n**.5)
        if a**2 == n:
            return 1

        last = int(n**.5)
        for a in xrange(1, last+1):
            r = n - a**2
            b = int(r**.5)
            if a**2+b**2 == n:
                return 2

        return 3
