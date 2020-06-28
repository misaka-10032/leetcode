# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_valid(c):
            return 'a' <= c <= 'z' or '0' <= c <= '9'

        i = 0
        j = len(s)-1
        while i < j:
            c1 = s[i].lower()
            if not is_valid(c1):
                i += 1
                continue
            c2 = s[j].lower()
            if not is_valid(c2):
                j -= 1
                continue
            if c1 != c2:
                return False
            i += 1
            j -= 1
        return True
