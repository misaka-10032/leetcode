# Maximum Product of Three Numbers

https://leetcode.com/problems/maximum-product-of-three-numbers/

## Solution

Let's denote `+` as non-negative numbers, and `-` as negative numbers. The result can be one of the following cases.

### Non-negative Result

* `+++`

The biggest is from `sorted_nums[-3:]`.

* `--+`

### Negative Result

The biggest is from `(sorted_nums[:2] + sorted_nums[-1:])`, because we want the negative number as small as possible,
and the non-negative number as big as possible.

* `-++`

The biggest is around zero, because we want the negative number as big as possible, and the non-negative numbers as
small as possible. However, there cannot be 3 non-negative numbers, otherwise, `+++` must have made a bigger product.
Therefore, the biggest selection is from `sorted_nums[-3:]` as well.

* `---`

There cannot be non-negative numbers, because otherwise, `--+` could have made a bigger product, because the product is
non-negative. As we want the candidates as big as possible to make a big negative product, they must come from
`sorted_nums[-3:]` as well.

### Summary

All the above cases have the candidates from one of the following cases.

* `sorted_nums[-3:]`
* `(sorted_nums[:2] + sorted_nums[-1:])`

Therefore, we sort the array, and compare these two products.
