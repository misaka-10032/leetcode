# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution, TreeNode
sol = Solution()


def make_nodes(vals):
    n = {}
    for v in vals:
        n[v] = TreeNode(v)
    return n


def test_0():
    assert sol.binaryTreePaths(None) == []
    assert sol.binaryTreePaths(TreeNode(1)) == ['1']


def test_1():
    n = make_nodes([1, 2, 3, 5])
    n[1].left, n[1].right = n[2], n[3]
    n[2].right = n[5]
    ans = sol.binaryTreePaths(n[1])
    tgt = ['1->2->5', '1->3']
    assert sorted(ans) == sorted(tgt)


def test_2():
    n = make_nodes([1, 2, 3, 4, 5, 6])
    n[1].left, n[1].right = n[2], n[3]
    n[2].left = n[4]
    n[3].left, n[3].right = n[5], n[6]
    ans = sol.binaryTreePaths(n[1])
    tgt = ['1->2->4', '1->3->5', '1->3->6']
    assert sorted(ans) == sorted(tgt)
