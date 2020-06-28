# 3Sum Smaller

* Given `nums` and `target`, find index triplets `(i, j, k)`,
  such that `0 <= i < j < k < n` and `nums[i] + nums[j] + nums[k] < target`.
 

## Solution

* Sort
* Three pointers `i, j, k`.
* The first pointer goes as usual
* The last two pointer is tricky
  * One goes from start
  * The other goes from end
  * Break when they meet
  * when current sum is smaller, it's guaranteed that
    `k` being `j+1..k` are all valid, so we add these many `cnt`s.
    Then we move the left pointer `j` to see new posibilities.
  * otherwise, move the right pointer
* It `O(n)`. It saves complexity to count one by one.
  But if we need the exact indices as result, we still need
  to do that one by one.

## Solution naive

* Sort
* Three pointers
* Early break when it's >= target
* As we return indices, we represent the sorted array in the
  form of indices.