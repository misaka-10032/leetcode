# Combination Sum

https://leetcode.com/problems/combination-sum/

## Solution

The problem can be reduced to searching a smaller target each time. We can also cache the results to save duplicate
searches.

In order to guarantee the combinations being unique, we can enforce them to be increasing. For example, if we were to
add a new candidate to a previous result, we should make sure it is the largest.
