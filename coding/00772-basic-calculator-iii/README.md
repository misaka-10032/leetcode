# Basic Calculator III

https://leetcode.com/problems/basic-calculator-iii/

## Solution 1: Postfix Expression

See also [224](../00224-basic-calculator/README.md). There is a tricky test case with negative integers.

```
4 - -2
```

To fix this, we need to track `prev_is_num` and `num_is_negative`. We don't push `-` immediately to stack if
`not prev_is_num`. We associate the negative sign to the number if `num_is_negative`. 

## Solution 2: Recursion

See also [227](../00227-basic-calculator-ii/README.md) for how to handle `+-*/`. The `()` will be handled by recursion.
The recursive function should also take the `start` pointer as argument, and handle `)` as a termination case.
