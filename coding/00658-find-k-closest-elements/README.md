# Find K Closest Elements

https://leetcode.com/problems/find-k-closest-elements/

## Solution

First, find the closest element in the array. `bisect_left()` helps us find the first element that is `>=` the target.
However, the closest element could be smaller. Thus, we need to probe one element ahead. If the previous element exists
and is closer or equally close to the target value, we return the previous element. Notice that we should return the
previous element even if it's equally close because the problem prefers small elements.

Then, probe the left and the right boundary until the length condition is met. Again, the left element is preferred if
the two values are equally close.
 