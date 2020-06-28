# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution, TreeNode
sol = Solution()


def build_nodes(l):
    nodes = {}
    for v in l:
        nodes[v] = TreeNode(v)
    return nodes


def test_0():
    assert sol.longestConsecutive(None) == 0
    assert sol.longestConsecutive(TreeNode(1)) == 1


def test_1():
    n = build_nodes([1, 2, 3, 4, 5])
    n[1].right = n[3]
    n[3].left, n[3].right = n[2], n[4]
    n[4].right = n[5]
    assert sol.longestConsecutive(n[1]) == 3


def test_2():
    n = build_nodes([2, 3, 4, 1])
    n[2].right = n[3]
    n[3].left = n[4]
    n[4].left = n[1]
    assert sol.longestConsecutive(n[2])
