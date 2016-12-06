# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert sol.maxProduct([]) == 0
    assert sol.maxProduct(['a', 'b']) == 1
    assert sol.maxProduct(['a', 'aa', 'aaa']) == 0


def test_1():
    assert sol.maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]) == 16
    assert sol.maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]) == 4
