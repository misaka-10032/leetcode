# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution, TreeNode


def test_0():
    sol = Solution()
    assert sol.maxDepth(None) == 0
    assert sol.maxDepth(TreeNode(3)) == 1


def test_1():
    sol = Solution()
    a1 = TreeNode(1)
    a0 = TreeNode(0)
    a3 = TreeNode(3)
    a1.left, a1.right = a0, a3
    a2 = TreeNode(2)
    a4 = TreeNode(4)
    a3.left, a3.right = a2, a4
    assert sol.maxDepth(a1) == 3
    assert sol.maxDepth(a0) == 1
    assert sol.maxDepth(a3) == 2
