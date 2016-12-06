# Sentence Screen Fitting

## Description

Given a rows x cols screen and a sentence represented by a list of words, find how many times the given sentence can be fitted on the screen.

* Note:

1. A word cannot be split into two lines.
2. The order of words in the sentence must remain unchanged.
3. Two consecutive words in a line must be separated by a single space.
4. Total words in the sentence won't exceed 100.
5. Length of each word won't exceed 10.
6. 1 ≤ rows, cols ≤ 20,000.

* Example 1:

```
Input:
rows = 2, cols = 8, sentence = ["hello", "world"]

Output: 
1

Explanation:
hello---
world---

(The character '-' signifies an empty space on the screen)
```


* Example 2:

```
Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

Output: 
2

Explanation:
a-bcd- 
e-a---
bcd-e-
```

* Example 3:

```
Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

Output: 
1

Explanation:
I-had
apple
pie-I
had--
```

## Solution

* Canonical string: insert one space between words.
* Screen string: may insert spaces at the end, or remove one
  space at the end because of new line.
* Map position in canonical str to screen or vice versa?
  * screen to canonical.
  * Logic is easier in this way, in that we simply scan the screen over,
    and insert/remove strings in the canonical str.
  * In the other direction, we may need to go back sometime in canonical str.
* At start of the row (in screen), we remove the possible space by
  moving `p` forward if it's space in canonical str.
* We also peek backwards, if it's not space, we need to rewind the previous word.
