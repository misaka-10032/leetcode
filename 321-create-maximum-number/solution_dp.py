# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def dp(self, a, f, n, k):
        k = min(n, k)
        for j in xrange(n+1):
            f[j][0] = 0
        for j in xrange(1, k+1):
            f[j][j] = f[j-1][j-1] + a[j-1]
        for i in xrange(1, n+1):
            for j in xrange(0, k+1):
                f[i][j] = max(-1, f[i-1][j], f[i-1][j-1]*10+a[i-1])

    def merge(self, x1, k1, x2, k2):
        def gt(a1, i1, a2, i2):
            while i1 < len(a1) and i2 < len(a2) and a1[i1] == a2[i2]:
                i1 += 1
                i2 += 1
            if i1 == len(a1):
                return False
            if i2 == len(a2):
                return True
            if a1[i1] > a2[i2]:
                return True
            else:
                return False

        if k1 > k2:
            x1, k1, x2, k2 = x2, k2, x1, k1
        a1 = []
        while x1 > 0:
            a1.append(x1 % 10)
            x1 /= 10
        a1 += [0] * (k1-len(a1))
        a1 = a1[::-1]
        a2 = []
        while x2 > 0:
            a2.append(x2 % 10)
            x2 /= 10
        a2 += [0] * (k2-len(a2))
        a2 = a2[::-1]

        r = []
        i1 = i2 = 0
        while i1 < k1 and i2 < k2:
            if gt(a1, i1, a2, i2):
                r.append(a1[i1])
                i1 += 1
            else:
                r.append(a2[i2])
                i2 += 1
        if i1 < k1:
            r += a1[i1:]
        else:
            r += a2[i2:]
        return r

    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        n1 = len(nums1)
        n2 = len(nums2)
        f1 = [[-1] * (k+1) for _ in xrange(n1+1)]
        f2 = [[-1] * (k+1) for _ in xrange(n2+1)]
        self.dp(nums1, f1, n1, k)
        self.dp(nums2, f2, n2, k)
        best = []
        for k1 in xrange(0, k+1):
            k2 = k - k1
            if f1[n1][k1] < 0 or f2[n2][k2] < 0:
                continue
            best = max(best, self.merge(f1[n1][k1], k1, f2[n2][k2], k2))
        return best
