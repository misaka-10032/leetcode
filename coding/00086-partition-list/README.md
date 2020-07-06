# Partition List

https://leetcode.com/problems/partition-list/

## Solution

Example

```
 (3) null  1  4  3  2  5  2
  ^pivot
```

Step 1. Find the first element (`it_ge`) that is >= `pivot`. In addition, track its previous pointer.

```
null  1  4  3  2  5  2
         ^it_ge
```

Step 2. Initialize `it_lt` as `it_ge`.

```
null  1  4  3  2  5  2
         ^it_ge
         ^it_lt
```

Step 3. Find the first element (`it_lt`) after (inclusive) its current position that is < `pivot`. In addition, track
its previous and post pointers.

```
null  1  4  3  2  5  2
         ^it_ge
               ^it_lt
```

Step 4. **Rotate** counter clockwise between `it_ge` and `it_lt`.

```
null  1  2  4  3  5  2
            ^it_ge
                  ^post_it_lt
```

Step 5. Move `it_lt` to `post_it_lt`. Repeat step 3 until it points to end (null).

## Common mistake

* We are asked to preserve the original order, so we should **rotate** the range, instead of swapping as we do for quick
  sort on arrays.
 