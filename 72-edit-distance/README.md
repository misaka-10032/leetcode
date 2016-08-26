# Edit Distance

* Let `d[i][j]` be edit distance between `[0, i]` of word1 and `[0, j]` of word2.
* `d[i][j]` is min of
  * `1+d[i-1][j]`
  * `1+d[i][j-1]`
  * `d[i-1][j-1] + w1[i]!=w2[j]`
* Edge case
  * d[-1][j-1] = j
  * d[i-1][-1] = i
