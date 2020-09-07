# Remove All Adjacent Duplicates in String II

https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

## Solution

It's similar to [the previous problem](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/). It's
just that we need to do some further check before cancelling.

There is an optimization we must apply: if the incoming char does not cancel with the top of the stack, we should
aggregate it with the top element, instead of simply pushing it onto the stack. Otherwise, the algorithm could be `k`
times slower because we need to check `k` more elements.

```
@dataclasses.dataclass
class Node:
    char: str
    cnt: int = 1
```
