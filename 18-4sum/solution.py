# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        nums_cnt = len(nums)
        ans = []
        _numsi = None
        for i in xrange(nums_cnt):
            """ Eliminate same numbers """
            prev_numsi = _numsi
            _numsi = nums[i]
            if _numsi == prev_numsi:
                continue
            if 4 * _numsi > target:
                break
            target3 = target - _numsi

            _numsj = None  # init here, not at very beginning.
            for j in xrange(i+1, nums_cnt):
                prev_numsj = _numsj
                _numsj = nums[j]
                if _numsj == prev_numsj:
                    continue
                if 3 * _numsj > target3:
                    break
                target2 = target3 - _numsj

                p, q = j+1, nums_cnt-1
                while p < q:
                    _numsp = nums[p]
                    _numsq = nums[q]
                    if _numsp + _numsq == target2:
                        ans.append([_numsi, _numsj, _numsp, _numsq])
                        while p < q and nums[p] == _numsp:
                            p += 1
                        while p < q and nums[q] == _numsq:
                            q -= 1
                    _numsq = nums[q]
                    while p < q and nums[p] + _numsq < target2:
                        p += 1
                    _numsp = nums[p]
                    while p < q and _numsp + nums[q] > target2:
                        q -= 1
        return ans
