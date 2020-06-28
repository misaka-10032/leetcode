# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.findSubstring(
        'barfoothefoobarman', ['foo', 'bar']) == [0, 9]
    assert sol.findSubstring('a', ['aa']) == []
    assert sol.findSubstring('a', ['a']) == [0]
    assert sol.findSubstring(
        'ababcdabcd', ['ab', 'ab', 'cd']) == [0, 2]
