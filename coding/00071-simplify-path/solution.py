#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def _parse_path(self, path: str) -> List[str]:
        components = ['']
        for component in path.split('/'):
            if not component:
                continue
            elif component == '.':
                continue
            elif component == '..':
                if len(components) == 1:
                    continue
                components.pop()
            else:
                components.append(component)
        return components

    def simplifyPath(self, path: str) -> str:
        components = self._parse_path(path)
        if len(components) == 1:
            return '/'
        return '/'.join(components)
