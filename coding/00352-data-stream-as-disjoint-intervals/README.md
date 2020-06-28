# Data Stream as Disjoint Intervals

## Binary Search Tree (BST)

One approach is to maintain a BST, but python doesn't have built in tree structure.
My impl of red-black tree seems to exceeds the code size limit by Leetcode, so...

## Union Find Set (UFS)

* Set of sets
 * {{1, 2, 3}, {4, 5, 6}, {7, 8}, ...}
* Supports
 * `Union(x, y)`: Union the set that `x` and `y` belongs to.
 * `Find(x)`: Find the representative of the set that `x` belongs to.
 * `Insert(x)`: Insert `{x}` into the global set.

* Example of union

```
{{1*, 2, 3}, {6*, 7, 8}, {9*, 10}}
```

After `union(3, 7)`, it becomes

```
{{1*, 2, 3, 6, 7, 8}, {9*, 10}}
```

### Data Structure

```
class Node(object):
    def __init__(self, key, parent=None):
        self.key = key
        self.parent = parent
        self.rank = 0
```

* The Union Find Set forms a forest.
* Each tree in it represents a set.
* The root of each tree is the representative.
* Each node keeps track of its parent.
* `rank` is effectively the height of the node in the tree.
* Example of `{{1*, 2, 3, 4}, {6*, 7}}` (what inside parentheses indicates rank).

```
    1(2)        6(1)
  /   \         |
2(1)  3(1)      7(0)
      |
      4(0)
```

### Path Compression

* Every time when a node finds its ancestor,
  it has its parent points directly to the ancestor.

```
    1(2)                   1(2)
  /   \                /    |    \
2(1)  3(1)    -->    2(1)  3(1)  4(0)
      |
      4(0)
```

* Rank is too difficult to maintain, so just leave them unchanged.

* Example of `union(3, 7)`.
 * `3` has root `1`; `7` has root `6`.
 * `1` has higher rank, so let `6` be child of `1`

```
        1(2)
     /   |   \
   2(1) 3(1) 6(1)
         |    |
        4(0) 7(0)
```

## For this problem

* We don't have to maintain the `Node` data structure.
* `parents` maintains mapping from nodes to parent nodes (root points to self).
* `roots` maintains mapping from root nodes to
 * `lower`, `upper`: the range of the interval.
 * `rank`: rank of the root node.
