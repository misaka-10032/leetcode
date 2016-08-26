# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        farthest = 1  # curr range is [0, farthest)
        cnt = 0       # number of patches
        for x in nums:
            while x > farthest and farthest <= n:
                cnt += 1        # patch farthest
                farthest <<= 1  # update range
            if farthest > n:
                break
            farthest += x       # update range
        while farthest <= n:    # last batch
            cnt += 1
            farthest <<= 1
        return cnt
