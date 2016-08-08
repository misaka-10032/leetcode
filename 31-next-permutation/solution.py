# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


def reverse(nums, l, r):
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        # find non-increasing suffix
        for i in xrange(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                break

        # i is pivot
        # but it's hard to tell if there' duplicate
        # 4, 4, 3, 2 1
        if i == 0 and nums[0] >= nums[1]:
            # don't need to sort it as we know we only need to reverse it
            reverse(nums, 0, len(nums)-1)
            return

        # find the first index whose value > nums[i]
        # >= is arguable, choose > here
        for j in xrange(len(nums)-1, -1, -1):
            if nums[j] > nums[i]:
                break

        nums[i], nums[j] = nums[j], nums[i]
        reverse(nums, i+1, len(nums)-1)
