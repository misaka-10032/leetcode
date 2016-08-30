# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        _len = len(nums)
        min_delta = int((1 << 31) - 1)
        closest = 0
        k = 0
        while k < _len:
            _numsk = nums[k]
            if _numsk * 3 > target + min_delta:
                break
            target2 = target - nums[k]
            i, j = k+1, _len-1
            while i < j:
                if nums[i] + nums[j] == target2:
                    return target
                while i < j:
                    s2 = nums[i] + nums[j]
                    if s2 >= target2:
                        break
                    s3 = s2 + _numsk
                    delta = abs(s3 - target)
                    if delta < min_delta:
                        min_delta = delta
                        closest = s3
                    i += 1
                while i < j:
                    s2 = nums[i] + nums[j]
                    if s2 <= target2:
                        break
                    s3 = s2 + _numsk
                    delta = abs(s3 - target)
                    if delta < min_delta:
                        min_delta = delta
                        closest = s3
                    j -= 1
            while k < _len and nums[k] == _numsk:
                k += 1
        return closest
