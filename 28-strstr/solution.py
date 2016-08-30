# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        Naive matching

        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l_needle = len(needle)
        l_haystack = len(haystack)
        if l_haystack < l_needle:
            return -1
        if l_needle == 0:
            return 0
        for i in xrange(len(haystack)):
            if i+len(needle) > len(haystack):
                break
            match = True
            for j in xrange(len(needle)):
                if haystack[i+j] != needle[j]:
                    match = False
                    break
            if match:
                return i
        return -1
