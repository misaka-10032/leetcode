# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from collections import Counter


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t:
            return ''
        i = ii = 0
        jj = len(s)+1
        missing = len(t)
        need = Counter(t)
        for j in xrange(1, len(s)+1):
            if s[j-1] in need:
                if need[s[j-1]] > 0:
                    missing -= 1
                need[s[j-1]] -= 1
            while i < j:
                if s[i] not in need:
                    i += 1
                elif need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                else:
                    break
            if not missing and j-i < jj-ii:
                ii, jj = i, j
        return s[ii:jj] if jj-ii <= len(s) else ''
