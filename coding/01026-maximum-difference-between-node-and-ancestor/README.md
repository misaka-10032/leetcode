# Maximum Difference Between Node and Ancestor

https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

## Solution

The max diff can be either with the min or the max element of the subtree. If the root element is big, we would like to
subtract a small number. However, if it's small, we would like to subtract a big number, so we can get a very negative
number, whose magnitude is big.

Therefore, we traverse the tree, and keep track of the min / max values.
