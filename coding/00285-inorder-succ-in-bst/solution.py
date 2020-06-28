# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

* successor is leftmost leaf of the right subtree
* if there's no right child, go back to parent
 * keep going back to parent if it's right child of parent
"""

from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        Assumes p is definitely in this tree
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if p.right:
            # simply return the leftmost of right child
            prev = curr = p.right
            while curr:
                prev = curr
                curr = curr.left
            return prev

        parents = deque()
        curr = root
        while curr is not p:
            parents.append(curr)
            if p.val < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        # now curr is p
        while parents:
            prev = curr
            curr = parents.pop()
            if prev is curr.left:
                return curr

        return None
