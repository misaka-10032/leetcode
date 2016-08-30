# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'

from solution import Solution


def test():
    sol = Solution()
    assert sol.intToRoman(4) == 'IV'
    assert sol.intToRoman(9) == 'IX'
    assert sol.intToRoman(40) == 'XL'
    assert sol.intToRoman(90) == 'XC'
    assert sol.intToRoman(400) == 'CD'
    assert sol.intToRoman(900) == 'CM'
    assert sol.intToRoman(1954) == 'MCMLIV'
    assert sol.intToRoman(1990) == 'MCMXC'
    assert sol.intToRoman(2014) == 'MMXIV'
