# Maximum Swap

https://leetcode.com/problems/maximum-swap/

## Solution

A number with monotonically decreasing digits cannot be made larger. For those that are not monototically decreasing, we
first find where this trend ends.

```
99215...
    ^mono_end
```

We find the max digit after (inclusively) `mono_end`.

```
99215...8
        ^max_idx 
```

We come back and find in `num[:mono_end]` the first digit that is smaller (strictly) than the max value.

```
99215...8
  ^smaller_idx
```

We swap the two numbers pointed by `smaller_idx` and `max_idx` and get the biggest number we can get. If there are
multiple digits being the same, we should return the last one.

```
99215...8...8.....8...
  ^smaller_idx    ^max_idx
```
