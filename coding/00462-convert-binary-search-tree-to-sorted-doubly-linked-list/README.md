# Convert Binary Search Tree to Sorted Doubly Linked List

https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

## Solution

We simply traverse the tree, and update the pointers in-place. Here is a proof of why we can do this in-place without
messing up the traversal.

Each time, we change the right pointer of the previous node, and the left pointer of the current node. The right pointer
of the previous node will no longer be used, because we have already moved on to its successor. The left pointer of the
current node will be no longer used, because, we only need its right pointer or one of its ancestor node to find its
successor.

The way to traverse is detailed in the following question.

https://leetcode.com/problems/inorder-successor-in-bst/
