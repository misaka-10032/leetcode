# Rotate image

* `(i, j)` becomes `(j, n-i-1)`
* In other words, rotate values in `(i, j), (j, n-i-1), (n-i-1, n-j-1), (n-j-1, i)`
* Tricky inplace
 * Rotate the first quarter
 * For odd `n`, rotate one belt only, don't do it twice, e.g.
 * `n=5`, `(i, j) = (1, 2)`. `j` is said to be "in the belt".
   Do it for `(1, 2)->(2, 3)->(3, 2)->(2, 1)`, but not `(2, 1)`.
