# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution, inf
sol = Solution()


def test_0():
    m = [[]]
    t = [[]]
    sol.wallsAndGates(m)
    assert m == t

    m = [[0]]
    t = [[0]]
    sol.wallsAndGates(m)
    assert m == t

    m = [[-1]]
    t = [[-1]]
    sol.wallsAndGates(m)
    assert m == t

    m = [[inf]]
    t = [[inf]]
    sol.wallsAndGates(m)
    assert m == t


def test_1():
    m = [[inf, -1, 0, inf],
         [inf, inf, inf, -1],
         [inf, -1, inf, -1],
         [0, -1, inf, inf]]
    t = [[3, -1, 0, 1],
         [2, 2, 1, -1],
         [1, -1, 2, -1],
         [0, -1, 3, 4]]
    sol.wallsAndGates(m)
    assert m == t


def test_2():
    m = [[0, 0, 0, 0, inf, inf],
         [-1, 0, -1, inf, 0, -1],
         [-1, -1, 0, 0, inf, 0],
         [-1, -1, inf, inf, inf, -1],
         [inf, inf, -1, inf, -1, inf],
         [inf, inf, 0, -1, -1, 0],
         [0, 0, 0, inf, -1, 0],
         [0, -1, 0, -1, 0, 0],
         [inf, 0, -1, -1, inf, inf],
         [0, 0, -1, -1, -1, inf]]
    t = [[0, 0, 0, 0, 1, 2],
         [-1, 0, -1, 1, 0, -1],
         [-1, -1, 0, 0, 1, 0],
         [-1, -1, 1, 1, 2, -1],
         [2, 2, -1, 2, -1, 1],
         [1, 1, 0, -1, -1, 0],
         [0, 0, 0, 1, -1, 0],
         [0, -1, 0, -1, 0, 0],
         [1, 0, -1, -1, 1, 1],
         [0, 0, -1, -1, -1, 2]]
    sol.wallsAndGates(m)
    assert m == t
