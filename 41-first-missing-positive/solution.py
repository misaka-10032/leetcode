# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        Tricky in-place operation.
        Be careful of edge cases.

        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums) and nums[i] <= 0:
            i += 1
        if i == len(nums):
            return 1

        # put 1..n in-place to 0..n-1
        while i < len(nums):
            # ignore it
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = -1
                i += 1
                continue
            # already in place
            if nums[i]-1 == i:
                i += 1
                continue
            # in case of duplicate, avoid infinite loop
            if nums[nums[i]-1] == nums[i]:
                i += 1
                continue
            # otherwise nums[nums[i]-1] is not yet in place
            # replace till all in place
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        for i in xrange(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1
