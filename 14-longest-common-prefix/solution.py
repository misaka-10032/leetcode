# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        _len = min([len(st) for st in strs])
        strcnt = len(strs)
        cnt = 0
        for i in xrange(_len):
            c = strs[0][i]
            matched = True
            for j in xrange(1, strcnt):
                if strs[j][i] != c:
                    matched = False
                    break
            if not matched:
                break
            cnt += 1
        return strs[0][:cnt]
