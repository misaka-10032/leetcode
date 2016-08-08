# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution, ListNode


def test():
    sol = Solution()
    head = ListNode(1)
    p = ListNode(2); head.next = p; q = p
    p = ListNode(3); q.next = p; q = p
    p = ListNode(4); q.next = p; q = p
    p = ListNode(5); q.next = p; q = p
    p = sol.removeNthFromEnd(head, 2)
    assert p.val == 1; p = p.next
    assert p.val == 2; p = p.next
    assert p.val == 3; p = p.next
    assert p.val == 5; p = p.next
    assert p is None


def test_1():
    # remove head
    sol = Solution()
    head = ListNode(1)
    p = ListNode(2); head.next = p; q = p
    p = ListNode(3); q.next = p; q = p
    p = ListNode(4); q.next = p; q = p
    p = ListNode(5); q.next = p; q = p
    p = sol.removeNthFromEnd(head, 5)
    assert p.val == 2; p = p.next
    assert p.val == 3; p = p.next
    assert p.val == 4; p = p.next
    assert p.val == 5; p = p.next
    assert p is None


def test_2():
    # remove tail
    sol = Solution()
    head = ListNode(1)
    p = ListNode(2); head.next = p; q = p
    p = ListNode(3); q.next = p; q = p
    p = ListNode(4); q.next = p; q = p
    p = ListNode(5); q.next = p; q = p
    p = sol.removeNthFromEnd(head, 1)
    assert p.val == 1; p = p.next
    assert p.val == 2; p = p.next
    assert p.val == 3; p = p.next
    assert p.val == 4; p = p.next
    assert p is None


def test_3():
    sol = Solution()
    head = ListNode(1)
    p = sol.removeNthFromEnd(head, 1)
    assert p is None
