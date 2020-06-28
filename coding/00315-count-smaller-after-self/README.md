# Count of Smaller Numbers After Self

## Frequency Table

* Fix-valued Frequency Table for Range Queries
  * val list
  * Binary Indexed Tree (BIT) of freq
  * val's are sorted, idx can be found with binary search
  * range sum query with BIT

## Solution

* Sort the unique values

`2, 6, 5, 5, 1 ==> 1, 2, 5, 6`

* Map from value to index

`1(0), 2(1), 5(2), 6(3)`

* Scan __the original__ from back; keep track of frequency of numbers.
* Return `res` also reversely.

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

## Debug

* `BITree.prefix()` is inclusive, but `FreqTable.prefix()` is exclusive.
* Should reverse `res` at last, as we scanned reversely.
