# Linked List Cycle

* `fast` moves two steps each time
* `slow` moves one step each time
* Claim 1: if `fast` and `slow` start at the start of the cycle, they meet at there.
* Proof: let `x` be number of steps `slow` moves, and `c` be cycle size, then

$$
2x - x = c \\
x = c
$$

* Claim 2: if start of cycle is `k` steps away from start of list,
  then `fast` is `k` steps away from start of cycle when `slow` enters the cycle.

* Claim 3: `fast` and `slow` meet at $[c-[k]]$, where $[x]$ means `x%c`.
 
$$
2x - x = [c - [k]] \\
x = [c - [k]]
$$
