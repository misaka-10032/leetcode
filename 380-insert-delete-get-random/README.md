# Insert Delete GetRandom O(1)

* Remove element at index `i` within $O(1)$
 * Swap that element with the last element, and remove the last.
 * Removing the last has amortized $O(1)$.
* Data structures
 * `vals` is a `list` keeping all the values.
 * `v2i` is a `dict` mapping value to index.
