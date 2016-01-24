# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'

from solution import Solution


def test():
    sol = Solution()
    sol.maxArea([1, 2, 8, 9, 8, 2, 1]) == 16
    sol.maxArea([1, 2, 3, 4, 3, 2, 1]) == 8
