# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        n = len(s)
        r = s[::-1]
        for j in xrange(n):
            if s.startswith(r[j:]):
                return r[:j] + s
