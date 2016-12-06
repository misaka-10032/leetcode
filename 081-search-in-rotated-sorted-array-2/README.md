# Search in Rotated Sorted Array II

* See 154 for finding pivot.
  * Tricky part is `l+1` disturbance when `a[m] == a[l]`.
* To decide side, compare with `a[-1]`, because `a[0]` could be pivot.
  * `target > a[0]` doesn't mean it's in the left side, because there
    isn't a left side.
  * However, there definitely is a right side, so compare with `a[-1]`.
