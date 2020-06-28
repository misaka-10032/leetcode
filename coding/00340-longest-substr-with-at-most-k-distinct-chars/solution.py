# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from collections import Counter


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0

        ctr = Counter()
        front = rear = 0
        n = len(s)
        best = 0
        while rear < n and front < n:
            # increasing phase
            while (front < n and
                   (len(ctr)+1 <= k or s[front] in ctr)):
                ctr[s[front]] += 1
                front += 1
            # current window is [rear, front)
            best = max(best, front-rear)
            # decreasing phase
            ctr[s[rear]] -= 1
            if ctr[s[rear]] == 0:
                del ctr[s[rear]]
            rear += 1
        return best
