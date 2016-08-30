# Substring with Concatenation of All Words

Define rolling hash as the sum of all ascii's. If hash matches, then compare content.
Use a dict to keep track of all words, like

```
{
 'foo': 1,
 'bar': 2,
 ...
}
```

The simplifying constraint is that all the words are of the same length. The exact
comparison is so simple as to compare segments of the same length.

## Possible improvements

[Better hash](https://discuss.leetcode.com/topic/37352/c-16ms-beating-99-86-simple-idea-easy-to-understand).
