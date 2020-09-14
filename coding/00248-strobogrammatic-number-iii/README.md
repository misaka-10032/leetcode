# Strobogrammatic Number III

https://leetcode.com/problems/strobogrammatic-number-iii/

## Solution

We keep searching all possible lengths between `low` and `high`. In addition, we can also restrict a lower bound and a
upper bound during searching. We can terminate the exponential search earlier if the new digit makes the number go
beyond bounds. 
