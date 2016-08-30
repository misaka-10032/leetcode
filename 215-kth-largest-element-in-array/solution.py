# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from random import randint


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(i, j):
            """ partition range [i, j].
                put nums[i] in location and
                return its location. """
            # introduce randomness to get rid of worst case
            k = randint(i, j)
            nums[i], nums[k] = nums[k], nums[i]
            while i < j:
                while i < j and nums[j] >= nums[i]:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
                while i < j and nums[i] <= nums[j]:
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]
            return i

        n = len(nums)
        # convert the problem to find k-th smallest, where k is index.
        k = n - k
        i = 0
        j = n - 1
        while True:
            p = partition(i, j)
            if k < p:
                j = p - 1
            elif k > p:
                i = p + 1
            else:
                return nums[p]
