# Range Sum of BST

https://leetcode.com/problems/range-sum-of-bst/

## Naive Solution

We iterate the tree via in-order traversal. We sum up the nodes in the range, and do early return when we go beyond the
upper bound.

The iterative approach can be found in [here](https://leetcode.com/problems/binary-search-tree-iterator/). We

* Keep going left and save the parents of the left children to `checkpoints`.
* Echo the current node by popping the node from stack.
* Go right, and then keep going left. Save the parents of the left children to `checkpoints`.

## Faster Solution

The naive solution can be slow if the lower bound is at the end. We can do a binary search to find
**the first element that is >=** the lower bound. The operation takes `O(h)`, where `h` is the height of the tree. We
then iterate the following nodes until we go beyond the upper bound.

When we search **the first element that is >=** the lower bound, we

* Go left if the current node is > the lower bound.
  * We save the current node in the checkpoint before going left.
* Go right if the current node is < the lower bound.
  * We do **NOT** save checkpoints when we go right.
* Return the node when we find the lower bound.

Adding the checkpoint before going left is the trick for the `next()` iteration. If we need to go back with `prev()`,
then we need to store the checkpoint before going right as well. When we pop the checkpoint, we need to check if the
current node if the left or the right node of the checkpoint before using it.
