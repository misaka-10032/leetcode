# Find K Pairs with Smallest Sums

https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

## Solution

First, we fix the first element of the first array, and pair it with all the elements in the second array. The pairs
will be put into a min heap.

Then we keep popping from the heap to find the minimal pairs. After popping, we will try to proceed in the first array,
if it still has more elements to come.

Let's denote the length of the first array to be `m` and that for the second array to be `n`. Then the time complexity
will be `log n`. In order to make the algorithm run faster, we can possibly swap the two arrays, such that the second
array is shorter. We also need to track this bit, because we also need to revert the pair in the result if two arrays
are swapped.
