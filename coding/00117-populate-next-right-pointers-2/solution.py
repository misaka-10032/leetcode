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
            return
        Q = deque([(root, 0)])
        while Q:
            prev, level = Q.popleft()
            if prev.left:
                Q.append((prev.left, level+1))
            if prev.right:
                Q.append((prev.right, level+1))
            while Q:
                curr, l_curr = Q.popleft()
                if l_curr > level:
                    # push it back
                    Q.appendleft((curr, l_curr))
                    break
                if curr.left:
                    Q.append((curr.left, level+1))
                if curr.right:
                    Q.append((curr.right, level+1))
                prev.next = curr
                prev = curr
