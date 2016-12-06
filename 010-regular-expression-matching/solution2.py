# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

* let f[i][j] be if s[:i] matches p[:j]
* consider if p[j] is * or not
  * if it's not, f[i][j] = f[i-1][j-1] and match(s[i-1], p[j-1])
  * otherwise, consider three cases
* no-repeat: f[i][j] |= f[i][j-1]
  * `aa` vs `aa*`
* repeat: f[i][j] |= f[i-1][j] and match(s[i-1], p[j-2])
  * `aaa` vs `aa*`
* ignore: f[i][j] |= f[i][j-2]
  * `a` vs `ab*`
* init
  * f[i][j] = False
  * f[<=0][<=0] = True
  * f[0][>0] = True if p is like a*b*c*...
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        def match(cs, cp):
            return cp == '.' or cs == cp

        ns = len(s)
        np = len(p)
        f = [[False] * (np + 1) for _ in xrange(ns + 1)]
        f[0][0] = True
        for j in xrange(2, np + 1, 2):
            f[0][j] = p[j - 1] == '*' and f[0][j - 2]
        for i in xrange(1, ns + 1):
            for j in xrange(1, np + 1):
                if p[j - 1] != '*':
                    f[i][j] = f[i - 1][j - 1] and match(s[i - 1], p[j - 1])
                    continue
                f[i][j] |= f[i][j - 1]
                f[i][j] |= f[i - 1][j] and j > 1 and match(s[i - 1], p[j - 2])
                f[i][j] |= j > 1 and f[i][j - 2]
        return f[ns][np]
