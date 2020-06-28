# Zigzag conversion

## Description

* [Link](https://leetcode.com/problems/zigzag-conversion/)
* Input: s, type: str
* Input: numRows, type: int
* Output: new_s, type: str

```
0:    a     a     a
1:    b   f b   f b
2:    c e   c e
3:    d     d
```

## Solution

* When `numRows` is 1, return the original string.
* The first and last row of output are just a series of chars with fixed `step`
 * step = 2 * numRows - 2
* Those in the middle not only have these chars, but also have an extra char in each step. The extra char is `delta` away from the beginning of period (`start`), which is linear to the row index.
 * delta = (numRows - start - 1) * 2
* `str` is immutable. Each time a new char is appended, all the chars are copied into a new string, so use a char list, and concat them up at the end.