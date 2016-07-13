# Palindrome Pairs

[Description](https://leetcode.com/problems/palindrome-pairs/)

## Solution

* Denote number of words as $n$, max word length as $k$.
 * Palindrome check takes $O(k)$.
 * Naive approach takes $O(n^2k)$, as pairing up takes $O(n^2)$.
* When $n>>k$, think it the other way.
* For each word, cache every possible complement of palindrome in a hash set.
 * Iteration over word takes $O(n)$
 * Iteration inside word takes $O(k)$
 * Palindrome check takes $O(k)$
 * Totally it takes $O(nk^2)$
* Note that there could be both left and right complements.
* Then it comes to the match phase
 * For each word, find if it is in the set, which is $O(1)$.
* Actually, we will need a dict, because we need to track the index.
* No worry about duplication, because it's said the word list is unique.