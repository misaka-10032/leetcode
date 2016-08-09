# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def _dfs(self, k, nums):
        """
        Swap k with something after.
        Don't swap the same numbers.
        Copy on recursion.

        :param k:
        :return:
        """
        if k == len(nums):
            self.all.append(nums)
            return

        self._dfs(k+1, list(nums))
        # iterate all next permutations
        for i in xrange(k+1, len(nums)):
            if nums[k] != nums[i]:
                nums[k], nums[i] = nums[i], nums[k]
                self._dfs(k+1, list(nums))

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        self.all = []
        self._dfs(0, sorted(nums))
        return self.all
