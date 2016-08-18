# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        def insert(v):
            b = v2b(v)
            for bb in neighbors(b):
                if bb not in buckets:
                    continue
                if abs(buckets[bb] - v) <= t:
                    return False
            buckets[b] = v
            return True

        def remove(v):
            buckets.pop(v2b(v))

        v2b = (lambda x: x) if t == 0 else (lambda x: x//t)
        neighbors = (lambda b: [b]) if t == 0 else (lambda b: [b-1, b, b+1])
        buckets = {}
        cnt = 0
        for i, v in enumerate(nums):
            cnt += 1
            if cnt > k+1:
                remove(nums[i-k-1])
                cnt -= 1
            if not insert(v):
                return True
        return False
