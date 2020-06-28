# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.groupAnagrams([]) == []
    assert sol.groupAnagrams(['a']) == [['a']]


def test_1():
    sol = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    tgt = [["ate", "eat", "tea"],
           ["nat", "tan"],
           ["bat"]]
    for i in xrange(len(tgt)):
        tgt[i] = sorted(tgt[i])
    ans = sol.groupAnagrams(strs)
    for i in xrange(len(ans)):
        ans[i] = sorted(ans[i])
    assert sorted(ans) == sorted(tgt)
