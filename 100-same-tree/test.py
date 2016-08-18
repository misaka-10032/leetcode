# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution, TreeNode


def test_0():
    sol = Solution()
    assert sol.isSameTree(None, None)
    assert not sol.isSameTree(None, TreeNode(3))
    assert not sol.isSameTree(TreeNode(2), None)
    assert sol.isSameTree(TreeNode(1), TreeNode(1))


def test_1():
    a1 = TreeNode(1)
    a0 = TreeNode(0)
    a3 = TreeNode(3)
    a1.left, a1.right = a0, a3
    a2 = TreeNode(2)
    a4 = TreeNode(4)
    a3.left, a3.right = a2, a4

    b1 = TreeNode(1)
    b0 = TreeNode(0)
    b3 = TreeNode(3)
    b1.left, b1.right = b0, b3
    b2 = TreeNode(2)
    b4 = TreeNode(4)
    b3.left, b3.right = b2, b4

    sol = Solution()
    assert sol.isSameTree(a1, b1)


def test_2():
    a1 = TreeNode(1)
    a0 = TreeNode(0)
    a3 = TreeNode(3)
    a1.left, a1.right = a0, a3
    a2 = TreeNode(2)
    a4 = TreeNode(4)
    a3.left, a3.right = a2, a4

    b1 = TreeNode(1)
    b0 = TreeNode(0)
    b3 = TreeNode(3)
    b1.left, b1.right = b0, b3
    b2 = TreeNode(2)
    b4 = TreeNode(6)
    b3.left, b3.right = b2, b4

    sol = Solution()
    assert not sol.isSameTree(a1, b1)
