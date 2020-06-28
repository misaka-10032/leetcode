# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        def range_to_str(r):
            lb, ub = r
            if lb == ub:
                return str(lb)
            else:
                return str(lb) + '->' + str(ub)

        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        n = len(nums)
        ranges = []
        lb = ub = nums[0]
        for i in xrange(1, n):
            if nums[i] == nums[i-1] + 1:
                ub += 1
            else:
                ranges.append((lb, ub))
                lb = ub = nums[i]
        ranges.append((lb, ub))
        return map(range_to_str, ranges)
