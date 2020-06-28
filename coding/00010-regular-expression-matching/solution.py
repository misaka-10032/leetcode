"""
* f[i][j] means if s[:i] matches p[:j]
* if p[j-1] is not '*', it's easy
* if p[j-1] is '*', here are the following cases
* repeat start
  * ab
  * .*
* repeat mid
  * abb
  * .*
* ignore
  * a
  * ab*
* Init
  * f[0][0] = True
  * f[0][j] = p[j-1] == '*' and f[0][j-2]
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        def matches(c1, c2):
            return c1 == '.' or c2 == '.' or c1 == c2

        m = len(s)
        n = len(p)
        f = [[False] * (n + 1) for _ in xrange(m + 1)]
        f[0][0] = True
        for j in xrange(2, n + 1):
            f[0][j] = p[j - 1] == '*' and f[0][j - 2]

        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if p[j - 1] != '*':
                    f[i][j] = matches(s[i - 1], p[j - 1]) and f[i - 1][j - 1]
                else:
                    if matches(s[i - 1], p[j - 2]) and (f[i - 1][j - 1] or f[i - 1][j]):
                        f[i][j] = True
                        continue
                    if j >= 2 and f[i][j - 2]:
                        f[i][j] = True
                        continue
        return f[m][n]
