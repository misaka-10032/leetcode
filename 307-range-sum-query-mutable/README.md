# Range Sum Query - Mutable

## Binary Indexed Tree

* [Tutorial 1](https://www.topcoder.com/community/data-science/data-science-tutorials/binary-indexed-trees/)
* [Tutorial 2](https://www.youtube.com/watch?v=CWDQJGaN1gY)
* Able to
 * Add marble to box `i`
 * Sum marbles from `k` to `l`
* Tree example of `0..11`

```
   _____ 0 _________________________
  /   |     |       \               \
 1    2     4        8         ____ 16 ____
      |    / \     / | \      /   |     |   \
      3   5   6   9  10 12   17   18    20   24
              |      |  | \       |     | \
              7     11  13 14     19    21 22
                           |               |
                           15              23
```

### Tree structure

* Each node takes index as key.
* `i`th level contains indices with `i` bits, e.g.
 * First layer has 1(1), 2(10), 4(100), 8(1000).
 * Second layer has 3(11), 5(101), 6(110), 9(1001), 10(1010).
 * Third layer has 7(111), 11(1011).
* Partial prefix sums are computed and stored in nodes.

### Range of node

* Prefix sums does NOT all start from `i=0`
* For a current node `c` and its parent `p`, it computes sum within `[p, c)`
* For example, `7` has parent `4`, so this node stores sum within `[4, 7)`

### Compute prefix sum

* Find the leaf node and sum up till root
* e.g. To compute `[0, 7)`
 * Sum up node 7, 4, 0.
 * Rationale is that [0, 7) = [000, 100) + [100, 110) + [110, 111)

### Find parent

* Easy way to tell parent is to flip the right most 1, e.g.
 * `11 = (1011)_2  -->  (1010)_2 = 10`
 * `10 = (1010)_2  -->  (1000)_2 = 8`
* Here's a quicker way to find parent
 * `x - (x & -x)`
 * As we know `-x` is `~x+1`
 * `&`ing that with original will only remain the rightmost `1`.

### Update value

* When value of some index is updated, multiple nodes need to be updated.
* Find the leaf interval and the other intervals that contains this interval.
 * Only two levels are affected.
 * One is the current level, all the right siblings are affected.
 * The other one is the first level, all the stems on the right are affected.
* e.g. When 8 is updated,
 * The leaf interval is like `[?, 1001)`, so node 9 is first found.
 * It's right sibling includes `1010 [8, 10)`, `1100 [8, 12)`.
 * It's right ancestors includes `10000 [0, 16)`, `100000 [0, 32)`, ...

### Find next

* Easy way to find next is to add the right most 1, e.g.
 * `1001 + 0001 = 1010` (next sibling)
 * `1010 + 0010 = 1100` (next sibling)
 * `1100 + 0100 = 10000` (next ancestor)

### Initialize

* Init the array of the same size with all 0's, whose BIT is also all zeros.
* Update values one by one.
