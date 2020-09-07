# Nested List Weight Sum II

https://leetcode.com/problems/nested-list-weight-sum-ii/

## Solution

The weight is defined as `max_depth-depth+1`, where the depth of first level is 1. Of course, we can do it in two
passes, with the first pass for `max_depth`. However, the interviewer might be interested in a one-pass solution that
could be used for the streaming data.

The idea is to not only track the current sum, but also track a flat sum. We start with the guess of `max_depth` being
1, and whenever the max depth is increased, we elevate the previous element based on their flat sum. Here is an example.

```
1  1
   ^
      2  2
                     3
            4   4
```

We start with the first level. We thought the max depth was 1, so both `tot` and `flat_tot` are (1+1=) 2.

However, when we see a 2 in the next level, we should elevate `tot` by `flat_tot`, because we didn't not apply enough
weights on them. Similarly, when we proceed to 4, we have the following.

 
```
      1  1
         ^
            2  2
                           3
                  4   4
                  ^
tot   1  2  6  8  24
flat  1  2  4  6  10
```

When we see 4 that increases `max_depth` by two, we should elevate `tot` by twice `flat_tot`.

Here is another explanation of the algorithm. The result can be written as follows.

```
(1+1)*4 + (2+2)*3 + (4+4)*1 + 3*2
```

It can also be written as follows

```
(1+1)*(1+1+2) + (2+2)*(1+2) + (4+4)*1 + 3*2
```

which reflects our update on the weights. Before we meet 4, we have our current sum being

```
(1+1)*(1+1) + (2+2)*1
```

However, when we update the max depth to 4, we need to add the following to the current total.

```
(1+1+2+2)*(4-2)
```

Then, we can safely add 4 to the sum as usual.

### Recursion

We can put `max_depth`, `flat_tot` and `tot` as output arguments, and rely on the recursion to update them.

```
def _depth_sum(nested_list: List[NestedInteger], depth: int,
               max_depth: List[int], flat_tot: List[int], tot: List[int]):
```
