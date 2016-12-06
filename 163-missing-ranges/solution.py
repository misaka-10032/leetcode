# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        def tuple_to_str(range):
            l, r = range
            if l == r:
                return str(l)
            else:
                return '->'.join([str(l), str(r)])

        next = lower
        res = []
        for x in nums:
            if x == next:
                next = x + 1
            else:
                res.append((next, x-1))
                next = x + 1
        if upper >= next:
            res.append((next, upper))
        return map(tuple_to_str, res)
