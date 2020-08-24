# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution, TreeNode

sol = Solution()


def test_0():
    n1 = TreeNode(1)
    assert sol.lowestCommonAncestor(n1, n1, n1) is n1


def test_1():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n2
    n1.right = n3
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n3.left = n4
    n3.right = n5
    assert sol.lowestCommonAncestor(n1, n4, n5) is n3
    assert sol.lowestCommonAncestor(n1, n2, n4) is n1
    assert sol.lowestCommonAncestor(n1, n2, n5) is n1


def test_2():
    n3 = TreeNode(3)
    n5 = TreeNode(5)
    n1 = TreeNode(1)
    n3.left = n5
    n3.right = n1
    n6 = TreeNode(6)
    n2 = TreeNode(2)
    n5.left = n6
    n5.right = n2
    n7 = TreeNode(7)
    n4 = TreeNode(4)
    n2.left = n7
    n2.right = n4
    n0 = TreeNode(0)
    n8 = TreeNode(8)
    n1.left = n0
    n1.right = n8
    assert sol.lowestCommonAncestor(n3, n5, n1) is n3
    assert sol.lowestCommonAncestor(n3, n5, n4) is n5
    assert sol.lowestCommonAncestor(n3, n5, n7) is n5
    assert sol.lowestCommonAncestor(n3, n5, n6) is n5
    assert sol.lowestCommonAncestor(n3, n5, n5) is n5
