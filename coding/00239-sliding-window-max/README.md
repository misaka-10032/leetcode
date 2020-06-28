# Sliding Window Maximum

* Monotonically decreasing priority queue. Before inserting,
  * Pop those out of boundary at left
  * Pop those not large enough at right
* Store the index in order to know the window boundary
