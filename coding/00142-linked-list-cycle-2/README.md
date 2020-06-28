# Linked List Cycle II

* Exactly the same as [141](https://leetcode.com/problems/linked-list-cycle/).
* According to Claim 2, two pointers meet at `[c-[k]]`, which is `k` steps away from start.
* Therefore we can have another `slow` start from `head`,
  and have `fast` slow down to one step each time.
* When they meet, it's the start of the cycle.
