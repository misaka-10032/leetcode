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
        ids = sorted(range(n), key=lambda i: nums[i])
        for i in xrange(n-2):
            ii = ids[i]
            for j in xrange(i+1, n-1):
                jj = ids[j]
                if nums[ii] + nums[jj] >= target and \
                   nums[jj] >= 0:
                    break
                for k in xrange(j+1, n):
                    kk = ids[k]
                    if nums[ii] + nums[jj] + nums[kk] >= target:
                        break
                    cnt += 1
        return cnt
