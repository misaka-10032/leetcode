# Find Median from Data Stream

* Maintain a max-heap on left and a min-heap on right.
* When inserting, insert to left if it's smaller than median; otherwise right.
* Make sure the difference between size of two heaps `<= 1`.
* Once it's skewed, pop one element and push it to the other to balance.
* Python `heapq` only has min-heap; max-heap can be simulated by pushing `-x`.