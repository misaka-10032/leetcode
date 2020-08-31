# Flatten a Multilevel Doubly Linked List

https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

## Solution

The link starts to change when a node has a child, so we keep finding the next node with a child, and traverse the child
node first. Before traversing, we cache the next node (`3`) and link the current node's (`2`) next pointer to its child
node. After traversal, we point the `last` node's next to the cached next (`3`). The cached next becomes current, and we
continue the traversal. 

```
1 <-> 2 <-> 3                      1 <-> 2                3
      |                                  |                ^
      4 <-> ...           -->            4 ... <-> last <-+
      |                                  |
     ...                                ...
```

One corner case is that the last node in a layer can have child. In this case, we should early return without linking
anything.

```
1 <-> 2                            1 <-> 2
      |                                  |
      4 <-> ...           -->            4 ... <-> last
      |                                  |
     ... 
```

The other corner case is that a layer can have no node with a child. In this case, we should simply return the last
node.

## Follow up

As a followup, we can ask how to traverse the list in a layered manner. This seems a BFS problem, but we don't actually
need a queue. We only need a `front` pointer and a `rear` pointer. The `front` pointer keeps probing to the end of a
layer, and the `rear` pointer stops at a node with a child. We keep doing this until the `rear` pointer reaches the end.