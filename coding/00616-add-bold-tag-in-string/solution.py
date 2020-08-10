#!/usr/bin/env python3
# encoding: utf-8

import dataclasses
from typing import Dict, List


@dataclasses.dataclass
class TrieNode:
    char: str
    children: Dict[str, 'TrieNode'] = dataclasses.field(
        default_factory=dict)
    final: bool = False


class Solution:
    def _build_trie(self, mydict: List[str]) -> TrieNode:
        root = TrieNode('')
        for word in mydict:
            assert word
            node = root
            for char in word:
                next_node = node.children.get(char, None)
                if not next_node:
                    next_node = TrieNode(char)
                    node.children[char] = next_node
                node = next_node
            node.final = True
        return root

    def _find_word(self, trie: TrieNode, s: str, start: int) -> int:
        node = trie
        end = -1
        i = start
        while i < len(s):
            next_node = node.children.get(s[i], None)
            if not next_node:
                break
            node = next_node
            i += 1
            if node.final:
                end = i
        return end

    def addBoldTag(self, s: str, mydict: List[str]) -> str:
        trie = self._build_trie(mydict)
        bold = [False] * len(s)
        for start in range(len(s)):
            end = self._find_word(trie, s, start)
            if end >= 0:
                bold[start:end] = [True] * (end - start)
        output = []
        prev_is_bold = False
        for char, curr_is_bold in zip(s, bold):
            if not prev_is_bold and curr_is_bold:
                output.append('<b>')
            elif prev_is_bold and not curr_is_bold:
                output.append('</b>')
            output.append(char)
            prev_is_bold = curr_is_bold
        if prev_is_bold:
            output.append('</b>')
        return ''.join(output)
