# Binary Tree Longest Consecutive Sequence

* Backtracking.
* Have to go through the left/right subtrees even it's not
  not consecutive for root.
* Each node pass `curr, best` to its parent.
  * `curr` is to take this node as chain, what's the longest consecutive path.
  * `best` the longest one in its subtree, excluding the current node.
