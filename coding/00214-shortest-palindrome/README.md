# Shortest Palindrome

### Naive

* Go reversely and check `startswith`

### KMP

* [ref](https://discuss.leetcode.com/topic/27261/clean-kmp-solution-with-super-detailed-explanation).
* Convert the problem into finding the longest palindrome from beginning,
  and what's remaining needs to be added back to head reversely.
* The problem can be solved trickily by building KMP table over `s+'#'+s[::-1]`.

```
 c a t a c b # b c a t a c
-1 0 0 0 1 0 0 0 0 1 2 3 4
                         ^ index of last match
```

* Notice that `t[i]=4` indicates `t[:4]==t[i-4:i]`.

* [To build table](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm#Description_of_pseudocode_for_the_table-building_algorithm)

```
i  0 1 2 3 4 5 6 7 8
s  a b a b a c a b c
t -1 0 0 1
   ^   ^ ^
   q     p

i  0 1 2 3 4 5 6 7 8
s  a b a b a c a b c
t -1 0 0 1 2
     ^   ^ ^
     q     p

i  0 1 2 3 4 5 6 7 8
s  a b a b a c a b c
t -1 0 0 1 2 3
       ^   ^ ^
       q     p

i  0 1 2 3 4 5 6 7 8
s  a b a b a c a b c
t -1 0 0 1 2 3 0
         ^   ^ ^
         q     p
```
