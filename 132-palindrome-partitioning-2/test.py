# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.minCut('a') == 0
    assert sol.minCut('') == 0
    assert sol.minCut('aa') == 0


def test_1():
    sol = Solution()
    assert sol.minCut('aab') == 1
    assert sol.minCut('aabb') == 1
    assert sol.minCut('aabc') == 2
    assert sol.minCut('abbacc') == 1
    assert sol.minCut('aabbaacec') == 1


def test_2():
    sol = Solution()
    assert sol.minCut("apjesgpsxoeiokmqmfgvjslcjukb"
                      "qxpsobyhjpbgdfruqdkeiszrlmtw"
                      "gfxyfostpqczidfljwfbbrflkgdv"
                      "tytbgqalguewnhvvmcgxboycffop"
                      "mtmhtfizxkmeftcucxpobxmelmjt"
                      "uzigsxnncxpaibgpuijwhankxbpl"
                      "pyejxmrrjgeoevqozwdtgospohzn"
                      "koyzocjlracchjqnggbfeebmuvbi"
                      "cbvmpuleywrpzwsihivnrwtxcukw"
                      "plgtobhgxukwrdlszfaiqxwjvrgx"
                      "nsveedxseeyeykarqnjrtlaliyud"
                      "pacctzizcftjlunlgnfwcqqxcqik"
                      "ocqffsjyurzwysfjmswvhbrmshju"
                      "zsgpwyubtfbnwajuvrfhlccvfwhx"
                      "fqthkcwhatktymgxostjlztwdxri"
                      "tygbrbibdgkezvzajizxasjnrcjw"
                      "zdfvdnwwqeyumkamhzoqhnqjfzwz"
                      "bixclcxqrtniznemxeahfozp") == 452


def test_3():
    sol = Solution()
    assert sol.minCut('a'*1500) == 0
