# Russian Doll Envelopes

* Sort according to w, then -h. It's tricky, will show why later.
* Problem is then converted into finding a increasing subsequence in h.
  * e.g. `[[5,4],[6,4],[6,7],[2,3]]`
  * After being sorted, it becomes `[[2,3],[5,4],[6,7],[6,4]]`.
  * Look at `h`s: `[3, 4, 7, 4]`, longest one is `[3, 4, 7]`.
* Idea is valid, because the later ones are able to wrap around
  the previous ones in `w` after being sorted. Now we only need
  to check if they can be wrapped in `h` by finding the increasing
  subsequence.
* The reason to sort `h` reversely is to avoid those with the same `w`,
  e.g. `[3, 5], [3, 6]`, though `6>5`, the second one cannot wrap around
  the first one because `3==3`.
* See 300 for longest increasing subsequence.

