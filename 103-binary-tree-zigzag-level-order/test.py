# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution, TreeNode


def test_0():
    sol = Solution()
    assert sol.zigzagLevelOrder(None) == []
    assert sol.zigzagLevelOrder(TreeNode(3)) == [[3]]


def test_1():
    sol = Solution()
    a3 = TreeNode(3)
    a9 = TreeNode(9)
    a20 = TreeNode(20)
    a3.left, a3.right = a9, a20
    a15 = TreeNode(15)
    a7 = TreeNode(7)
    a20.left, a20.right = a15, a7
    assert sol.zigzagLevelOrder(a3) == [[3], [20, 9], [15, 7]]
