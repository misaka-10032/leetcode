# Group Shifted Strings

https://leetcode.com/problems/group-shifted-strings/

## Solution

Each group can elect an representative. It can be the very first string of the group, i.e. to shift the first character
to `a` and shift the rest accordingly. All the strings of the same group can be keyed by this representative.

The amount to be shifted of the following chars can be computed as follows.

```
(ord(string[i]) - ord(string[0])) % 26
```

The modulo is important, because the first char can be very large, e.g. `z`.
