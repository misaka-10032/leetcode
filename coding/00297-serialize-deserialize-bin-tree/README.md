# Serialize and Deserialize Binary Tree

* Level order traversal with FIFO queue.
* Add the node to serialization upon being popped.
* `None` won't be pushed, but will be appended to serialization.
* This is a little bit different from the LeetCode serialization/deserialization
  * Leetcode will strip the rightmost `None`.
  * For simplicity, I don't.
