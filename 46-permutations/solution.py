# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def _dfs(self, k):
        if k == len(self.nums):
            # need to copy
            self.all.append(list(self.curr))
            return
        for i in self.avail:
            self.curr[k] = self.nums[i]
            self.avail.remove(i)
            self._dfs(k+1)
            self.avail.add(i)
            self.curr[k] = -1

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        self.avail = set(range(len(nums)))
        self.all = []
        self.curr = [-1] * len(nums)
        self.nums = nums
        self._dfs(0)
        return self.all
