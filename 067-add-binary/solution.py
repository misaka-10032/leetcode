# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def to_digit(s):
            return ord(s) - ord('0')

        def to_chr(x):
            return chr(x + ord('0'))

        a, b = sorted([a[::-1], b[::-1]], key=len)

        res = []
        c = 0
        for i in xrange(len(a)):
            aa = to_digit(a[i])
            bb = to_digit(b[i])
            v = aa + bb + c
            c = v >> 1
            res.append(to_chr(v & 1))
        for i in xrange(len(a), len(b)):
            bb = to_digit(b[i])
            v = bb + c
            c = v >> 1
            res.append(to_chr(v & 1))
        if c:
            res.append('1')
        return ''.join(res)[::-1]
