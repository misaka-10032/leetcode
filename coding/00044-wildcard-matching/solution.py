# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

* split by *; ignore empty segments
* match every segment greedily; do kmp first match for p in s.
* do exact match in start and end

* Jump table t
  * t[i] means if p[i] fails, jump to t[i]
  * satisfies p[:t[i]] == p[i-t[i]:i]
  * maintain a front pointer k, and a rear pointer j
  * *** p[j] == p[k] would indicate p[k+1] would need to jump back to p[j+1] ***
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def matches(c1, c2):
            return c1 == '?' or c2 == '?' or c1 == c2

        def startswith(s, p):
            if len(s) < len(p):
                return False
            for cs, cp in zip(s, p):
                if not matches(cs, cp):
                    return False
            return True

        def endswith(s, i, p):
            if len(s) - i < len(p):
                return False
            for cs, cp in zip(s[len(s) - len(p):], p):
                if not matches(cs, cp):
                    return False
            return True

        def kmp(s, i, p):
            """ assumes len(p) >= 1 """
            if len(s) - i < len(p):
                return -1

            # build jump table for p
            n = len(s)
            m = len(p)
            t = [0] * (m + 1)

            j = 0
            k = 1
            while k < m:
                if matches(p[j], p[k]):
                    t[k + 1] = j + 1
                    j += 1
                    k += 1
                elif j != 0:
                    j = t[j]
                else:
                    k += 1

            j = i
            k = 0
            while j < n and k < m:
                if matches(s[j], p[k]):
                    j += 1
                    k += 1
                elif k != 0:
                    k = t[k]
                else:
                    j += 1

            return j if k == m else -1

        n = len(s)
        ps = p.split('*')
        if not startswith(s, ps[0]):
            return False

        if len(ps) == 1:
            return n == len(p)

        i = len(ps[0])
        for pp in ps[1:-1]:
            if not pp:
                continue
            i = kmp(s, i, pp)
            if i < 0:
                return False
        return endswith(s, i, ps[-1])
