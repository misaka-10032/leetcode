# Longest Increasing Subsequence

### Naive

* `f[i]` denotes the longest increasing subsequence up till `i`th element.
* `f[i] = max_j(f[j] +  (a[i] > a[j]))`
* Complexity is `O(n^2)`

### Optimization

* Don't need to traverse all the previous numbers.
* Rearrange them into an array `tails`
  * `tails[i-1]` stores the __minimum__ last element for
    the increasing subsequence with `i` elements
  * e.g. if we have `[4, 5]` and `[5, 6]` as increasing
    subsequence with size 2 up till now, then `tails[1]`
    would be `5` because it's smaller than `6`.
* The problem is converted into finding an index `i`, such that
  * `tail[p] < tails[i]`, for `p` in `[0, i)`
  * `tail[q] >= tails[i]`, for `q` in `[i, n)`
* After finding this `i`, see if we can update `tails[i]` with
  current value as a smaller tail.
* Init `tails` with `n` `inf`'s.
