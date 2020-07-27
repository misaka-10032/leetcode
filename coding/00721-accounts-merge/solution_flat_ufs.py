#!/usr/bin/env python3
# encoding: utf-8

from typing import Dict, List, Set


class Node:
    def __init__(self, email: str):
        self.email = email
        self.child_emails = {email}


class UnionFindSet:
    def __init__(self):
        self.roots: Set[Node] = set()
        self.email_to_root_map: Dict[str, Node] = {}

    def union(self, email1: str, email2: str):
        root1 = self.email_to_root_map[email1]
        root2 = self.email_to_root_map[email2]
        if root1 is root2:
            return
        if len(root1.child_emails) < len(root2.child_emails):
            root1, root2 = root2, root1
        for email in root2.child_emails:
            root1.child_emails.add(email)
            self.email_to_root_map[email] = root1
        self.roots.remove(root2)

    def add(self, email: str):
        if email in self.email_to_root_map:
            return
        root = Node(email)
        self.roots.add(root)
        self.email_to_root_map[email] = root


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Build an edge between adjacent emails, and build a union-find set
        # (email_ufs) for all the email addresses. In addition, build a map
        # from email to name (email_to_name_map) to compile the final results.
        # Some account can have no email? We can have a separate set to track
        # These accounts.
        email_ufs = UnionFindSet()
        email_to_name_map = {}
        result = []
        for account in accounts:
            name = account[0]
            if len(account) == 1:
                result.append(account)
                continue
            email1 = account[1]
            email_ufs.add(email1)
            email_to_name_map[email1] = name
            for i in range(2, len(account)):
                email2 = account[i]
                email_to_name_map[email2] = name
                email_ufs.union(email1, email2)
        for root in email_ufs.roots:
            name = email_to_name_map[root.email]
            account = [name]
            account.extend(sorted(root.child_emails))
            result.append(account)
        return result
