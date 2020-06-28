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
        def build_table(s):
            n = len(s)
            assert n >= 2
            t = [0] * n
            t[0] = -1
            t[1] = 0
            p = 2  # probe
            q = 0  # backup
            while p < n:
                if s[p-1] == s[q]:
                    q += 1
                    t[p] = q
                    p += 1
                elif q != 0:
                    q = t[q]
                else:
                    p += 1
            return t

        if not s:
            return ''
        r = s[::-1]
        t = build_table(s+'#'+r)
        return r[:len(s)-t[-1]-1] + s
