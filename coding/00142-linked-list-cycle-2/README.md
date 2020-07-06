# Linked List Cycle II

https://leetcode.com/problems/linked-list-cycle-ii/submissions/

## Solution

* Make a `fast` that moves two steps each time.
* Make a `slow` that moves one step each time.
* They meet if there is loop.
* Once they meet, kill `fast` and restart a `slow` at head.
* The two `slow` pointers will eventually meet at the start of the loop.

## Proof



* Exactly the same as [141](https://leetcode.com/problems/linked-list-cycle/).
* According to Claim 2, two pointers meet at `[c-[k]]`, which is `k` steps away from start.
* Therefore we can have another `slow` start from `head`,
  and have `fast` slow down to one step each time.
* When they meet, it's the start of the cycle.
