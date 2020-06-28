# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution, TreeNode

sol = Solution()


def make_nodes(vals):
    d = {}
    for v in vals:
        d[v] = TreeNode(v)
    return d


def make_branch(root, left, right):
    root.left = left
    root.right = right


def test_0():
    n1 = TreeNode(1)
    assert sol.lowestCommonAncestor(n1, n1, n1) is n1


def test_1():
    n2 = TreeNode(2)
    n1 = TreeNode(1)
    n3 = TreeNode(3)
    n2.left = n1
    n2.right = n3
    assert sol.lowestCommonAncestor(n2, n1, n3) is n2
    assert sol.lowestCommonAncestor(n2, n1, n2) is n2
    assert sol.lowestCommonAncestor(n2, n2, n3) is n2


def test_2():
    n = make_nodes([6, 2, 8, 0, 4, 7, 9, 3, 5])
    make_branch(n[6], n[2], n[8])
    make_branch(n[2], n[0], n[4])
    make_branch(n[8], n[7], n[9])
    make_branch(n[4], n[3], n[5])
    assert sol.lowestCommonAncestor(n[6], n[2], n[8]) is n[6]
    assert sol.lowestCommonAncestor(n[6], n[2], n[4]) is n[2]
    assert sol.lowestCommonAncestor(n[6], n[3], n[7]) is n[6]
    assert sol.lowestCommonAncestor(n[6], n[0], n[3]) is n[2]
    assert sol.lowestCommonAncestor(n[6], n[2], n[3]) is n[2]
    assert sol.lowestCommonAncestor(n[6], n[5], n[6]) is n[6]
