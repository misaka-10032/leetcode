# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'

from solution import Solution


def test():
    sol = Solution()
    assert sol.myAtoi('  123 ') == 123
    assert sol.myAtoi(' +255 ') == 255
    assert sol.myAtoi(' -244sfa ') == -244
    assert sol.myAtoi('- 123') == 0
    assert sol.myAtoi(' + ') == 0
    assert sol.myAtoi(' 2147483648sas') == 2147483647
    assert sol.myAtoi(' -2147483649gg') == -2147483648
