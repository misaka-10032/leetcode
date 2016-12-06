# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums = sorted(nums)
        v_to_i = {}
        for i, v in enumerate(nums):
            v_to_i[v] = i
        res = set()
        for i in xrange(n):
            a = nums[i]
            for j in xrange(i+1, n):
                b = nums[j]
                c = -a-b
                if c in v_to_i:
                    k = v_to_i[c]
                    if k > j:
                        res.add((a, b, c))
        return map(list, res)
