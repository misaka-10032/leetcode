# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class State(object):
    ACT_TRAVERSE = 1
    ACT_PRINT = 2

    def __init__(self, node, action):
        self.node = node
        self.action = action


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = deque()
        stack.append(State(root, State.ACT_TRAVERSE))
        while stack:
            state = stack.pop()
            if state.node is None:
                continue
            if state.action == state.ACT_PRINT:
                result.append(state.node.val)
                continue
            # now it's traverse
            stack.append(State(state.node.right, state.ACT_TRAVERSE))
            stack.append(State(state.node, state.ACT_PRINT))
            stack.append(State(state.node.left, state.ACT_TRAVERSE))
        return result
