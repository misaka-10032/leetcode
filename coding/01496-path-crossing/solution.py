#!/usr/bin/env python3
# encoding: utf-8

class Solution:
    def walk(self, loc, d):
        x, y = loc
        if d == 'N':
            return (x, y+1)
        elif d == 'S':
            return (x, y-1)
        elif d == 'E':
            return (x+1, y)
        elif d == 'W':
            return (x-1, y)
        else:
            assert 0

    def isPathCrossing(self, path: str) -> bool:
        loc = (0, 0)
        past = set([loc])
        for d in path:
            loc = self.walk(loc, d)
            if loc in past:
                return True
            past.add(loc)
        return False

