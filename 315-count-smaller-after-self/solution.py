# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

import bisect


class BITree(object):
    def __init__(self, freqs):
        self.freqs = freqs
        self.sums = [0] * (len(self.freqs) + 1)

    def inc(self, k, dv):
        k += 1
        while k < len(self.sums):
            self.sums[k] += dv
            k += k & -k  # find siblings

    def prefix(self, k):
        """ Computes sum(freq[:k]) """
        s = 0
        k += 1
        while k > 0:
            s += self.sums[k]
            k -= k & -k  # k & -k finds the rightmost 1 of k
        return s


class FreqTable(object):
    def __init__(self, nums):
        self.vals = sorted(set(nums))
        self.freqs = BITree([0] * (len(self.vals) + 1))

    def inc(self, v, df):
        i = bisect.bisect_left(self.vals, v)
        self.freqs.inc(i, df)

    def prefix(self, v):
        # a[j] < a[i], j < i
        # a[j] >= a[i], j >= i
        i = bisect.bisect_left(self.vals, v)
        return self.freqs.prefix(i-1)


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        ft = FreqTable(nums)
        res = []
        for v in reversed(nums):
            ft.inc(v, 1)
            res.append(ft.prefix(v))
        return res[::-1]
