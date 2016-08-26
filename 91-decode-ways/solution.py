# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def is_valid_1(s):
            return '1' <= s <= '9'

        def is_valid_2(s):
            return 10 <= int(s) <= 26

        for c in s:
            if not '0' <= c <= '9':
                return 0
        if not s:
            return 0
        f = [0] * len(s)
        f[0] = int(is_valid_1(s[0]))

        for i in xrange(1, len(s)):
            if is_valid_1(s[i]):
                f[i] += f[i-1]
            if is_valid_2(s[i-1:i+1]):
                f[i] += f[i-2] if i > 1 else 1
        return f[-1]
