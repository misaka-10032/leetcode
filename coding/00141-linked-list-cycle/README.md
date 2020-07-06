# Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/

## Solution

* Make a `fast` that moves two steps each time.
* Make a `slow` that moves one step each time.
* They meet if there is loop.

### Claim 1

If the start of the cycle is `t1` steps away from `head`, then `fast` is `t1 % c` steps away from start of cycle when
`slow` enters the cycle.

**Proof:** `fast` is twice as fast, so when `slow` enters the cycle (`t1` steps from `head`), `fast` should have
progressed `2 * t1` steps. The first `t1` steps are outside the cycle, and the later `t1` steps are inside the cycle.
Considering `c` could be smaller than `t1`, `fast` should have reached `t1 % c` in the cycle at the moment.

### Claim 2

`fast` and `slow` meet at `c - (t1 % c)` at the cycle.

**Proof:** When `fast` and `slow` meet, `fast` would have made `c` steps more than `slow` in the cycle. Denote `t2` as
the time `slow` spent in the cycle, then we have the following

```
(t1 % c) + 2 * t2 = t2 + c
t2 = c - (t1 % c)
```

### Claim 3

If we start another slow pointer `slow2` once `slow` and `fast` meet, `slow` and `slow2` will meet at the start of the
cycle.

**Proof:** After another `t1` time units, `slow2` would reach the start of the cycle. On the other hand, `slow` would
reach

```
(t1 + t2) % c
= (t1 + c - (t1 % c)) % c
= (t1 + c - t1) % c
= 0
```