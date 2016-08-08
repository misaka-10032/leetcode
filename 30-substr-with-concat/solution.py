# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class RollingHash(object):
    def __init__(self, text, winsz):
        self.text = text
        self.winsz = winsz
        assert winsz <= len(text)
        # pos the first char of the current window
        self.pos = -1
        self.hash = sum(map(lambda x: ord(x), text[:winsz]))

    def roll(self):
        self.pos += 1
        if self.pos == 0:
            return True
        if self.pos + self.winsz > len(self.text):
            self.pos = len(self.text)
            return False
        self.hash -= ord(self.text[self.pos-1])
        self.hash += ord(self.text[self.pos+self.winsz-1])
        return True


def dict_acc(d, e):
    if e in d:
        d[e] += 1
    else:
        d[e] = 1


def dict_safe_rm(d, e):
    if e in d:
        d[e] -= 1
        if not d[e]:
            d.pop(e)
        return True
    else:
        return False


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []

        wlen = len(words[0])
        winsz = wlen * len(words)
        if len(s) < winsz:
            return []

        tgt = {}
        for w in words:
            dict_acc(tgt, w)

        rh = RollingHash(s, winsz)
        hash_ = sum(map(lambda x: ord(x), ''.join(words)))

        indices = []
        while rh.roll():
            if rh.hash != hash_:
                continue
            tgt_cp = dict(tgt)
            match = True
            for dp in xrange(0, winsz, wlen):
                word = s[rh.pos+dp:rh.pos+dp+wlen]
                if not dict_safe_rm(tgt_cp, word):
                    match = False
                    break
            if match:
                indices.append(rh.pos)
        return indices
