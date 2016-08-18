# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = [0] * len(nums)
        # idx 0 is dummy
        self.sums = [0] * (len(nums)+1)
        for i in xrange(len(nums)):
            self.update(i, nums[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        dv = val - self.nums[i]
        self.nums[i] = val
        k = i + 1
        while k < len(self.sums):
            self.sums[k] += dv
            k += k & -k

    def prefix_sum(self, i):
        """
        Computes [0, i]
        :param i:
        :return:
        """
        k = i + 1
        s = 0
        while k > 0:
            s += self.sums[k]
            k -= k & -k
        return s

    def sumRange(self, i, j):
        """
        Sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.prefix_sum(j) - self.prefix_sum(i-1)
