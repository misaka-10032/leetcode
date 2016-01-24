# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'

from solution import Solution, ListNode


def insert_ll(ll, x):
    """
    insert x into front of linked-list ll
    """
    node = ListNode(x)
    node.next = ll
    return node


def test_1():
    """
    243 + 564 = 807
    """
    sol = Solution()
    l1 = ListNode(2)
    l1 = insert_ll(l1, 4)
    l1 = insert_ll(l1, 3)
    l2 = ListNode(5)
    l2 = insert_ll(l2, 6)
    l2 = insert_ll(l2, 4)
    l = sol.addTwoNumbers(l1, l2)
    p = l
    assert p.val == 7
    p = p.next
    assert p.val == 0
    p = p.next
    assert p.val == 8
    p = p.next
    assert not p


def test_2():
    """
    7 + 6 = 13
    """
    sol = Solution()
    l1 = ListNode(7)
    l2 = ListNode(6)
    l = sol.addTwoNumbers(l1, l2)
    p = l
    assert p.val == 3
    p = p.next
    assert p.val == 1
    p = p.next
    assert not p


def test_3():
    """
    8 + 94 = 102
    """
    sol = Solution()
    l1 = ListNode(8)
    l2 = ListNode(9)
    l2 = insert_ll(l2, 4)
    l = sol.addTwoNumbers(l1, l2)
    p = l
    assert p.val == 2
    p = p.next
    assert p.val == 0
    p = p.next
    assert p.val == 1
    p = p.next
    assert not p
