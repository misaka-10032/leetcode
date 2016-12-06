# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        cnt = 0
        vals = sorted(nums)
        for i in xrange(n-2):
            j = i + 1
            k = n - 1
            while j < k:
                if vals[i] + vals[j] + vals[k] < target:
                    cnt += k - j
                    j += 1
                else:
                    k -= 1
        return cnt
