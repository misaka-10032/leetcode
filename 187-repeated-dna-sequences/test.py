# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert sol.findRepeatedDnaSequences('') == []
    assert sol.findRepeatedDnaSequences('a') == []
    assert sol.findRepeatedDnaSequences('AAAAAAAAAA') == []
    assert sol.findRepeatedDnaSequences('AAAAAAAAAAA') == ['AAAAAAAAAA']


def test_1():
    s = 'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'
    tgt = ["AAAAACCCCC", "CCCCCAAAAA"]
    assert sorted(sol.findRepeatedDnaSequences(s)) == sorted(tgt)
