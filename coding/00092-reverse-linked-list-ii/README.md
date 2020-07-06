# Reverse Linked List II

https://leetcode.com/problems/reverse-linked-list-ii/

## Solution

Example

```
idx  0     1  2  3  4  5
val  null  1  2  3  4  5
              ^m    ^n
```

Step 1: Initialize `left` as `head` (idx 1), and move `m-1` times to find the left boundary. In addition, track its
previous pointer `pre_left`.

How to compute range? We have `start` index (1) and `end` index (m), so range is `m-1`.

```
idx  0     1  2  3  4  5
val  null  1  2  3  4  5
              ^left
```

Step 2: Initialize `right` as `left` (idx `m`) and move `n-m` times. The same rule is applied to find the range.

```
idx  0     1  2  3  4  5
val  null  1  2  3  4  5
              ^left ^right
```

Step 3: Rotate the range given `pre_left`, `left`, `right`, `post_right`.

## Tip

Change the multiple next pointers together as a tuple to prevent reusing the stale semantic of a pointer.