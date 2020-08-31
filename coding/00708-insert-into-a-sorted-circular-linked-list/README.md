# Insert into a Sorted Circular Linked List

https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

## Solution

First, we should take care of the special case with < 2 nodes.

Then, if we have >= 2 nodes, we can keep two adjacent pointers `left` `right`, and keep moving them until we find an
insertion point. The following cases could be the insertion point.

* `left.val <= new_val <= right.val`.
* We circled back to the original position. For example, all the initial values are the same.
* We find the tail of the list, and either of the following is true:
  * The new value is >= than the tail.
  * The new value is <= than the head.
   