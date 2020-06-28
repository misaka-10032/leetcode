# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution, TreeNode


def test_0():
    sol = Solution()
    assert sol.isValidBST(None)
    assert sol.isValidBST(TreeNode(9))


def test_1():
    sol = Solution()
    a2 = TreeNode(2)
    a1 = TreeNode(1)
    a4 = TreeNode(4)
    a2.left, a2.right = a1, a4
    a3 = TreeNode(3)
    a5 = TreeNode(5)
    a4.left, a4.right = a3, a5
    assert sol.isValidBST(a2)


def test_2():
    sol = Solution()
    a2 = TreeNode(2)
    a6 = TreeNode(6)
    a4 = TreeNode(4)
    a2.left, a2.right = a6, a4
    a3 = TreeNode(3)
    a5 = TreeNode(5)
    a4.left, a4.right = a3, a5
    assert not sol.isValidBST(a2)


def test_3():
    sol = Solution()
    a2 = TreeNode(2)
    a1 = TreeNode(1)
    a4 = TreeNode(4)
    a2.left, a2.right = a1, a4
    a6 = TreeNode(6)
    a1.right = a6
    a3 = TreeNode(3)
    a5 = TreeNode(5)
    a4.left, a4.right = a3, a5
    assert not sol.isValidBST(a2)
