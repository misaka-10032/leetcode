# Diagonal Traverse II

https://leetcode.com/problems/diagonal-traverse-ii/

## Solution

We can give the diagonals an index, and the traversal is in the index order. There is a property that helps us easily
find which diagonal an element belongs to.

```
i + j = diag_idx
```

As the matrix can be sparse, it will be too time consuming to traverse the non-existent elements. We can maintain a list
of list to track the diagonals. We can initialize the variable as follows because we know there are at most `m+n-1`
diagonals, where `m` is rows and `n` is cols.

```
[[] for _ in range(m+n-1)]
```

When we organize the final result, we need to invert the diagonal elements because we traverse the elements with a
smaller row number first, but the required order has the larger number come first.
