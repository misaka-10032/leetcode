# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution, RandomListNode
sol = Solution()


def make_nodes(vals):
    n = {}
    for v in vals:
        n[v] = RandomListNode(v)
    return n


def equal(l1, l2):
    p = l1
    q = l2
    while p:
        if not q:
            return False
        if p.label != q.label:
            return False
        if p.random and not q.random or \
           not p.random and q.random:
            return False
        if p.random and q.random and \
           p.label != q.label:
            return False
        p = p.next
        q = q.next
    return not q


def test_0():
    assert sol.copyRandomList(None) is None
    n = make_nodes([1])
    assert equal(sol.copyRandomList(n[1]), n[1])


def test_1():
    n = make_nodes([1, 2, 3, 4, 5])
    n[1].next = n[2]
    n[2].next = n[3]
    n[3].next = n[4]
    n[4].next = n[5]
    n[1].random = n[5]
    n[2].random = n[2]
    n[3].random = None
    n[4].random = n[1]
    n[5].random = n[1]
    assert equal(sol.copyRandomList(n[1]), n[1])
