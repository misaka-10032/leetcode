# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution, ListNode


def test_0():
    sol = Solution()
    assert not sol.hasCycle(None)

    n1 = ListNode(1)
    n1.next = n1
    assert sol.hasCycle(n1)

    n1 = ListNode(1)
    assert not sol.hasCycle(n1)

    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2
    assert not sol.hasCycle(n1)


def test_1():
    sol = Solution()
    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2
    n3 = ListNode(3)
    n2.next = n3
    n4 = ListNode(4)
    n3.next = n4
    n5 = ListNode(5)
    n4.next = n5
    n5.next = n2
    assert sol.hasCycle(n1)
