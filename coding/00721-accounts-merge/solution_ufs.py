#!/usr/bin/env python3
# encoding: utf-8

import collections
from typing import Dict, List, Optional


class UnionFindSet:
    def __init__(self):
        self._parents: Dict[str, Optional[str]] = {}
        self._ranks: Dict[str, int] = {}

    def add(self, key: str):
        if key in self._parents:
            return
        self._parents[key] = None
        self._ranks[key] = 0

    def find(self, key: str):
        curr = key
        trace = []
        while True:
            trace.append(curr)
            parent = self._parents[curr]
            if parent is None:
                break
            curr = parent
        for i in range(len(trace) - 2):
            self._parents[trace[i]] = trace[-1]
            self._ranks.pop(trace[i], None)
        return trace[-1]

    def union(self, key1: str, key2: str):
        root1 = self.find(key1)
        root2 = self.find(key2)
        if root1 == root2:
            return
        if self._ranks[root1] < self._ranks[root2]:
            root1, root2 = root2, root1
        self._parents[root2] = root1
        self._ranks[root1] = max(self._ranks[root1], self._ranks[root2] + 1)
        self._ranks.pop(root2)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Add the new emails to the union find set (email_ufs). If an account
        # has multiple emails, join the later emails with the first one.
        # In addition, we also need to track the email_to_name map.
        # Once the set is created, we iterate the emails (tracked in email_to_name_map),
        # find the representative,  use it as key, and track all the emails by the same
        # person (root_email_to_all_map). Finally, we create the result by iterating
        # root_email_to_rest_map.
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
                email_ufs.add(email2)
                email_to_name_map[email2] = name
                email_ufs.union(email1, email2)
        root_email_to_all_map = collections.defaultdict(list)
        for email in email_to_name_map:
            root_email = email_ufs.find(email)
            root_email_to_all_map[root_email].append(email)
        for root_email, all_emails in root_email_to_all_map.items():
            name = email_to_name_map[root_email]
            account = [name] + sorted(all_emails)
            result.append(account)
        return result
