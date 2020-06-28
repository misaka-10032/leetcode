# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution, TreeNode

sol = Solution()


def build_nodes(ids):
    r = {}
    for idx in ids:
        r[idx] = TreeNode(idx)
    return r


def test_0():
    n = build_nodes([10])
    assert sol.kthSmallest(n[10], 1) == 10


def test_1():
    n = build_nodes([3, 4, 5])
    n[4].left, n[4].right = n[3], n[5]
    assert sol.kthSmallest(n[4], 1) == 3
    assert sol.kthSmallest(n[4], 2) == 4
    assert sol.kthSmallest(n[4], 3) == 5


def test_2():
    n = build_nodes([2, 3, 4, 5, 6])
    n[4].left, n[4].right = n[2], n[6]
    n[2].right = n[3]
    n[6].left = n[5]
    assert sol.kthSmallest(n[4], 1) == 2
    assert sol.kthSmallest(n[4], 2) == 3
    assert sol.kthSmallest(n[4], 3) == 4
    assert sol.kthSmallest(n[4], 4) == 5
    assert sol.kthSmallest(n[4], 5) == 6
