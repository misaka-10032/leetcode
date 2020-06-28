# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return [1]
        digits = digits[::-1]
        n = len(digits)
        digits[0] += 1
        for i in xrange(n-1):
            if digits[i] < 10:
                break
            digits[i+1] += digits[i] // 10
            digits[i] %= 10
        if digits[-1] >= 10:
            digits.append(digits[-1]//10)
            digits[-2] %= 10
        return digits[::-1]
