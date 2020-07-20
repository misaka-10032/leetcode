# Kth Largest Element in an Array

https://leetcode.com/problems/kth-largest-element-in-an-array/

## Solution

* Finding the `k`th (1-based) largest is the same as finding the `(n-1-k)`th (0-based) smallest.
* Run `partition()` to put the first element in the range in its place, i.e. the smaller elements are on its left, and
  the bigger elements are on its right.
  * Swap a random element to the first to avoid the worst case.
* Use divide-and-conquer to find the `k`th element in a smaller range.
* The amortized complexity is `O(n)`.

### Partition Solution 1

1. Keep reducing the right pointer until the right element is smaller than the left element.
2. Swap the left and the right elements.
3. Keep increasing the left pointer until the left element is greater than the right element.
4. Swap the left and the right elements.
5. Repeat 1 until the left and the right pointer meet.

### Partition Solution 2

1. Find the first element (`gt`) that is > the pivot.
2. Find the first element (`le`) after `gt` that is <= the pivot.
3. Swap `a[gt]` and `a[le]`.
4. Move both `gt` and `le` forward.
5. Repeat 2 until `le` reaches the end.
6. Swap `a[start]` and `a[gt]`. For a stable sort, we should rotate `a[start:gt]` clockwise.

This solution can be used for a linked list as well.

### Proof

* Let <img src="https://render.githubusercontent.com/render/math?math=X_i%20%3D%201%5C%7Bp%3Di%5C%7D">,
  where <img src="https://render.githubusercontent.com/render/math?math=p"> is pivot.
* Then

<!--
function toGithubRenderURL(input) {
    return '<img src="https://render.githubusercontent.com/render/math?math=' + encodeURIComponent(input) + '">';
}
input = String.raw`\begin{align*}
T_i &= T(\max\{i, n-i-1\}) + \Theta(n) \\
T &= \sum_i X_i T_i \\
ET &= \sum_i \frac{1}{n}\big( T(\max\{i, n-i-1\}) + \Theta(n) \big) \\
   &= \frac{2\sum_{k=n/2}^{n}T(k)}{n} + \Theta(n) \\
   &\le cn + \Theta(n) \\
   &= \Theta(n)
\end{align*}`;
output = toGithubRenderURL(input);
-->

![](https://render.githubusercontent.com/render/math?math=%5Cbegin%7Balign*%7D%0AT_i%20%26%3D%20T(%5Cmax%5C%7Bi%2C%20n-i-1%5C%7D)%20%2B%20%5CTheta(n)%20%5C%5C%0AT%20%26%3D%20%5Csum_i%20X_i%20T_i%20%5C%5C%0AET%20%26%3D%20%5Csum_i%20%5Cfrac%7B1%7D%7Bn%7D%5Cbig(%20T(%5Cmax%5C%7Bi%2C%20n-i-1%5C%7D)%20%2B%20%5CTheta(n)%20%5Cbig)%20%5C%5C%0A%20%20%20%26%3D%20%5Cfrac%7B2%5Csum_%7Bk%3Dn%2F2%7D%5E%7Bn%7DT(k)%7D%7Bn%7D%20%2B%20%5CTheta(n)%20%5C%5C%0A%20%20%20%26%5Cle%20cn%20%2B%20%5CTheta(n)%20%5C%5C%0A%20%20%20%26%3D%20%5CTheta(n)%0A%5Cend%7Balign*%7D)

* `max{i, n-i-1}` is to the mimic adversarial behavior, to make `k` appear in the worst side.
* The upper bound `cn` can be proved by mathematical induction: claim for `n`, prove for `n+1`.