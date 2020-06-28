# Merge Sorted Array

### List

* Easiest way is to stretch linked list into list, sort, and convert it back.
* By doing this complexity is $O(n \log n)$,
  where $n = n_1 + n_2 + ... + n_k$

### Heap

* The other way is to maintain a heap of at most $k$ elements.
* Edge case could be tricky, don't try to do that unless being asked to.
* Complexity would be $O(n \log k)$
