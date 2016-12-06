# Find K Pairs with Smallest Sums

## Solution

* Need to keep track of candidates.
* `pos[i] = j` means the next candidate would be `(i, j)`
  if we pick `i` as first element.
* Given `pos`, each time we need to find min among `m` candidates
  `j1, j2, ..., jm`, who has smallest `nums[i]+nums[j]`.
* Min heap can be used to keep track of min's.
  Push all valid `nums1[i]+nums1[j]`s to heap.
  Sum along is not enough. We also need to keep track of `i`, `j`.
* It's possible that in the middle of the process, some `j`
  becomes `>= n`. In that case, we don't push the sum to heap.
* Edge case
  * some `j >= n`
  * `nums1` or `nums2` is empty

