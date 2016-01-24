# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        num_I = num % 10
        num /= 10
        num_X = num % 10
        num /= 10
        num_C = num % 10
        num /= 10
        num_M = num
        C = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        X = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        I = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        return '%s%s%s%s' % ('M' * num_M, C[num_C], X[num_X], I[num_I])
