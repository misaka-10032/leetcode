#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def _safe_get(self, board: List[List[str]], i: int, j: int) -> str:
        if i < 0 or j < 0:
            return '.'
        else:
            return board[i][j]

    def countBattleships(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0
        m, n = len(board), len(board[0])

        cnt = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    continue
                if (self._safe_get(board, i - 1, j) == '.' and
                        self._safe_get(board, i, j - 1) == '.'):
                    cnt += 1
        return cnt
