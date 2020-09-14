#!/usr/bin/env python3
# encoding: utf-8


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotation_map = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',
        }
        n = len(num)
        for i in range(n):
            c = num[i]
            rc = rotation_map.get(c)
            if rc is None:
                return False
            if rc != num[n-1-i]:
                return False
        return True
