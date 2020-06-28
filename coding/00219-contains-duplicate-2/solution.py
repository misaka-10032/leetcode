# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        k += 1
        n = len(nums)
        s = set()
        for i in xrange(min(n, k)):
            if nums[i] not in s:
                s.add(nums[i])
            else:
                return True
        for i in xrange(k, n):
            s.remove(nums[i-k])
            if nums[i] not in s:
                s.add(nums[i])
            else:
                return True
        return False
