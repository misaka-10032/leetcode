# Merge Sorted Array

### List

* Easiest way is to stretch linked list into list, sort, and convert it back.
* By doing this complexity is $O(n \log n)$,
  where $n = n_1 + n_2 + ... + n_k$

### Heap

* The other way is to maintain a heap of at most $k$ elements.
* Complexity would be $O(n \log k)$
* `heapq` requires the elements to be comparable. Two workarounds:
  * Creates a wrapper class with `__lt__` and `__gt__` implemented.
  * Use a tuple `(node.val, id(node), node)`.