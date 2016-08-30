# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

import numpy as np
from solution import Solution


def test_0():
    sol = Solution()
    assert sol.multiply('0', '123') == '0'
    assert sol.multiply('123', '0') == '0'
    assert sol.multiply('0', '0') == '0'


def test_1():
    sol = Solution()
    for _ in xrange(100):
        n1 = np.random.randint(100000)
        n2 = np.random.randint(100000)
        n = n1 * n2
        assert sol.multiply(str(n1), str(n2)) == str(n)


def test_2():
    sol = Solution()
    n1 = "34951988787875060539794079748961576784564363070245114613707595672441019547866090721102583434"
    n2 = "16659770238224335056461144790912689758874618241978614940512513991166165549575662545139401664"
    key = "5822921025749915852214668758391140049878435518175951031971353065579437743518919000057828559" \
          "00775852608271536564205447032568312955070157163090097380822461926168774347387939575398434176"
    assert sol.multiply(n1, n2) == key
