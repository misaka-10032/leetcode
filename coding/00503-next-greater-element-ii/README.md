# Next Greater Element II

https://leetcode.com/problems/next-greater-element-ii/

## Solution

It is similar to [the previous problem](https://leetcode.com/problems/next-greater-element-i/), except that

* There could be duplicate candidates.
* The array is circular.

To solve the first problem, we need to map the index, instead of the value. To solve the second one, we need to scan the
array twice. In the second pass, we no longer push elements, and early return if the stack has a single element left.
