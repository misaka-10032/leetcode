# Add Two Numbers

## Description
* [Link](https://leetcode.com/problems/add-two-numbers/)
* Input: l1, type: ListNode.
* Input: l2, type: ListNode.
* Output: l, type: ListNode.

## Solution
* When inserting nodes into single linked list, maintain two pointers when iterating.
  * `q`: previous
  * `p`: probe
* As `l1`, `l2` are reversely ordered, things would be easy.
  * As long as `l1` or `l2` is non-empty, or there's a carry, loop and do addition.