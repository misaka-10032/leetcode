# Basic Calculator II

https://leetcode.com/problems/basic-calculator-ii/

## Solution

An expression with `+-*/` only can be broken down to sum of products

```
(0+) (1*)a*b/c + (1*)d*-e/f - (1*)g*h + ...
               ^            ^         ^
```

We need a parser to parse the expression item by item. An item can be

* A non-negative number
* An operator

In the meantime, we also need to track the following states

* `curr_sum`: the current sum so far.
* `prev_sum_op`: the sum op (+ or -) to use for the next number.
* `curr_prod`: the current product so far.
* `prev_prod_op`: the product op (* or /) to use for the next number.

To handle negative numbers, we also need to track

* `prev_is_num`. If the current op is `-` and this flag is false, we need to take this `-` as sign instead.

We do the following for the parsed items:

* Number
  * Update `curr_prod`.
  * Set `prev_is_num`.
* `-` and `not prev_is_num`
  * Reverse `curr_sum_op`.
* `+` or `-`
  * Update `curr_sum` based on `curr_sum_op`.
  * Update `curr_sum_op`.
  * Reset `prev_is_num`.
  * Reset `curr_prod` to 1.
  * Reset `prev_prod_op` to `*`.
* `*` or `-`
  * Update `prev_prod_op`.
  * Reset `prev_is_num`.
  
### Example

```
item         | init |  2  +  -  2  /  2  | last
-------------+------+--------------------+-----
curr_sum     |  0   |     2  2           |  1
curr_prod    |  1   |  2  1     2     1  |
prev_is_num  |  0   |  1  0     1  0  1  |
prev_sum_op  |  +   |     +  -           |
prev_prod_op |  *   |     *        /     |
```
