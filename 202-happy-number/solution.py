# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        past = set()
        while n not in past:
            if n == 1:
                return True
            past.add(n)
            v = 0
            while n > 0:
                v += (n % 10)**2
                n //= 10
            n = v
        return False
