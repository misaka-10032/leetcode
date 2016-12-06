# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def rotate(node):
            """ returns the new root and the rightmost node
                assumes node is not None """

            # there will be no dangling right node
            if not node.left:
                # it's leaf
                return node, node

            left_root, left_end = rotate(node.left)
            if node.right:
                right_root, _ = rotate(node.right)
            else:
                right_root = None

            left_end.left = right_root
            left_end.right = node
            node.left = node.right = None
            return left_root, node

        if not root:
            return None

        return rotate(root)[0]
