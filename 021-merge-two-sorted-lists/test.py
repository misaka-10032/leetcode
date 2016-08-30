# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution, ListNode


def test_1():
    sol = Solution()
    l1 = ListNode(1)
    p = ListNode(3); l1.next = p; q = p
    p = ListNode(5); q.next = p; q = p
    p = ListNode(5); q.next = p; q = p

    l2 = ListNode(0)
    p = ListNode(2); l2.next = p; q = p
    p = ListNode(4); q.next = p; q = p

    p = sol.mergeTwoLists(l1, l2)
    assert p.val == 0; p = p.next
    assert p.val == 1; p = p.next
    assert p.val == 2; p = p.next
    assert p.val == 3; p = p.next
    assert p.val == 4; p = p.next
    assert p.val == 5; p = p.next
    assert p.val == 5; p = p.next
    assert p is None


def test_2():
    sol = Solution()
    l1 = ListNode(1)
    p = ListNode(3); l1.next = p; q = p
    p = ListNode(5); q.next = p; q = p
    p = ListNode(5); q.next = p; q = p

    l2 = ListNode(0)
    p = ListNode(2); l2.next = p; q = p
    p = ListNode(4); q.next = p; q = p

    p = sol.mergeTwoLists(l2, l1)
    assert p.val == 0; p = p.next
    assert p.val == 1; p = p.next
    assert p.val == 2; p = p.next
    assert p.val == 3; p = p.next
    assert p.val == 4; p = p.next
    assert p.val == 5; p = p.next
    assert p.val == 5; p = p.next
    assert p is None


def test_3():
    sol = Solution()
    assert sol.mergeTwoLists(None, None) is None


def test_4():
    sol = Solution()
    l1 = ListNode(1)
    p = ListNode(3); l1.next = p; q = p
    p = ListNode(5); q.next = p; q = p
    p = ListNode(5); q.next = p; q = p

    p = sol.mergeTwoLists(l1, None)
    assert p.val == 1; p = p.next
    assert p.val == 3; p = p.next
    assert p.val == 5; p = p.next
    assert p.val == 5; p = p.next
    assert p is None


def test_5():
    sol = Solution()
    l1 = ListNode(1)
    p = ListNode(3); l1.next = p; q = p
    p = ListNode(5); q.next = p; q = p
    p = ListNode(5); q.next = p; q = p

    p = sol.mergeTwoLists(None, l1)
    assert p.val == 1; p = p.next
    assert p.val == 3; p = p.next
    assert p.val == 5; p = p.next
    assert p.val == 5; p = p.next
    assert p is None
