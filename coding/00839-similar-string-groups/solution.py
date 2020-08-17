#!/usr/bin/env python3
# encoding: utf-8


import dataclasses
from typing import Dict, List, Set


@dataclasses.dataclass
class Node:
    word: str
    children: List['Node'] = dataclasses.field(default_factory=list)


class Solution:
    def _is_similar(self, word1: str, word2: str) -> bool:
        cnt = 0
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                cnt += 1
            if cnt > 2:
                return False
        return cnt == 2

    def _build_graph1(self, word_set: Set[str]) -> Dict[str, Node]:
        words = list(word_set)
        word_to_node_map = {word: Node(word) for word in words}
        for i1 in range(len(words)):
            word1 = words[i1]
            node1 = word_to_node_map[word1]
            for i2 in range(i1 + 1, len(words)):
                word2 = words[i2]
                node2 = word_to_node_map[word2]
                if self._is_similar(word1, word2):
                    node1.children.append(node2)
                    node2.children.append(node1)
        return word_to_node_map

    def _build_graph2(self, word_set: Set[str]) -> Dict[str, Node]:
        word_to_node_map = {word: Node(word) for word in word_set}
        for word1 in word_set:
            node1 = word_to_node_map[word1]
            for i in range(len(word1)):
                for j in range(i + 1, len(word1)):
                    chars = list(word1)
                    if chars[i] == chars[j]:
                        continue
                    chars[i], chars[j] = chars[j], chars[i]
                    word2 = ''.join(chars)
                    maybe_node2 = word_to_node_map.get(word2, None)
                    if maybe_node2:
                        node1.children.append(maybe_node2)
        return word_to_node_map

    def _visit(self, node: Node, visited: Set[str]):
        visited.add(node.word)
        for child in node.children:
            if child.word in visited:
                continue
            self._visit(child, visited)

    def _count_groups(self, word_to_node_map: Dict[str, Node]) -> int:
        visited = set()
        cnt = 0
        for word in word_to_node_map:
            if word in visited:
                continue
            self._visit(word_to_node_map[word], visited)
            cnt += 1
        return cnt

    def numSimilarGroups(self, A: List[str]) -> int:
        if not A:
            return 0
        if not A[0]:
            return 0
        if len(A[0]) == 1:
            return 1

        word_set = set(A)
        n = len(word_set)
        m = len(A[0])
        build_graph_fn = self._build_graph1 if n * n * m < n * m * m * m else self._build_graph2
        word_to_node_map = build_graph_fn(word_set)
        return self._count_groups(word_to_node_map)
