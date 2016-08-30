# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

import numpy as np
from solution import Solution, ListNode


def ll_to_list(ll):
    a = []
    while ll:
        a.append(ll.val)
        ll = ll.next
    return a


def list_to_ll(a):
    if not a:
        return None
    p = head = ListNode(a[0])
    for i in xrange(1, len(a)):
        q = ListNode(a[i])
        p.next = q
        p = q
    return head


def _test_list(a):
    sol = Solution()
    ll = sol.reverseList(list_to_ll(a))
    ra = ll_to_list(ll)
    assert ra == a[::-1]


def test_0():
    _test_list([])
    _test_list([1])


def test_1():
    for n in xrange(100):
        a = np.random.choice(100, n).tolist()
        _test_list(a)
