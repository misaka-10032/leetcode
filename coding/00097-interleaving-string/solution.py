# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l3 != l1 + l2:
            return False

        f = [[False] * (l2+1) for _ in xrange(l1+1)]
        f[0][0] = True
        for i in xrange(1, l1+1):
            f[i][0] = s3[i-1] == s1[i-1] and f[i-1][0]
        for j in xrange(1, l2+1):
            f[0][j] = s3[j-1] == s2[j-1] and f[0][j-1]
        for i in xrange(1, l1+1):
            for j in xrange(1, l2+1):
                f[i][j] = s3[i+j-1] == s1[i-1] and f[i-1][j] or \
                          s3[i+j-1] == s2[j-1] and f[i][j-1]
        return f[l1][l2]
