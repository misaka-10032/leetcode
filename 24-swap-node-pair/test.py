# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution, ListNode


def test_0():
    sol = Solution()
    assert sol.swapPairs(None) is None
    head = ListNode(1)
    ans = sol.swapPairs(head)
    p = ans
    assert p.val == 1; p = p.next
    assert p is None


def test_1():
    sol = Solution()
    head = ListNode(1); q = head
    p = ListNode(2); q.next = p; q = p
    p = ListNode(3); q.next = p; q = p
    p = ListNode(4); q.next = p; q = p
    ans = sol.swapPairs(head)
    p = ans
    assert p.val == 2; p = p.next
    assert p.val == 1; p = p.next
    assert p.val == 4; p = p.next
    assert p.val == 3; p = p.next
    assert p is None


def test_2():
    sol = Solution()
    head = ListNode(1); q = head
    p = ListNode(2); q.next = p; q = p
    p = ListNode(3); q.next = p; q = p
    ans = sol.swapPairs(head)
    p = ans
    assert p.val == 2; p = p.next
    assert p.val == 1; p = p.next
    assert p.val == 3; p = p.next
    assert p is None


def test_3():
    sol = Solution()
    head = ListNode(1); q = head
    p = ListNode(2); q.next = p; q = p
    p = ListNode(3); q.next = p; q = p
    p = ListNode(4); q.next = p; q = p
    p = ListNode(5); q.next = p; q = p
    ans = sol.swapPairs(head)
    p = ans
    assert p.val == 2; p = p.next
    assert p.val == 1; p = p.next
    assert p.val == 4; p = p.next
    assert p.val == 3; p = p.next
    assert p.val == 5; p = p.next
    assert p is None


def test_4():
    sol = Solution()
    head = ListNode(1); q = head
    p = ListNode(2); q.next = p; q = p
    p = ListNode(3); q.next = p; q = p
    p = ListNode(4); q.next = p; q = p
    p = ListNode(5); q.next = p; q = p
    p = ListNode(6); q.next = p; q = p
    p = ListNode(7); q.next = p; q = p
    p = ListNode(8); q.next = p; q = p
    ans = sol.swapPairs(head)
    p = ans
    assert p.val == 2; p = p.next
    assert p.val == 1; p = p.next
    assert p.val == 4; p = p.next
    assert p.val == 3; p = p.next
    assert p.val == 6; p = p.next
    assert p.val == 5; p = p.next
    assert p.val == 8; p = p.next
    assert p.val == 7; p = p.next
    assert p is None
