# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from collections import Counter


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        best = 0
        n = len(s)
        l = r = 0
        ctr = Counter([s[0]])
        while l <= r < n:
            # don't make assumption about validity here
            while r < n and len(ctr) <= 2:
                r += 1  # try move anyway
                best = max(best, r-l)
                if r == n:
                    break
                ctr[s[r]] += 1
            # either s[l:r+1] becomes invalid
            # or r == n
            while l < r and len(ctr) > 2:
                l += 1
                ctr[s[l-1]] -= 1
                if not ctr[s[l-1]]:
                    del ctr[s[l-1]]
                    break
        # in case of last substr
        best = max(best, r-l)
        return best
