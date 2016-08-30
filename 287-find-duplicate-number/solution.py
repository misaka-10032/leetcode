# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        slow = nums[0]
        fast = nums[slow]
        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
        slow = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        return fast
