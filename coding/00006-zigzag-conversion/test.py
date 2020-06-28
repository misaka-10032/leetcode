# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'

from solution import Solution


def test():
    sol = Solution()
    assert sol.convert('KLSDFJIOEJWF', 1) == 'KLSDFJIOEJWF'
    assert sol.convert('ababababa', 2) == 'aaaaabbbb'
    assert sol.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
    assert sol.convert('abcdefabcdefab', 4) == 'aaabfbfbcecedd'
