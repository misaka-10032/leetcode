# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False

        n = len(nums)
        l, r = 0, n-1
        while l < r and nums[l] >= nums[r]:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            if nums[m] > nums[l]:
                l = m + 1
            elif nums[m] < nums[l]:
                r = m - 1
            else:
                l += 1
        # now pivot is l
        p = l

        # make side decision easier
        if nums[l] == target or nums[r] == target:
            return True

        if target > nums[-1]:
            # left side
            l, r = 0, p
        else:
            # right side
            l, r = p, n-1
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return True
        return nums[l] == target
