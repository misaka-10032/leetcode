# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


from collections import deque


class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return None
        level = deque([root])
        cnt = 1
        finish = False
        while not finish:
            prev = level.popleft()
            if not prev.left:
                finish = True
            level.append(prev.left)
            level.append(prev.right)
            for _ in xrange(1, cnt):
                curr = level.popleft()
                level.append(curr.left)
                level.append(curr.right)
                prev.next = curr
                prev = curr
            prev.next = None
            cnt <<= 1
