# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        cnt = 1 << len(nums)
        all = []
        for i in xrange(cnt):
            j = i
            idx = 0
            curr = []
            while j > 0:
                if j % 2 == 1:
                    curr.append(nums[idx])
                j >>= 1
                idx += 1
            all.append(curr)
        return all
