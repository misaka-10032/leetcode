# Expression Add Operators

https://leetcode.com/problems/expression-add-operators/

## Solution

The problem can been taken as adding `('', '+', '-', '*')` in-between the digits to achieve `target`. As leading 0's are
not allowed, we need to take special care before adding `''`.

The eval result can be tracked on the fly. See also the
[calculator problem](https://leetcode.com/problems/basic-calculator-ii/). To summarize, an expression can be taken as
the sum of products. We finalize and reset the current number when we see an operator. We multiply this number to the
current product if the operator is `*`. We aggregate the sum if the operator is `+` or `-`.

The recursive problem can be defined as

```
def _search(self, num: str, target: int, idx: int,
            curr_num: int, curr_prod: int, curr_sum: int,
            ops: List[str], results: List[str]):
```

`curr_num`, `curr_prod`, `curr_sum` are the states used to track the eval result. `ops` is used to recover the final
expression. We can rely on Python's `eval`, but this is slow because we need to waste `O(n)` to make the expression that
does not equal our target.