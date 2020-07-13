# K Closest Points to Origin

https://leetcode.com/problems/k-closest-points-to-origin/

## Solution

Maintain a **max** heap of `k` elements. It might seem a bit counter-intuitive as we need the "closest" points. The max
heap is to kick out the non-interesting points. Python only has a min heap. The max heap can be achieved by negating the
the distance used for comparison.
