# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution, TreeNode


def test_0():
    sol = Solution()
    assert sol.isSymmetric(None)
    assert sol.isSymmetric(TreeNode(3))


def test_1():
    sol = Solution()
    a = TreeNode(1)
    b1 = TreeNode(2)
    b2 = TreeNode(2)
    a.left, a.right = b1, b2
    c1 = TreeNode(3)
    c2 = TreeNode(4)
    b1.left, b1.right = c1, c2
    c3 = TreeNode(4)
    c4 = TreeNode(3)
    b2.left, b2.right = c3, c4
    assert sol.isSymmetric(a)


def test_2():
    sol = Solution()
    a = TreeNode(1)
    b1 = TreeNode(1)
    b2 = TreeNode(1)
    a.left, a.right = b1, b2
    c2 = TreeNode(1)
    b1.right = c2
    c4 = TreeNode(1)
    b2.right = c4
