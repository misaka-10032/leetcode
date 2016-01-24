# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        _len = len(nums)
        sol = []
        k = 0
        while k < _len:
            _numsk = nums[k]
            if _numsk > 0:
                break
            target = -_numsk
            i, j = k+1, _len-1
            while i < j:
                _numsi = nums[i]
                _numsj = nums[j]
                if _numsi + _numsj == target:
                    sol.append([_numsk, _numsi, _numsj])
                    while i < j and nums[i] == _numsi:
                        i += 1
                    while i < j and nums[j] == _numsj:
                        j -= 1
                while i < j and nums[i] + nums[j] < target:
                    i += 1
                while i < j and nums[i] + nums[j] > target:
                    j -= 1
            while k < _len and nums[k] == _numsk:
                k += 1
        return sol
