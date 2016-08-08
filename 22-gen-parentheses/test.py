# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    key = []
    assert set(key) == set(sol.generateParenthesis(0))
    key = ['()']
    assert set(key) == set(sol.generateParenthesis(1))


def test_1():
    sol = Solution()
    key = [
      "((()))",
      "(()())",
      "(())()",
      "()(())",
      "()()()",
    ]
    assert set(key) == set(sol.generateParenthesis(3))


def catalan(n):
    """
    https://en.wikipedia.org/wiki/Catalan_number
    :param n:
    :return:
    """
    p = 1
    for k in xrange(2, n+1):
        p *= n+k
    for k in xrange(2, n+1):
        p /= k
    return p


def is_valid(s):
    left = right = 0
    for c in s:
        if c == '(':
            left += 1
        else:
            right += 1
        if left < right:
            return False
    if left != right or left+right != len(s):
        return False
    return True


def test_2():
    sol = Solution()
    for n in xrange(2, 8):
        ans = sol.generateParenthesis(n)
        assert len(ans) == catalan(n), \
            'len(ans) is {}, but catalan({}) is {}'\
                .format(len(ans), n, catalan(n))
        invalid = filter(lambda s: not is_valid(s), ans)
        assert not invalid
