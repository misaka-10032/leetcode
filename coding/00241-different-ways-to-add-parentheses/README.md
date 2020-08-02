# Different Ways to Add Parentheses

https://leetcode.com/problems/different-ways-to-add-parentheses/

## Solution

First, we parse the expression as a list of numbers and ops. Then we add parentheses in a divide-and-conquer manner.

```
(...)<op>(...)
```

We iterate the `op`s used to split the expression, unless we have a single number. Each subexpression has a list of
possible result. We do a Cartesian product of two sets, and compute a list of new results.
