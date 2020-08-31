# LRU Cache

https://leetcode.com/problems/lru-cache/

## Solution

LRU cache can be implemented with an `OrderedDict`, aka a linked hash map. The recently accessed elements will be
appended to the end of the linked list. When the capacity is reached, we should pop from the head to satisfy the size
constraint. `OrderedDict` has an API `popitem(last=False)` to do this.

There is a corner case where `capacity` is <= 0. We should early return on `put()` to prevent weird behaviors.

## Followup

https://leetcode.com/problems/lfu-cache/submissions/
