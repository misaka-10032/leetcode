# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'

from solution import Solution


def test_1():
    sol = Solution()
    digits = '23'
    ans = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    assert sorted(sol.letterCombinations(digits)) == sorted(ans)
    digits = '203'
    ans = ['a d', 'a e', 'a f', 'b d', 'b e', 'b f', 'c d', 'c e', 'c f']
    assert sorted(sol.letterCombinations(digits)) == sorted(ans)
    digits = '121131'
    ans = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    assert sorted(sol.letterCombinations(digits)) == sorted(ans)


def test_2():
    sol = Solution()
    digits = ''
    ans = []
    assert sorted(sol.letterCombinations(digits)) == sorted(ans)
