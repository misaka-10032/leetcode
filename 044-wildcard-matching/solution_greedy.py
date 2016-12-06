# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        def match(c_s, c_p):
            return c_s == c_p or c_p == '?'

        n_s = len(s)
        n_p = len(p)
        i = j = 0
        s_reg = p_reg = -1

        while i < n_s:
            if j < n_p and p[j] == '*':
                # where to regret
                s_reg = i + 1
                p_reg = j
                j += 1
                continue
            if j < n_p and match(s[i], p[j]):
                i += 1
                j += 1
                continue
            if p_reg >= 0:
                # regret
                i = s_reg
                j = p_reg
            else:
                return False

        while j < n_p and p[j] == '*':
            j += 1

        return j == n_p
