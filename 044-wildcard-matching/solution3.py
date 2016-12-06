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
        def startswith(i, p):
            """ check if s[i:] starts with p
                ? would count for match """
            if n - i < len(p):
                return False
            for j in xrange(len(p)):
                if not match(s[i+j], p[j]):
                    return False
            return True

        def endswith(i, p):
            """ check if s[i:] ends with p
                ? would count for match """
            if n - i < len(p):
                return False
            m = len(p)
            for j in xrange(m):
                if not match(s[n-m+j], p[j]):
                    return False
            return True

        def match(c1, c2):
            return c1 == c2 or c1 == '?' or c2 == '?'

        def match_str(s1, s2):
            if len(s1) != len(s2):
                return False
            for c1, c2 in zip(s1, s2):
                if not match(c1, c2):
                    return False
            return True

        def kmp(i, p):
            """ try to find p in s[i:]
                return the position of first match.
                -1 if not match """
            if not p:
                return i
            m = len(p)
            t = [0] * (m+1)  # last one is dummy
            k = 0
            j = 1
            while j < m:
                if match(p[j], p[k]):
                    j += 1
                    k += 1
                    t[j] = k
                elif k == 0:
                    j += 1
                else:
                    k = t[k]

            j = i
            k = 0
            while j < n and k < m:
                if match(s[j], p[k]):
                    j += 1
                    k += 1
                elif k == 0:
                    j += 1
                else:
                    k = t[k]

            if k == m:
                return j - m
            else:
                return -1

        if s and not p:
            return False
        if not s and not p:
            return True

        n = len(s)
        ps = p.split('*')

        if len(ps) == 1:
            return match_str(s, p)

        if not startswith(0, ps[0]):
            return False

        i = len(ps[0])
        for pi in xrange(1, len(ps)-1):
            p = ps[pi]
            m = len(p)
            j = kmp(i, p)
            if j < 0:
                return False
            i = j + m

        return endswith(i, ps[-1])
