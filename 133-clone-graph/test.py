# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution, UndirectedGraphNode


def graph_eq(g1, g2):
    def _graph_eq(g1, g2, old2new):
        """ visit g1, compare g2 """
        if not g1 and not g2:
            return True
        if not g1 and g2 or g1 and not g2:
            return False
        if g1 in old2new:
            return True
        if g1.label != g2.label:
            return False
        old2new[g1] = g2
        if len(g1.neighbors) != len(g2.neighbors):
            return False
        for g1_n, g2_n in zip(g1.neighbors, g2.neighbors):
            if not _graph_eq(g1_n, g2_n, old2new):
                return False
        return True
    return _graph_eq(g1, g2, {})


def test_0():
    sol = Solution()
    assert sol.cloneGraph(None) is None
    g1 = UndirectedGraphNode(2)
    g2 = sol.cloneGraph(g1)
    assert graph_eq(g1, g2)
    g1.label = 3
    assert not graph_eq(g1, g2)


def test_1():
    sol = Solution()
    n1 = UndirectedGraphNode(1)
    n0 = UndirectedGraphNode(0)
    n2 = UndirectedGraphNode(2)
    n1.neighbors = [n0, n2]
    n0.neighbors = [n1, n2]
    n2.neighbors = [n0, n1, n2]
    c1 = sol.cloneGraph(n1)
    assert graph_eq(n1, c1)
    n0.label = 9
    assert not graph_eq(n1, c1)
