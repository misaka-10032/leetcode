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
        if not p:
            if not s:
                return True
            else:
                return False

        i_s = i_p = 0
        # p_star is the position of star
        # s_star is the position in s that doesn't accept *
        p_star = s_star = -1
        while i_s < len(s):
            if i_p < len(p) and (s[i_s] == p[i_p] or p[i_p] == '?'):
                i_s += 1
                i_p += 1
                continue
            if i_p < len(p) and p[i_p] == '*':  # try ignore first
                s_star = i_s
                p_star = i_p
                i_p += 1
                continue
            if p_star >= 0:  # still able to regret
                # go back and ask * to take one more
                i_s = s_star = s_star + 1
                i_p = p_star + 1
                continue
            return False

        while i_p < len(p):
            if p[i_p] != '*':
                return False
            i_p += 1
        return True
