# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas:
            return -1
        k = 0
        d_min = 999999999
        curr = 0
        for i in xrange(len(gas)):
            d = gas[i] - cost[i]
            curr += d
            if curr < d_min:
                d_min = curr
                k = i
        if curr < 0:
            return -1
        return (k+1) % len(gas)
