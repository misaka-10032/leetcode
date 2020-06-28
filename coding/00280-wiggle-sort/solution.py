# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        res = []
        vals = sorted(nums)
        l, r = 0, len(vals)-1
        while l < r:
            res.append(vals[l])
            res.append(vals[r])
            l += 1
            r -= 1
        if l == r:
            res.append(vals[l])
        nums[:] = res[:]
