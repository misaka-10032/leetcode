# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.removeDuplicateLetters('') == ''
    assert sol.removeDuplicateLetters('a') == 'a'


def test_1():
    sol = Solution()
    assert sol.removeDuplicateLetters('bcabc') == 'abc'
    assert sol.removeDuplicateLetters('cbacdcbc') == 'acdb'


def test_2():
    sol = Solution()
    assert sol.removeDuplicateLetters('bdcdecda') == 'bcdea'
    assert sol.removeDuplicateLetters('bdcdfecdaf') == 'bcdeaf'


def test_3():
    sol = Solution()
    assert sol.removeDuplicateLetters('baa') == 'ba'


def test_4():
    sol = Solution()
    assert sol.removeDuplicateLetters('bddbccd') == 'bcd'


def test_5():
    sol = Solution()
    assert sol.removeDuplicateLetters('abacb') == 'abc'
