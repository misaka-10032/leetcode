# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

MAX_INT = (1 << 31) - 1
MIN_INT = -(1 << 31)


class Solution(object):
    def divide(self, dividend, divisor):
        """
        Exponential probe
        Take sign separately
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return MAX_INT

        if dividend == 0:
            return 0

        sign = (dividend < 0 < divisor) or \
               (dividend > 0 > divisor)
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0

        probe = divisor
        base = 1
        while probe << 1 <= dividend:
            probe <<= 1
            base <<= 1

        while dividend > 0 and probe >= divisor:
            if dividend - probe >= 0:
                dividend -= probe
                quotient += base
            else:
                probe >>= 1
                base >>= 1

        # This problem uses round-to-zero.
        # if dividend > 0 and sign:
        #     quotient += 1
        quotient = -quotient if sign else quotient

        if quotient > MAX_INT or quotient < MIN_INT:
            quotient = MAX_INT

        return quotient
