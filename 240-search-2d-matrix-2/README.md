# Search a 2D Matrix II

* Start from top right.
* According to definition, all on its left is smaller and
  all on its bottom is larger.
* Therefore, if target is smaller, we can rule out of the column.
  Else if target is larger, we can rule out of the row.
* Complexity is `O(m+n)`.
