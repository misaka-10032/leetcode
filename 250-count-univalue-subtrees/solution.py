# encoding: utf-8
"""
* define good node as a node of which all the subtree nodes have the same value
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            """
            assumes node is not None
            returns the value if it's a good node
            returns None if it's a bad node
            """
            if not node.left and not node.right:
                cnt[0] += 1
                return node.val

            if not node.left:
                rval = dfs(node.right)
                if rval == node.val:
                    cnt[0] += 1
                    return rval
                else:
                    return None

            if not node.right:
                lval = dfs(node.left)
                if lval == node.val:
                    cnt[0] += 1
                    return lval
                else:
                    return None

            lval = dfs(node.left)
            rval = dfs(node.right)
            if lval == rval == node.val:
                cnt[0] += 1
                return lval
            else:
                return None

        if not root:
            return 0

        cnt = [0]
        dfs(root)
        return cnt[0]
