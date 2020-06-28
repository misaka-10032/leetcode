# Longest Consecutive Sequence

* Build a set of `nums`.
* Check the consecutive length only for the last element
  * e.g. `1, 2, 3, 4`, when we are at 3, if we find 4
    is in the set, we simply skip it.
* Each element will at most be visited twice, so
  the complexity would be `O(n)`.
