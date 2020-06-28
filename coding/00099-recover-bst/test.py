# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution, TreeNode


def tree_eq(t1, t2):
    if t1 is None and t2 is not None or \
       t1 is not None and t2 is None:
        return False
    if t1 is None and t2 is None:
        return True
    if t1.val != t2.val:
        return False
    if not tree_eq(t1.left, t2.left):
        return False
    if not tree_eq(t1.right, t2.right):
        return False
    return True


def test_1():
    """ 0, 1, 2, 3, 4, 5 """
    sol = Solution()
    a1 = TreeNode(1)
    a5 = TreeNode(5)
    a3 = TreeNode(3)
    a1.left, a1.right = a5, a3
    a2 = TreeNode(2)
    a4 = TreeNode(4)
    a3.left, a3.right = a2, a4
    a0 = TreeNode(0)
    a4.right = a0
    sol.recoverTree(a1)

    t1 = TreeNode(1)
    t0 = TreeNode(0)
    t3 = TreeNode(3)
    t1.left, t1.right = t0, t3
    t2 = TreeNode(2)
    t4 = TreeNode(4)
    t3.left, t3.right = t2, t4
    t5 = TreeNode(5)
    t4.right = t5
    assert tree_eq(a1, t1)


def test_2():
    sol = Solution()
    a1 = TreeNode(1)
    a0 = TreeNode(0)
    a1.right = a0
    sol.recoverTree(a1)

    t0 = TreeNode(0)
    t1 = TreeNode(1)
    t0.right = t1
    assert tree_eq(a1, t0)


def test_3():
    sol = Solution()
    a1 = TreeNode(1)
    a3 = TreeNode(3)
    a1.right = a3
    a2 = TreeNode(2)
    a3.right = a2
    sol.recoverTree(a1)

    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t1.right = t2
    t3 = TreeNode(3)
    t2.right = t3
    assert tree_eq(a1, t1)
