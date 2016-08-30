# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution, TreeLinkNode


def test_0():
    sol = Solution()
    n1 = TreeLinkNode(1)
    sol.connect(n1)
    assert n1.next is None


def test_1():
    sol = Solution()
    n1 = TreeLinkNode(1)
    n2 = TreeLinkNode(2)
    n3 = TreeLinkNode(3)
    n1.left = n2
    n1.right = n3
    n4 = TreeLinkNode(4)
    n5 = TreeLinkNode(5)
    n2.left = n4
    n2.right = n5
    n6 = TreeLinkNode(6)
    n7 = TreeLinkNode(7)
    n3.left = n6
    n3.right = n7
    sol.connect(n1)
    assert n1.next is None
    assert n2.next is n3
    assert n3.next is None
    assert n4.next is n5
    assert n5.next is n6
    assert n6.next is n7
    assert n7.next is None


def test_2():
    sol = Solution()
    n1 = TreeLinkNode(1)
    n2 = TreeLinkNode(2)
    n3 = TreeLinkNode(3)
    n1.left = n2
    n1.right = n3
    n4 = TreeLinkNode(4)
    n5 = TreeLinkNode(5)
    n2.left = n4
    n2.right = n5
    n7 = TreeLinkNode(7)
    n3.right = n7
    sol.connect(n1)
    assert n1.next is None
    assert n2.next is n3
    assert n3.next is None
    assert n4.next is n5
    assert n5.next is n7
    assert n7.next is None
