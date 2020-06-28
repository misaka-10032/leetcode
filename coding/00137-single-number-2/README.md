# Single Number II

Thanks [ziyihao](https://discuss.leetcode.com/topic/22821/an-general-way-to-handle-all-this-sort-of-questions)

General solution for anomaly detection.
* Assume all appear `K=3` times, except one for `M=1` time.
* Use a counter to record state. It can be 0, 1, 2, which is sufficient to be represented with 2 bits.
* Denote the two bits of counter as `a` and `b`.
* Focus on any one bit of the incoming numbers; let it be `c`.
* Write down the logical table.

```
current   incoming  next
a b            c    aa bb
0 0            0    0  0
0 1            0    0  1
1 0            0    1  0
0 0            1    0  1
0 1            1    1  0
1 0            1    0  0
```

* The transfer table can be written in [canonical form](https://en.wikipedia.org/wiki/Canonical_normal_form).
* Write the transfer bit by bit.
* For a, pick out two rows where `aa=1` under next.

```
current   incoming  next
a b            c    aa bb
1 0            0    1  0
0 1            1    1  0

aa = (a&~b&~c)|(~a&b&c)
```

* Similar, for `bb`

```
current   incoming  next
a b            c    aa bb
0 1            0    0  1
0 0            1    0  1

bb = (~a&b&~c)|(~a&~b&c)
```

Simplify it if you like, but that's enough.

* If the anomaly is `M=1=(01)_2`, where `a=0` and `b=1`, it can be recovered by `~a&b`.
* But the problem seems not have mentioned how many times it appears, so it can appear once (`a=0`, `b=1`) or twice (`a=1`, `b=0`), which can be recovered by

```
a|b
```

* That applies to one bit, and also applies to the whole number.
