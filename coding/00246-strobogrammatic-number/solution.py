# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        n = len(num)
        for i in xrange(n):
            if num[i] not in map:
                return False
            if map[num[i]] != num[n-i-1]:
                return False
        return True
