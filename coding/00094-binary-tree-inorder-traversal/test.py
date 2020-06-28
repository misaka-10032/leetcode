# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution, TreeNode


def test_0():
    sol = Solution()
    assert sol.inorderTraversal(None) == []
    r = TreeNode(0)
    assert sol.inorderTraversal(r) == [0]


def test_1():
    sol = Solution()
    r = TreeNode(0)
    a1 = TreeNode(1)
    a2 = TreeNode(2)
    a3 = TreeNode(3)
    a4 = TreeNode(4)
    a5 = TreeNode(5)
    a6 = TreeNode(6)
    r.left, r.right = a1, a2
    a2.left, a2.right = a3, a6
    a3.left, a3.right = a4, a5
    assert sol.inorderTraversal(r) == [1, 0, 4, 3, 5, 2, 6]
