# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution

sol = Solution()


def int_to_digits(x):
    # construct as low to high
    a = []
    while x > 0:
        a.append(x % 10)
        x //= 10
    # convert
    return a[::-1]


def digits_to_int(a):
    # a is high to low
    x = 0
    for d in a:
        x *= 10
        x += d
    return x


def test_0():
    assert sol.plusOne([]) == [1]
    assert sol.plusOne([0]) == [1]
    assert sol.plusOne([1]) == [2]
    assert sol.plusOne([9]) == [1, 0]


def test_1():
    for x in xrange(1000):
        a = int_to_digits(x)
        a = sol.plusOne(a)
        assert x+1 == digits_to_int(a)
