# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        if citations[-1] == 0:
            # sorted, last is max.
            return 0
        n = len(citations)
        i, j = 0, n-1
        while i < j:
            m = (i+j) // 2
            if citations[m] <= n-1-m:
                # p > m
                i = m + 1
            else:
                # p <= m
                j = m
        return n-i
