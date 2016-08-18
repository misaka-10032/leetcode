# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


def c2i(c):
    return ord(c) - ord('a')


class TrieNode(object):
    def __init__(self, char, is_word=False):
        """
        Initialize your data structure here.
        """
        self.char = char
        self.is_word = is_word
        self.next = [None] * 26


class Trie(object):
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        p = self.root
        for c in word:
            i = c2i(c)
            if p.next[i] is None:
                p.next[i] = TrieNode(c)
            p = p.next[i]
        p.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self.root
        for c in word:
            i = c2i(c)
            if p.next[i] is None:
                return False
            p = p.next[i]
        return p.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = self.root
        for c in prefix:
            i = c2i(c)
            if p.next[i] is None:
                return False
            p = p.next[i]
        return True


class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.trie = Trie()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.trie.insert(word)

    def _search(self, node, word, k):
        if k == len(word):
            return node.is_word
        found = False
        c = word[k]
        if c == '.':
            for i in xrange(26):
                if node.next[i] is None:
                    continue
                found = self._search(node.next[i], word, k+1)
                if found:
                    break
        else:
            i = c2i(c)
            if node.next[i] is None:
                return False
            found = self._search(node.next[i], word, k+1)
        return found

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self._search(self.trie.root, word, 0)
