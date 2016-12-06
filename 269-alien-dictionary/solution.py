# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

* Topological sort via iterative approach
* deps: set of dependencies, like ['ab', 'bc', ...]
* heads: set of chars without incoming links
* remain: set of chars that are not cleared
* order: list of chars in topological order
"""


class Solution(object):
    def alienOrder(self, words):
        deps = set()
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    deps.add(c1+c2)
                    break
            if len(w1) > len(w2) and w1.startswith(w2):
                # bad dict order
                return ''

        remain = set(''.join(words))
        order = []
        deps = list(deps)
        while deps:
            heads = remain - set(zip(*deps)[1])
            if not heads:
                # circular dependency found
                return ''
            order.extend(heads)
            remain -= heads
            deps = filter(heads.isdisjoint, deps)

        order.extend(remain)
        return ''.join(order)
