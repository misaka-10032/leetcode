# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class TrieNode(object):
    def __init__(self, word=None):
        """
        Initialize your data structure here.
        """
        self.word = word
        self._next = [None] * 26

    def next(self, c):
        return self._next[ord(c) - ord('a')]

    def add_next(self, c, node):
        self._next[ord(c) - ord('a')] = node


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        p = self.root
        for c in word:
            if p.next(c) is None:
                p.add_next(c, TrieNode())
            p = p.next(c)
        p.word = word


class Solution(object):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def _search(self, node, i, j):
        if node.word is not None:
            self.found.append(node.word)
            # remove word to avoid duplication
            node.word = None
        for di, dj in self.dirs:
            ii, jj = i+di, j+dj
            if ii < 0 or ii >= self.m or \
               jj < 0 or jj >= self.n:
                continue
            if self.visited[ii][jj]:
                continue
            c = self.board[ii][jj]
            if node.next(c) is None:
                continue
            self.visited[ii][jj] = True
            self._search(node.next(c), ii, jj)
            self.visited[ii][jj] = False

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]:
            return []

        self.m, self.n = len(board), len(board[0])
        self.board = board

        self.trie = Trie()
        for word in words:
            self.trie.add(word)

        self.found = []
        for i in xrange(self.m):
            for j in xrange(self.n):
                node = self.trie.root.next(board[i][j])
                if node is None:
                    continue
                self.visited = [[False] * self.n for _ in xrange(self.m)]
                self.visited[i][j] = True
                self._search(node, i, j)

        return self.found
