# Count of Smaller Numbers After Self

## Binary Indexed Tree

* Sort the unique values

`2, 6, 5, 5, 1 ==> 1, 2, 5, 6`

* Map from value to index

`1(0), 2(1), 5(2), 6(3)`

* Scan from back; keep track of frequency of numbers

```
Incoming: 1
idx   0 1 2 3
val   1 2 5 6
freq  0 0 0 0
prefix sum [0, 0): 0
freq  1 0 0 0

Incoming: 5
idx   0 1 2 3
val   1 2 5 6
freq  1 0 0 0
prefix sum [0, 2): 1
freq  1 0 1 0

Incoming: 5
idx   0 1 2 3
val   1 2 5 6
freq  1 0 1 0
prefix sum [0, 2): 1
freq  1 0 2 0

Incoming: 6
idx   0 1 2 3
val   1 2 5 6
freq  1 0 2 0
prefix sum [0, 3): 3
freq  1 0 2 1

Incoming: 2
idx   0 1 2 3
val   1 2 5 6
freq  1 0 2 1
prefix sum [0, 1): 1
freq  1 1 2 1
```
