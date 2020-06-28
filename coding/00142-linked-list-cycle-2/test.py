# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution, ListNode


def test_0():
    sol = Solution()
    assert sol.detectCycle(None) is None

    n1 = ListNode(1)
    n1.next = n1
    assert sol.detectCycle(n1) is n1

    n1 = ListNode(1)
    assert sol.detectCycle(n1) is None

    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2
    assert sol.detectCycle(n1) is None

    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2
    n2.next = n1
    assert sol.detectCycle(n1) is n1


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
    assert sol.detectCycle(n1) is n2


def test_2():
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
    n6 = ListNode(6)
    n5.next = n6
    n6.next = n2
    assert sol.detectCycle(n1) is n2


def test_3():
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
    n6 = ListNode(6)
    n5.next = n6
    n7 = ListNode(7)
    n6.next = n7
    n8 = ListNode(8)
    n7.next = n8
    n8.next = n3
    assert sol.detectCycle(n1) is n3
