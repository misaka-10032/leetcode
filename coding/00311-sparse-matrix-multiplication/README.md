# Sparse Matrix Multiplication

https://leetcode.com/problems/sparse-matrix-multiplication/

## Solution

According to the matrix definition,

```
C[i][j] = sum_k { A[i][k] * B[k][j] }
```

Instead of doing a gathering, we can distribute the summed elements to the output. We do this because the matrices are
sparse, and the distribution-based approach can save compute.

For a quick lookup, we can convert A to col-based representation, and B to row-based representation. We then iterate all
the `k`s and find the non-zero combinations of `A[i][k]` and `B[k][j]` for the sum distribution.
