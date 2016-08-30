* One possible solution is to use a set of tuples to store uniques
* This solution strictly follows [Next Permutation](https://leetcode.com/problems/next-permutation/)
* Tricky next permutation
 * Requires sorted `nums` in each sub-problem
 * Pass copy of `nums` in recursion.
 * This requires that modification in sub-problem does not affect the parent one. 
 * If `nums` were global, the parent problem would be mess up by the sub-problems.
* Here's an example, the bold part is sub-problem

1 __1 2 2 3 3 ...__ <br/>
2 __1 1 2 3 3 ...__ <br/>
3 __1 1 2 2 3 ...__ <br/>
