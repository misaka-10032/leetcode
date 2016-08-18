# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class BinaryIndexedTree(object):
    def __init__(self, nums):
        self.sums = [0] * (len(nums)+1)
        for i, v in enumerate(nums):
            self.inc(i, v)

    def inc(self, i, dv):
        k = i + 1
        while k < len(self.sums):
            self.sums[k] += dv
            k += k & -k

    def prefix_sum(self, i):
        """ [0, i) """
        k, s = i, 0
        while k > 0:
            s += self.sums[k]
            k -= k & -k
        return s


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        v2i = {v: i for i, v in enumerate(sorted(set(nums)))}
        freq = BinaryIndexedTree([0]*len(v2i))
        res = []
        for x in reversed(nums):
            i = v2i[x]
            res.append(freq.prefix_sum(i))
            freq.inc(i, 1)
        return res[::-1]
