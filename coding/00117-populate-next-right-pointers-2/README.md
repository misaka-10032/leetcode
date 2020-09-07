# Populating Next Right Pointers in Each Node II

https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

## Solution

The problem is similar to
[the previous one](https://leetcode.com/problems/populating-next-right-pointers-in-each-node/). However, due to the
incompleteness of the tree, we need to be careful about how to link the next layer, and how to hop onto the next layer.

To link the next layer, we can essentially traverse the next layer by traversing the current layer. Beside traversing,
we should also keep track of the `prev` node. We can come up with the following abstraction.

```
while it:
  prev = _maybe_link_next(prev, it.left)
  prev = _maybe_linke_next(prev, it.right)
  it = it.next
```

In order to move on to the next layer, we need to traverse the current layer again, and find the first node with a
child, the child could be either `left` or `right`. We find this child, and update the `head` pointer to this child.
