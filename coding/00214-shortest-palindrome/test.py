# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

import numpy as np
from solution import Solution
from solution_naive import Solution as Ref

sol = Solution()
ref = Ref()


def test_0():
    assert sol.shortestPalindrome('') == ''
    assert sol.shortestPalindrome('a') == 'a'
    assert sol.shortestPalindrome('aa') == 'aa'
    assert sol.shortestPalindrome('ab') == 'bab'


def test_1():
    assert sol.shortestPalindrome('dedcba') == 'abcdedcba'


def test_2():
    assert sol.shortestPalindrome('aa'+'ba'*10000) == \
        'ab'*10000+'aa'+'ba'*10000


def test_3():
    assert sol.shortestPalindrome('abaab') == 'baabaab'


def test_4():
    assert sol.shortestPalindrome('abcd') == 'dcbabcd'


def test_5():
    assert sol.shortestPalindrome('aacecaaa') == 'aaacecaaa'


def test_ref():
    for _ in xrange(1000):
        a = np.random.choice(26, 10).tolist()
        s = ''.join(map(lambda x: chr(x+ord('a')), a))
        ans = sol.shortestPalindrome(s)
        tgt = ref.shortestPalindrome(s)
        assert ans == tgt, (s, ans, tgt)
