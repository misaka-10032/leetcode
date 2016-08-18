# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution, TreeNode


def post(root):
    if root is None:
        return []
    left = post(root.left)
    right = post(root.right)
    return left + right + [root.val]


def forest_equal(f1, f2):
    f1 = sorted(map(post, f1))
    f2 = sorted(map(post, f2))
    return f1 == f2


def test_0():
    sol = Solution()
    assert sol.generateTrees(0) == []
    tgt = [TreeNode(1)]
    ans = sol.generateTrees(1)
    assert forest_equal(ans, tgt)


def test_1():
    sol = Solution()
    tgt = []
    """
       1
        \
         3
        /
       2
    """
    a = TreeNode(1)
    c = TreeNode(3)
    a.right = c
    b = TreeNode(2)
    c.left = b
    tgt.append(a)

    """
        3
       /
      2
     /
    1
    """
    c = TreeNode(3)
    b = TreeNode(2)
    c.left = b
    a = TreeNode(1)
    b.left = a
    tgt.append(c)

    """
      3
     /
    1
     \
      2
    """
    c = TreeNode(3)
    a = TreeNode(1)
    c.left = a
    b = TreeNode(2)
    a.right = b
    tgt.append(c)

    """
      2
     / \
    1   3
    """
    b = TreeNode(2)
    a = TreeNode(1)
    c = TreeNode(3)
    b.left = a
    b.right = c
    tgt.append(b)

    """
    1
     \
      2
       \
        3
    """
    a = TreeNode(1)
    b = TreeNode(2)
    a.right = b
    c = TreeNode(3)
    b.right = c
    tgt.append(a)

    ans = sol.generateTrees(3)
    assert forest_equal(ans, tgt)
