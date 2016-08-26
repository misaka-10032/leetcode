# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        ugly = [0] * n
        ugly[0] = 1
        l2 = l3 = l5 = 0  # all start at level 0
        for i in xrange(1, n):
            curr = min(2*ugly[l2], 3*ugly[l3], 5*ugly[l5])
            ugly[i] = curr
            l2 += 1 if curr == 2*ugly[l2] else 0
            l3 += 1 if curr == 3*ugly[l3] else 0
            l5 += 1 if curr == 5*ugly[l5] else 0
        return ugly[-1]
