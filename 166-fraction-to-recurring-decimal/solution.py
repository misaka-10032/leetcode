# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return '0'

        sign = (numerator < 0) != (denominator < 0)
        a = abs(numerator)
        b = abs(denominator)
        whole = a // b
        a -= whole * b

        # stores str
        frac = []
        # maps a to previous location
        loc = {}
        recur = -1
        while a > 0:
            a *= 10
            if a in loc:
                recur = loc[a]
                break
            loc[a] = len(frac)
            q = a // b
            a -= q * b
            frac.append(str(q))

        if recur < 0:
            s_frac = ''.join(frac)
        else:
            s_frac = ''.join(frac[:recur]) + \
                     '(' + ''.join(frac[recur:]) + ')'

        res = '-' if sign else ''
        res += str(whole)
        if s_frac:
            res += '.' + s_frac
        return res
