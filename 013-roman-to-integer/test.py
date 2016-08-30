# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'

from solution import Solution


def test():
    sol = Solution()
    assert sol.romanToInt('IV') == 4
    assert sol.romanToInt('IX') == 9
    assert sol.romanToInt('XL') == 40
    assert sol.romanToInt('XC') == 90
    assert sol.romanToInt('CD') == 400
    assert sol.romanToInt('CM') == 900
    assert sol.romanToInt('MCMLIV') == 1954
    assert sol.romanToInt('MCMXC') == 1990
    assert sol.romanToInt('MMXIV') == 2014
