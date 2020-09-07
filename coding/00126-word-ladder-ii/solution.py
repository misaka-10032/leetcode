#!/usr/bin/env python3
# encoding: utf-8

import collections
import dataclasses
from typing import DefaultDict, Dict, List, Set, Tuple


@dataclasses.dataclass
class Node:
    word: str
    children: List['Node'] = dataclasses.field(
        default_factory=list)


@dataclasses.dataclass
class BfsState:
    graph_node: Node
    word_list: List[str]


class Solution:
    def _build_graph(self, word_set: Set[str]) -> Dict[str, Node]:
        graph = {}
        for word in word_set:
            graph[word] = Node(word)
        for word in word_set:
            node = graph[word]
            for idx, char in enumerate(word):
                for new_char_ord in range(ord(char) + 1, ord('z') + 1):
                    new_char = chr(new_char_ord)
                    new_word = word[:idx] + new_char + word[idx + 1:]
                    new_node = graph.get(new_word)
                    if new_node:
                        node.children.append(new_node)
                        new_node.children.append(node)
        return graph

    def _probe(self, s_set: Set[str], s_front: DefaultDict[str, BfsState],
               t_front: DefaultDict[str, BfsState], is_reversed: bool
               ) -> Tuple[List[List[str]], Dict[str, BfsState]]:
        result = []
        new_s_front = collections.defaultdict(list)
        for s_bfs_states in s_front.values():
            for s_bfs_state in s_bfs_states:
                for child in s_bfs_state.graph_node.children:
                    if child.word in s_set:
                        continue
                    t_bfs_states = t_front.get(child.word)
                    if t_bfs_states:
                        for t_bfs_state in t_bfs_states:
                            if is_reversed:
                                concat_list = t_bfs_state.word_list + s_bfs_state.word_list[::-1]
                            else:
                                concat_list = s_bfs_state.word_list + t_bfs_state.word_list[::-1]
                            result.append(concat_list)
                        continue
                    new_word_list = s_bfs_state.word_list + [child.word]
                    new_s_front[child.word].append(BfsState(child, new_word_list))

        for word in new_s_front:
            s_set.add(word)
        return result, new_s_front

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        word_set.add(beginWord)
        word_set.add(endWord)
        graph = self._build_graph(word_set)

        s_set = {beginWord}
        s_front = collections.defaultdict(list)
        s_front[beginWord].append(BfsState(graph[beginWord], [beginWord]))
        t_set = {endWord}
        t_front = collections.defaultdict(list)
        t_front[endWord].append(BfsState(graph[endWord], [endWord]))
        is_reversed = False
        while True:
            result, s_front = self._probe(s_set, s_front, t_front, is_reversed)
            if result:
                return result
            if not s_front:
                return []
            s_set, s_front, t_set, t_front = t_set, t_front, s_set, s_front
            is_reversed = not is_reversed
