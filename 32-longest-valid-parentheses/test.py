# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.longestValidParentheses('') == 0
    assert sol.longestValidParentheses('(') == 0
    assert sol.longestValidParentheses(')') == 0
    assert sol.longestValidParentheses('()') == 2
    assert sol.longestValidParentheses(')(') == 0


def test_1():
    sol = Solution()
    assert sol.longestValidParentheses('(()') == 2
    assert sol.longestValidParentheses(')()())') == 4
    assert sol.longestValidParentheses('))(()()((())))(') == 12
    assert sol.longestValidParentheses('(()))((()))') == 6


def test_2():
    sol = Solution()
    assert sol.longestValidParentheses('()(()') == 2
    assert sol.longestValidParentheses('(()()') == 4


def test_3():
    sol = Solution()
    assert sol.longestValidParentheses(')(((((()())()()))()(()))(') == 22
