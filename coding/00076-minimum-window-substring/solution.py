import collections
from typing import Counter, Set


class Solution:

    def _dec(self, char: str, counter: Counter[str]):
        counter[char] -= 1
        if counter[char] == 0:
            counter.pop(char)

    def _add_char(self, char: str, t_set: Set[str],
                  residue: Counter[str], overflow: Counter[str]):
        if char not in t_set:
            return
        if char in residue:
            self._dec(char, residue)
        else:
            overflow[char] += 1

    def _remove_char(self, char: str, t_set: Set[str],
                     overflow: Counter[str]) -> bool:
        if char not in t_set:
            return True
        if char in overflow:
            self._dec(char, overflow)
            return True
        return False

    def _find_right_boundary(self, s: str, right: int, t_set: Set[str],
                             residue: Counter[str], overflow: Counter[str]) -> int:
        while right < len(s):
            self._add_char(s[right], t_set, residue, overflow)
            if not residue:
                break
            right += 1
        return right

    def _find_left_boundary(self, s: str, left: int, right: int, t_set: Set[str],
                            overflow: Counter[str]) -> int:
        while left < right:
            success = self._remove_char(s[left], t_set, overflow)
            if not success:
                return left
            left += 1
        return left

    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ''
        t_set = set(t)
        residue = collections.Counter(t)
        overflow = collections.Counter()
        min_len = len(s) + 1
        min_left = min_right = -1
        left = right = 0
        while right < len(s):
            right = self._find_right_boundary(s, right, t_set, residue, overflow)
            if right == len(s):
                break
            left = self._find_left_boundary(s, left, right, t_set, overflow)
            new_len = right - left + 1
            if new_len < min_len:
                min_len, min_left, min_right = new_len, left, right
            residue[s[left]] += 1
            left, right = left + 1, right + 1
        return s[min_left:min_right + 1] if min_left >= 0 else ''
