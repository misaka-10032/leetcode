# Find Minimum in Rotated Sorted Array

* Simplifying constraint: no duplicate.
* Characteristic: `a[p]<a[r]<a[l]`.
* When `a[l]<a[r]`, terminate early, because `a[l]` is the minimum.
* Define Left group as `[l, p)`, right group as `[p+1, r]`.
* When `a[m]>a[l]`, it indicates `m` is in left group. Min is at least at `m+1`.
* When `a[m]<a[l]`, it indicates `m` is in right group. Min is at most at `m`.
* Shrink the range.
