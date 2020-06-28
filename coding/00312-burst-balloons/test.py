# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""

from solution import Solution


def test1():
    sol = Solution()
    r, ans = sol.maxCoins([3, 1, 5, 8]), 167
    assert r == ans, '%d != %d' % (r, ans)

def test2():
    sol = Solution()
    r, ans = sol.maxCoins([]), 0
    assert r == ans, '%d != %d' % (r, ans)

