# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def proceed(k, j):
            """ Begin proceeding from k to j, inclusive, exclusive.
                Returns operand, new location. """
            v = 0
            l = k
            if '0' <= s[k] <= '9':
                while l < j and '0' <= s[l] <= '9':
                    l += 1
                v = int(s[k:l])
            elif s[k] == '(':
                cnt = 1
                l = k + 1
                while l < j and cnt > 0:
                    if s[l] == '(':
                        cnt += 1
                    elif s[l] == ')':
                        cnt -= 1
                    l += 1
                v = compute(k+1, l-1)
            return v, l

        def compute(i, j):
            """ Compute inside [i, j) """
            k = i
            op1 = 0
            op = '+'
            while k < j:
                op2 = 1
                l = k
                while True:
                    op3, l = proceed(l, j)
                    op2 *= op3
                    if l >= j or s[l] != '*':
                        break
                    l += 1
                if op == '+':
                    op1 += op2
                else:
                    op1 -= op2
                if l < j:
                    op = s[l]
                k = l + 1
            return op1

        # get rid of blanks
        s = s.replace(' ', '')
        if not s:
            return 0
        return compute(0, len(s))
