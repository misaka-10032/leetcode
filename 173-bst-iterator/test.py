# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import BSTIterator, TreeNode


def test_0():
    it = BSTIterator(None)
    assert not it.hasNext()
    it = BSTIterator(TreeNode(1))
    assert it.next() == 1
    assert not it.hasNext()


def test_1():
    t4 = TreeNode(4)
    t2 = TreeNode(2)
    t6 = TreeNode(6)
    t4.left = t2
    t4.right = t6
    t3 = TreeNode(3)
    t2.right = t3
    t5 = TreeNode(5)
    t7 = TreeNode(7)
    t6.left = t5
    t6.right = t7
    it = BSTIterator(t4)
    assert it.hasNext()
    assert it.next() == 2
    assert it.hasNext()
    assert it.next() == 3
    assert it.hasNext()
    assert it.next() == 4
    assert it.hasNext()
    assert it.next() == 5
    assert it.hasNext()
    assert it.next() == 6
    assert it.hasNext()
    assert it.next() == 7
    assert not it.hasNext()


def test_2():
    it = BSTIterator(TreeNode(1))
    ans = []
    while it.hasNext():
        ans.append(it.next())
    assert ans == [1]
