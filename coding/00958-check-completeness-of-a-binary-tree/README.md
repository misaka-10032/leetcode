# Check Completeness of a Binary Tree

https://leetcode.com/problems/check-completeness-of-a-binary-tree/

## Solution

We assign each node an index. The root is `0`. The children of node `i` are `2*i+1` and `2*i+2`. Then we BFS the tree,
and check if the index increments by one each time.
