# All O`one Data Structure

https://leetcode.com/problems/all-oone-data-structure/

## Solution

Maintain a hash map and a doubly-linked list. The map maps a key to a node in the list, and the list groups the keys by
their counts. The nodes are ordered by their counts.

```
                                        v max_node
dummy <-> node_1 <-> node_2 <-> ... <-> node_n
          {keys}     {keys}             {keys}
cnt=0     cnt=1      cnt=3              cnt=k
```

### Min / Max Query

The first node after the dummy node stores the min keys. The last node stores the max keys.

### Increment

First, we find the node that the key lies in by looking up the map. If it does not exist yet, we tentatively add it to
the dummy node.

Then, we look up its next node. If its next node exist and has the count being `cnt+1` as well, it's easy, we return the
next node. Otherwise, we need to create a new node, and insert it after the current node. During insertion, if we find
the current node was the max node, we need to update the max node as well.

Once we get the next node, we remove the key from the current node, and add it to the next node. If the current node no
longer has keys and the current node is not the dummy node, we should remove the current node.

Lastly, we should update the map to map the key to the next node.

### Decrement

First, we find the node that the key lies in by looking up the map. The problem guarantees that the node must exist.

Then, we look up its previous node. As we have a dummy node, its previous node must exist. If its previous node has
count being `cnt-1`, it's easy, we return the previous node. Otherwise, we need to create a new node, and insert it
after the original previous node.

Once we get the previous node, we remove the key from the current node, and only add it to the previous node if the
previous node is not the dummy node. If the current node no longer has keys, we need to remove the current node. During
removal, if we find the current node was the max node, we need to update the max node as well.

Lastly, if the previous node is the dummy node, we need to remove the key from the map. Otherwise, we need to update the
node for the key.
