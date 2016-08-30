# Two Sum

## Description
* [Link](https://leetcode.com/problems/two-sum/)
* Input: `nums`, type: List[int].
* Input: `target`, type: int.
* Return: [id1, id2], type: List[int].

## Solution
* Sort indices of `nums` according to `nums`.
 * This maps `new_id` to `old_id`. 
* Sort `nums`.
 * This maps `new_id` to `num`.
* To achieve $O(n)$ worst case complexity, use a `front` and a `rear` index to greedily shrink the search space (see code for detail).
* Correctness:  Assume we now have `front` = $x_2$, `rear` = $x_5$, where $ x_1^* < x_1 < x_2 < x_3 < ... < x_4 < x_5 < x_6 < x_6^*$. Without lossing generality, assume $(x_2, x_5)$ is reduced through $(x_1^*, x_6^*) \rightarrow ... \rightarrow (x_1, x_6^*) \rightarrow (x_2, x_6^*) \rightarrow ... \rightarrow (x_2, x_6) \rightarrow (x_2, x_5)$, then
 * At $(x_1, x_6^*) \rightarrow (x_2, x_6^*)$, we have $x_1 + x_6^* < target$.
 * At $(x_2, x_6) \rightarrow (x_2, x_5)$, we have $x_2 + x_6 > target$.
 * If `front` + `rear` < `target`, $x_2$ can no longer be within a possible solution. Otherwise, $x_2$ must choose something on the right of $x_5$. However, $x_2 + x_6 > target$. That means $x_6$ is impossible, let alone anything on the right of it.
 * If `front` + `rear` > `target`, $x_5$ can no longer be within a possible solution. Otherwise, $x_5$ must choose something on the left of $x_2$. However, $x_1 + x_5 < x_1 + x_6^* < target$. That means $x_1$ is impossible, let alone anything on the left of it.