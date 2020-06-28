# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

* Find the lowerbound
* Compare that with its successor
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """

        def find_succ(node, parents):
            if node.right:
                prev = None
                curr = node.right
                while curr:
                    prev = curr
                    curr = curr.left
                return prev

            parents = list(parents)
            curr = node
            while parents:
                prev = curr
                curr = parents.pop()
                if prev is curr.left:
                    return curr
            return None

        def find_pred(node, parents):
            if node.left:
                prev = None
                curr = node.left
                while curr:
                    prev = curr
                    curr = curr.right
                return prev

            parents = list(parents)
            curr = node
            while parents:
                prev = curr
                curr = parents.pop()
                if prev is curr.right:
                    return curr
            return None

        # find the lower bound
        parents = []
        prev = None
        curr = root
        while curr:
            parents.append(curr)
            if target < curr.val:
                prev = curr
                curr = curr.left
            elif target > curr.val:
                prev = curr
                curr = curr.right
            else:
                break

        if curr:
            return curr.val

        best = prev.val
        pred = find_pred(prev, parents)
        succ = find_succ(prev, parents)
        if pred and abs(pred.val - target) < abs(best - target):
            best = pred.val
        if succ and abs(succ.val - target) < abs(best - target):
            best = succ.val
        return best
