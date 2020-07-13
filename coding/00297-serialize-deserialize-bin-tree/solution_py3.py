#!/usr/bin/env python3
# encoding: utf-8


import collections
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize_node(self, node: Optional[TreeNode]) -> str:
        return str(node.val) if node else ''

    def layered_repr(self, root: TreeNode) -> List[str]:
        # The queue can contain None nodes. We do the following when we
        # dequeue: 1) add the node to `layered_repr`. 2) enqueue its child
        # nodes. The None nodes will not have child nodes, so we add them
        # to `layered_repr` but do not enqueue more.
        queue = collections.deque()
        queue.append(root)
        layered_repr = []
        while queue:
            node = queue.popleft()
            layered_repr.append(self.serialize_node(node))
            if not node:
                continue
            queue.append(node.left)
            queue.append(node.right)
        return layered_repr

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        layered_repr: List[str] = self.layered_repr(root)
        return ','.join(layered_repr)

    def make_node(self, val_str: str) -> Optional[TreeNode]:
        return TreeNode(int(val_str)) if val_str else None

    def next_nonnull_idx(self, nodes: List[Optional[TreeNode]], idx: int) -> int:
        idx += 1
        while idx < len(nodes):
            if nodes[idx]:
                return idx
            idx += 1
        return idx

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        layered_repr: List[str] = data.split(',')
        nodes = [None] * len(layered_repr)
        nodes[0] = self.make_node(layered_repr[0])
        parent_idx = 0
        child_idx = 1
        while parent_idx < len(nodes) and child_idx < len(nodes):
            node = nodes[parent_idx]
            nodes[child_idx] = left_node = self.make_node(layered_repr[child_idx])
            nodes[child_idx + 1] = right_node = self.make_node(layered_repr[child_idx + 1])
            node.left = left_node
            node.right = right_node
            # The parent should move to the next nonnull index because the null nodes will not have children.
            parent_idx = self.next_nonnull_idx(nodes, parent_idx)
            child_idx += 2
        return nodes[0]
