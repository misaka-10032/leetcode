# LFU Cache

https://leetcode.com/problems/lfu-cache/

## Solution

The access frequency can be tracked with a linked list
(see also [here](https://leetcode.com/problems/all-oone-data-structure/)). The least recent keys can also be tracked
with a linked list. As the problem asks us to first evict by least frequency, and then by least recency, we can group
the key-value pairs first by frequency, and then link them in a linked list. In other words, it will be a nested linked
list. The first level is sorted by frequency (the least frequent comes first), and the second level is sorted by
freshness (the least fresh comes first).

```
@dataclasses.dataclass
class KvNode:
    key: int
    val: int
    freq_node: 'FreqNode' = None
    prev: 'KeyNode' = None
    next: 'KeyNode' = None


@dataclasses.dataclass
class FreqNode:
    freq: int
    kv_node_list: 'LinkedList' = dataclasses.field(
        default_factory=lambda: LinkedList(KvNode('', -1)))
    prev: 'FreqNode' = None
    next: 'FreqNode' = None
```

For fast access, we also need a map that maps the key to the `KvNode`.

In `get()`, we find the `KvNode`, and move it from the current `FreqNode` to the next `FreqNode`. Be aware that the next
`FreqNode` may not has `freq+1` so we might need to create it.

In `put()`, we reuse `get()` to update the frequency if it's in the map already. Otherwise, we insert a new `KvNode` in
the 1-freq node. If the capacity is reached, we pop a `KvNode` from the first `FreqNode`.
