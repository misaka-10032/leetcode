# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

import numpy as np
from solution import Solution, MAX_INT


def test_0():
    sol = Solution()
    assert sol.divide(0, 0) == MAX_INT
    assert sol.divide(1, 0) == MAX_INT
    assert sol.divide(0, -12) == 0
    assert sol.divide(-2147483648, -1) == MAX_INT
    assert sol.divide(1004958205, -2137325331) == 0


def test_1():
    sol = Solution()
    dividends = np.random.choice(np.arange(1, 100000), 100, replace=True)
    divisors = np.random.choice(np.arange(1, 1000), 100, replace=True)
    # dividends = dividends[divisors != 0]
    # divisors = divisors[divisors != 0]
    for dividend, divisor in zip(dividends, divisors):
        assert dividend//divisor == sol.divide(dividend, divisor)
