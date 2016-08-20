# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Codec, TreeNode


def tree_eq(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is not None and t2 is None:
        return False
    if t1 is None and t2 is not None:
        return False
    if t1.val != t2.val:
        return False
    if not tree_eq(t1.left, t2.left):
        return False
    if not tree_eq(t1.right, t2.right):
        return False
    return True


def _test_codec(root):
    cc = Codec()
    assert tree_eq(cc.deserialize(cc.serialize(root)), root)


def test_0():
    _test_codec(None)
    _test_codec(TreeNode(3))


def test_1():
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1.left = t2
    t1.right = t3
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t3.left = t4
    t3.right = t5
    _test_codec(t1)


def test_2():
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t1.left = t2
    t1.right = t3
    t4 = TreeNode(4)
    t2.left = t4
    t5 = TreeNode(5)
    t3.right = t5
    t6 = TreeNode(6)
    t4.right = t6
    t7 = TreeNode(7)
    t5.left = t7
    _test_codec(t1)
