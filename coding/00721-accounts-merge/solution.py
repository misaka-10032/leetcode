#!/usr/bin/env python3
# encoding: utf-8

import dataclasses
from typing import Dict, List, Set


@dataclasses.dataclass(frozen=True)
class Node:
    email: str
    name: str
    children: Set['Node'] = dataclasses.field(
        default_factory=set, compare=False)


class Solution:
    def _find_or_add_node(self, email: str, name: str,
                          email_to_node_map: Dict[str, Node]) -> Node:
        node = email_to_node_map.get(email, None)
        if node:
            assert node.name == name
            return node
        node = Node(email, name)
        email_to_node_map[email] = node
        return node

    def _traverse(self, node: Node, visited_node_ids: Set[int], user_emails: List[str]):
        visited_node_ids.add(id(node))
        user_emails.append(node.email)
        for child in node.children:
            if id(child) not in visited_node_ids:
                self._traverse(child, visited_node_ids, user_emails)

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # For each additional email owned by a user, we add an edge to their
        # first email. Then we do a DFS of the email graph, and find the connected
        # components.
        email_to_node_map = {}
        result = []
        for account in accounts:
            name = account[0]
            if len(account) == 1:
                result.append(account)
                continue
            email1 = account[1]
            node1 = self._find_or_add_node(email1, name, email_to_node_map)
            for i in range(2, len(account)):
                email2 = account[i]
                node2 = self._find_or_add_node(email2, name, email_to_node_map)
                node1.children.add(node2)
                node2.children.add(node1)
        visited_node_ids = {id(None)}
        for email, node in email_to_node_map.items():
            if id(node) in visited_node_ids:
                continue
            user_emails = []
            self._traverse(node, visited_node_ids, user_emails)
            result.append([node.name] + sorted(user_emails))
        return result
