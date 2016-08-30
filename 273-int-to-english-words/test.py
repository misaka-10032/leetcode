# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

import numpy as np
from solution import Solution


def ref(num):
    """ https://discuss.leetcode.com/topic/23061/recursive-python """
    to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
    tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
    def words(n):
        if n < 20:
            return to19[n-1:n]
        if n < 100:
            return [tens[n/10-2]] + words(n%10)
        if n < 1000:
            return [to19[n/100-1]] + ['Hundred'] + words(n%100)
        for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
            if n < 1000**(p+1):
                return words(n/1000**p) + [w] + words(n%1000**p)
    return ' '.join(words(num)) or 'Zero'


def test_0():
    sol = Solution()
    assert sol.numberToWords(0) == 'Zero'


def test_1():
    sol = Solution()
    for i in xrange(10):
        lower = 10**i
        upper = 10**(i+1)
        for _ in xrange(100):
            x = np.random.randint(lower, upper)
            assert sol.numberToWords(x) == ref(x), x
