# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        char_list = []
        _len = len(s)
        step = 2 * numRows - 2
        deltas = [2*(numRows-start-1) for start in xrange(numRows)]

        for p in xrange(0, _len, step):
            char_list.append(s[p])
        for start in xrange(1, numRows-1):
            for p in xrange(start, _len, step):
                char_list.append(s[p])
                q = p + deltas[start]
                if 0 <= q < _len:
                    char_list.append(s[q])
        for p in xrange(numRows-1, _len, step):
            char_list.append(s[p])

        return ''.join(char_list)
