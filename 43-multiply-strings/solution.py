# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        ith in num1 and jth in num2 maps to (i+j)th in num

        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'

        num = [0] * (len(num1) + len(num2))
        for i, x2 in enumerate(reversed(num2)):
            for j, x1 in enumerate(reversed(num1)):
                num[i+j] += int(x1) * int(x2)
                num[i+j+1] += num[i+j] / 10
                num[i+j] %= 10
        for i in xrange(len(num)-1):
            num[i+1] += num[i] / 10
            num[i] %= 10
        while len(num) > 1 and not num[-1]:
            num.pop()
        return ''.join(map(str, num[::-1]))
