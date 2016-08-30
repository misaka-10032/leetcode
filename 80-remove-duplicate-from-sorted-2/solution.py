# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        sz = cnt = 1
        for i in xrange(1, n):
            if nums[i] != nums[sz-1]:
                nums[sz] = nums[i]
                sz += 1
                cnt = 1
            elif cnt < 2:
                nums[sz] = nums[i]
                sz += 1
                cnt += 1
        return sz
