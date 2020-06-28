# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def pick(self, nums, k):
        r = []
        for i, x in enumerate(nums):
            """ regret """
            while r and r[-1] < x and \
                  len(r) - 1 + len(nums) - i >= k:
                r.pop()
            if len(r) < k:
                r.append(x)
        return r

    def merge(self, a1, k1, a2, k2):
        def gt(a1, i1, a2, i2):
            while i1 < len(a1) and i2 < len(a2) and a1[i1] == a2[i2]:
                i1 += 1
                i2 += 1
            if i1 == len(a1):
                return False
            if i2 == len(a2):
                return True
            if a1[i1] > a2[i2]:
                return True
            else:
                return False

        r = []
        i1 = i2 = 0
        while i1 < k1 and i2 < k2:
            if gt(a1, i1, a2, i2):
                r.append(a1[i1])
                i1 += 1
            else:
                r.append(a2[i2])
                i2 += 1
        if i1 < k1:
            r += a1[i1:]
        else:
            r += a2[i2:]
        return r

    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        best = []
        for k1 in xrange(0, k+1):
            k2 = k - k1
            if k1 > len(nums1) or k2 > len(nums2):
                continue
            a1 = self.pick(nums1, k1)
            a2 = self.pick(nums2, k2)
            best = max(best, self.merge(a1, k1, a2, k2))
        return best
