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
        def _match(c_s, c_p):
            return c_s == c_p or c_p == '?'

        def _startswith(s, p):
            if len(s) < len(p):
                return False
            for i in xrange(len(p)):
                if not _match(s[i], p[i]):
                    return False
            return True

        def _endswith(s, p, start):
            if len(s) - start < len(p):
                return False
            for i in xrange(len(p)):
                if not _match(s[-i-1], p[-i-1]):
                    return False
            return True

        def _find(s, p, start):
            """
            idea
            """
            m = len(s)
            n = len(p)
            if m - start < n:
                return -1

            # build table
            t = [0] * (n+1)
            i = 1
            j = 0
            while i < n:
                if _match(p[j], p[i]) or _match(p[i], p[j]):
                    i += 1
                    j += 1
                    t[i] = j
                elif j == 0:
                    i += 1
                else:
                    j = t[j]

            # match
            i = start
            j = 0
            while i < m and j < n:
                if _match(s[i], p[j]):
                    i += 1
                    j += 1
                elif j == 0:
                    i += 1
                else:
                    j = t[j]

            return i - n if j == n else -1

        def match1(s, p):
            pos = p.find('*')
            if pos < 0:
                return len(s) == len(p) and _startswith(s, p)
            return _startswith(s, p[:pos]) and \
                   _endswith(s, p[pos+1:], pos)

        ps = p.split('*')

        if len(ps) <= 2:
            return match1(s, p)

        if not _startswith(s, ps[0]):
            return False

        q = len(ps[0])
        n = len(ps)
        for i in xrange(1, n-1):
            q = _find(s, ps[i], q)
            if q < 0:
                return False
            q += len(ps[i])

        return _endswith(s, ps[-1], q)
