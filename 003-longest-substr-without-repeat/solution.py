# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        appeared = set()
        """ p is front and q is rear. """
        q = 0
        _len = len(s)
        for p in xrange(_len):
            c = s[p]
            if c not in appeared:
                appeared.add(c)
                curr = p - q + 1
                if curr > longest:
                    longest = curr
            else:
                while s[q] != c and q < p:
                    appeared.remove(s[q])
                    q += 1
                if q < p:
                    q += 1
        return longest
