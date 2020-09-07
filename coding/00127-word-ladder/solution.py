#!/usr/bin/env python3
# encoding: utf-8

import collections
import dataclasses
from typing import Dict, Deque, List, Set, Tuple


@dataclasses.dataclass
class Node:
    word: str
    children: List['Node'] = dataclasses.field(default_factory=list)


class Solution:
    def _is_neighbor(self, word1: str, word2: str) -> bool:
        diff = 0
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                diff += 1
            if diff > 1:
                return False
        return diff == 1

    def _build_graph1(self, word_set: Set[str]) -> Dict[str, Node]:
        graph = {}
        word_list = list(word_set)
        for word in word_list:
            graph[word] = Node(word)
        for i in range(len(word_list)):
            word1 = word_list[i]
            node1 = graph[word1]
            for j in range(i + 1, len(word_list)):
                word2 = word_list[j]
                node2 = graph[word2]
                if self._is_neighbor(word1, word2):
                    node1.children.append(node2)
                    node2.children.append(node1)
        return graph

    def _build_graph2(self, word_set: Set[str]) -> Dict[str, Node]:
        graph = {}
        for word in word_set:
            graph[word] = Node(word)
        for word in word_set:
            node = graph[word]
            chars = list(word)
            for i, char in enumerate(word):
                for new_char_ord in range(ord(char) + 1, ord('z') + 1):
                    new_char = chr(new_char_ord)
                    chars[i] = new_char
                    new_word = ''.join(chars)
                    new_node = graph.get(new_word)
                    if new_node:
                        node.children.append(new_node)
                        new_node.children.append(node)
                    chars[i] = char
        return graph

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        word_set.add(beginWord)
        n = len(word_set)
        m = len(beginWord)
        if n * n * m < n * m * m * 26:
            graph = self._build_graph1(word_set)
        else:
            graph = self._build_graph2(word_set)

        s_depths = {beginWord: 1}
        s_queue = collections.deque([(graph[beginWord], 1)])
        t_depths = {endWord: 1}
        t_queue = collections.deque([(graph[endWord], 1)])

        def _probe(src_depths: Dict[str, int], src_queue: Deque[Tuple[Node, int]],
                   dst_depths: Dict[str, int]
                   ) -> int:
            node1, depth1 = src_queue.popleft()
            for node2 in node1.children:
                depth2 = depth1 + 1
                if node2.word in src_depths:
                    continue
                dst_depth = dst_depths.get(node2.word)
                if dst_depth is not None:
                    return depth1 + dst_depth
                src_depths[node2.word] = depth2
                src_queue.append((node2, depth2))
            return -1

        while True:
            depth = _probe(s_depths, s_queue, t_depths)
            if depth > 0:
                return depth
            if not s_queue:
                return 0
            s_depths, s_queue, t_depths, t_queue = (
                t_depths, t_queue, s_depths, s_queue)
        return 0
