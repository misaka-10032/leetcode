# Interval List Intersections

https://leetcode.com/problems/interval-list-intersections/

## Solution

We keep creating new intersections, and move the range pointers forward. Without losing generality, assuming the first
range has a smaller start, we have the following cases

* Case 1

```
 |_____|
   |__|
```

* Case 2

```
 |_____|
   |_____|
```

* Case 3

```
 |_____|
          |_____|
```

In all the above cases, the new interval, if it exists, will be

```
[max(left1, left2), min(right1, right2)]
```

The next range to consider is the range with a smaller `right`.