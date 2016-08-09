# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test():
    sol = Solution()
    assert sol.countAndSay(1) == '1'
    assert sol.countAndSay(2) == '11'
    assert sol.countAndSay(3) == '21'
    assert sol.countAndSay(4) == '1211'
    assert sol.countAndSay(5) == '111221'
    assert sol.countAndSay(6) == '312211'
    assert sol.countAndSay(7) == '13112221'
    assert sol.countAndSay(8) == '1113213211'
    assert sol.countAndSay(9) == '31131211131221'
    assert sol.countAndSay(10) == '13211311123113112211'
