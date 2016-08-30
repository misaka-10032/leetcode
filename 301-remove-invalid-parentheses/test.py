# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.removeInvalidParentheses('') == ['']
    assert sol.removeInvalidParentheses('(') == ['']
    assert sol.removeInvalidParentheses(')') == ['']
    assert sol.removeInvalidParentheses('(a)') == ['(a)']


def test_1():
    sol = Solution()
    s = '()())()'
    tgt = ['()()()', '(())()']
    assert sorted(sol.removeInvalidParentheses(s)) == sorted(tgt)


def test_2():
    sol = Solution()
    s = 'a)b)c)d)e)f)g)h)i)j)k)l)m)n)o)p)(((((((((((((((((((('
    tgt = ['abcdefghijklmnop']
    assert sorted(sol.removeInvalidParentheses(s)) == sorted(tgt)


def test_3():
    sol = Solution()
    s = ')a' * 100
    tgt = ['a'*100]
    assert sorted(sol.removeInvalidParentheses(s)) == sorted(tgt)


def test_4():
    sol = Solution()
    s = ')()('
    tgt = ["()"]
    assert sorted(sol.removeInvalidParentheses(s)) == sorted(tgt)


def test_5():
    # counter example of grouping alg
    sol = Solution()
    s = ')()))())))'
    tgt = ['(())', '()()']
    assert sorted(sol.removeInvalidParentheses(s)) == sorted(tgt)
