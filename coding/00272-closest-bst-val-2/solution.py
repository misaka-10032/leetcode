# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

* first find the closest node
* find k-1 pred and succ
* pick k
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """

        def find_preds(node, k, parents):
            """ find at most k predecessors, in decreasing order """
            res = []
            parents = list(parents)
            curr = node

            while k > 0:
                if curr.left:
                    parents.append(curr)
                    curr = curr.left
                    while curr.right:
                        parents.append(curr)
                        curr = curr.right
                    k -= 1
                    res.append(curr)
                elif parents:
                    found = False
                    while parents:
                        prev = curr
                        curr = parents.pop()
                        if prev is curr.right:
                            found = True
                            k -= 1
                            res.append(curr)
                            break
                    if not found:
                        break
                else:
                    break
            return res

        def find_succs(node, k, parents):
            res = []
            parents = list(parents)
            curr = node
            while k > 0:
                if curr.right:
                    parents.append(curr)
                    curr = curr.right
                    while curr.left:
                        parents.append(curr)
                        curr = curr.left
                    k -= 1
                    res.append(curr)
                elif parents:
                    found = False
                    while parents:
                        prev = curr
                        curr = parents.pop()
                        if prev is curr.left:
                            found = True
                            k -= 1
                            res.append(curr)
                            break
                    if not found:
                        break
                else:
                    break
            return res

        best = curr = root
        parents = []
        while curr:
            if abs(curr.val - target) < abs(best.val - target):
                best = curr

            parents.append(curr)
            if target < curr.val:
                curr = curr.left
            elif target > curr.val:
                curr = curr.right
            else:
                break

        while parents and parents[-1] is not best:
            parents.pop()
        if parents and parents[-1] is best:
            parents.pop()

        preds = find_preds(best, k - 1, parents)
        succs = find_succs(best, k - 1, parents)
        lp = len(preds)
        ls = len(succs)

        i = j = 0
        r = k - 1
        res = [best]
        while r > 0 and i < lp and j < ls:
            r -= 1
            if abs(preds[i].val - target) < abs(succs[j].val - target):
                res.append(preds[i])
                i += 1
            else:
                res.append(succs[j])
                j += 1

        if r > 0 and i < lp:
            res.extend(preds[i:i + r])
        elif r > 0 and j < ls:
            res.extend(succs[j:j + r])
        res = map(lambda node: node.val, res)
        return res
