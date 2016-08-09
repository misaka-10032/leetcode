# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1

        if n > 0:
            base2 = []
            while n > 0:
                base2.append(n % 2)
                n /= 2
            xb = x
            r = 1
            for base in base2:
                if base:
                    r *= xb  # take this base
                xb *= xb     # prepare for next
            return r

        if n < 0:
            base2 = []
            n = -n
            while n > 0:
                base2.append(n % 2)
                n /= 2
            xb = 1./x
            r = 1
            for base in base2:
                if base:
                    r *= xb
                xb *= xb
            return r
