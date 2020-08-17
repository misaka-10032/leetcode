# Minimum Window Substring

https://leetcode.com/problems/minimum-window-substring/

## Solution

We track the characters in the window in two pointers.

* `residue` tracks the characters needed to match `t`.
* `overflow` tracks the overflowing characters from `residue`.

When we add a character from the right, we should first try decrementing the `residue` counter. If missing, we then add
it to the `overflow` counter. When we remove a character from the left, we should first try decrementing the `overflow`
counter. If missing, we add it to the `residue` counter.

The idea is to find the closest right of the window to contain `t`'s chars. Then find the farthest left of the window to
still contain `t`'s chars. Then repeat.

```
while right < len(s):
  right = _find_right_boundary()
  if right == len(s):
    break
  left = _find_left_boundary()
  _maybe_update_min_state()
  residue[s[left]] += 1
  left, right = left+1, right+1 
```  
