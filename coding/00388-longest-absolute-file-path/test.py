# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert sol.lengthLongestPath('') == 0
    assert sol.lengthLongestPath('dir') == 0
    assert sol.lengthLongestPath('dir1\ndir2') == 0
    assert sol.lengthLongestPath('dir1\ndir2\n\tf.txt') == 10
    assert sol.lengthLongestPath('f.txt') == 5


def test_1():
    tree = 'dir\n' \
           '\tsubdir1\n' \
           '\t\tfile1.ext\n' \
           '\t\tsubsubdir1\n' \
           '\tsubdir2\n' \
           '\t\tsubsubdir2\n' \
           '\t\t\tfile2.ext'
    assert sol.lengthLongestPath(tree) == 32


def test_2():
    tree = 'dir\n    file.txt'
    assert sol.lengthLongestPath(tree) == 12


def test_3():
    tree = 'file name with  space.txt'
    assert sol.lengthLongestPath(tree) == 25