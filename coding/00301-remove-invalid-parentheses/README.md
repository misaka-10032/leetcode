# Remove Invalid Parentheses

https://leetcode.com/problems/remove-invalid-parentheses/

## Solution

Start with the greedy solution to probe the minimal number of '(' and ')' to remove
([easier exercise](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/)). Then DFS all the possible
removals and early return if the budgets are used up.

```
def remove_recur(
    self, s: str, curr_idx: int, curr_left_cnt: int,
    left_rm_budget: int, right_rm_budget: int, kept_chars: List[str],
    sol: Set[str]):
```
