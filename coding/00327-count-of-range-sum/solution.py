# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class BITree(object):
    def __init__(self, sz):
        self.sums = [0] * (sz+1)

    def inc(self, i, dv):
        k = i + 1
        while k < len(self.sums):
            self.sums[k] += dv
            k += k & -k

    def prefix_sum(self, i):
        k = i + 1
        s = 0
        while k > 0:
            s += self.sums[k]
            k -= k & -k
        return s

    def range_sum(self, i, j):
        return self.prefix_sum(j) - self.prefix_sum(i-1)


class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        if not nums:
            return 0
        nums = list(nums)  # copy it

        vals = set()
        vals |= {lower, upper}
        for i in xrange(len(nums)):
            nums[i] += nums[i-1] if i > 0 else 0
            vals |= {nums[i]+lower, nums[i], nums[i]+upper}

        v2i = {}
        for i, v in enumerate(sorted(vals)):
            v2i[v] = i

        cnt = 0
        # bit maintains frequency for vals
        bit = BITree(len(vals))
        for i in xrange(len(nums)-1, -1, -1):
            prev = nums[i-1] if i > 0 else 0
            bit.inc(v2i[nums[i]], 1)   # count for i
            li = v2i[prev+lower]  # index of lower bound
            ui = v2i[prev+upper]  # index of upper bound
            cnt += bit.range_sum(li, ui)
        return cnt
