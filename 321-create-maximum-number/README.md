# Create Maximum Number

* The problem can be broken down to two sub-problems
  * Pick $k_1$ from `nums1` and $k_2$ form `nums2`;
  * Combine these two numbers.
* The second sub-problem can be solved by greedy.
* The first one can be either solved by DP or greedy.

## Sub-problem 2: Greedy merge

* The second sub-problem can be solved by greedy merge, but be careful
* Example

```
nums1: 0, 1
       ^
nums2: 0, 9
       ^
```

* Each time pick the greater one and move the pointer.
* But when they are equal, we need to look forward to decide who to pick.
* For example, here if we peek forward, we would find `9>1`, so we pick `0` from `nums2`.

## Sub-problem 1: DP thanks to big integer

* Let `f[n][k]` represent the largest `k` len sequence given the previous `n` numbers
* `f[n][k] = max{f[n-1][k], f[n-1][k-1]*10+nums[n]}`
* Init 
  * `f[?][0] = 0`
  * `f[j][j] = (nums[0], ..., nums[j])_10`, `j=0..k-1`.
* However this exceeds time limit

## Sub-problem 1: Greedy

* Optimistic proceeding with regrets
* For example, `k=3`,

```
nums = [9, 4, 7, 9, 9]
        ^
res  = []
```

* Proceed because `res` is empty

```
nums = [9, 8, 7, 9, 9]
           ^
res  = [9]
```

* Proceed because `8 <= 9`

```
nums = [9, 8, 7, 9, 9]
              ^
res  = [9, 8]
```

* Proceed because `7 <= 8`

```
nums = [9, 8, 7, 9, 9]
                 ^
res  = [9, 8, 7]
```

* Regret because `9 > 7`

```
nums = [9, 8, 7, 9, 9]
                 ^
res  = [9, 8]
```

* Regret because `9 > 8`

```
nums = [9, 8, 7, 9, 9]
                 ^
res  = [9]
```

* Proceed because `9 >= 9`

```
nums = [9, 8, 7, 9, 9]
                 ^
res  = [9]
```

### Edge case 1

* can only regret till the rest of `nums` can all be taken, e.g.

```
k = 4
nums = [3, 4, 5, 2]
              ^
res  = [3, 4]
```

* It can no longer regret, because even if we pick all after `5`, `len([3, 5, 2]) < k`.

### Edge case 2

* If `len(res) == k`, no longer need to append `num` to it.
