# Populating Next Right Pointers in Each Node

https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

## Solution

The solution is traverse the tree with BFS, but the interviewer might ask we to eliminate the queue to save space.
Thanks to the `next` pointer in the tree node, we can safely traverse the tree with two pointers.

We can have a `head` pointer that points to the head of each layer, and a `probe` pointer to traverse the current layer.
When we traverse the current layer, we link the `next` pointers of the next layer. Once we finished the current layer,
we can move on to the next layer.

As the tree is complete, we can easily connect the next layer by linking the current `left` and `right`, and then the
current `right` and next's `left`. To hop onto the next layer, we can simply move the head to its `left`.
