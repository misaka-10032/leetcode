# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'


class Solution(object):
    def _probe(self, s, p, q):
        """
        Probe palindrome starting from (p, q)
        :param s:
        :param p:
        :param q:
        :return: (p, q) where s[p:q] would be the longest.
        """
        _len = len(s)
        while p >= 0 and q < _len and s[p] == s[q]:
            p -= 1
            q += 1
        return p + 1, q

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        _len = len(s)
        max_len = 0
        max_p = None
        i = 0
        while True:
            if i + max_len / 2 >= _len:
                break
            """ Case 1: len is odd """
            p, q = self._probe(s, i, i)
            new_len = q - p
            if new_len > max_len:
                max_len = new_len
                max_p = p
            """ Case 2: len is even """
            p, q = self._probe(s, i, i + 1)
            new_len = q - p
            if new_len > max_len:
                max_len = new_len
                max_p = p
            """ next iter """
            i += 1
        return s[max_p:max_p+max_len] if max_p is not None else None
