# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution:
    def longestConsecutive(self, nums):
        nums = set(nums)
        maxlen = 0
        for x in nums:
            if x-1 in nums:
                continue
            cnt = 1
            while x+cnt in nums:
                cnt += 1
            if cnt > maxlen:
                maxlen = cnt
        return maxlen
