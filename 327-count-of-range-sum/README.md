# Count of Range Sum

* Variant of [315 Count of Smaller Number After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/)
* First convert range sum into difference in prefix sums. Then we may find similarity.
* That problem was counting

```
c[i] = \sum_{j>i} I{ a[j]-a[i] < 0 }
```

* This problem is counting

```
c[i] = \sum_{j>i} I{ lower <= s[j]-s[i-1]<= upper }
```

or

```
c[i] = \sum_{j>i} I{ s[i-1]+lower <= s[j] <= s[i-1]+upper }
```

* !!! See README of 315 for detail !!!
* Maintain a map tracking from unique value to index.
* Build a binary indexed tree according to these indices.
* Scan backward, maintain the frequency count for each value.
* Tricky part is to also add `s[i-1]+lower` and `s[i-1]+upper` to set.
  This doesn't affect correctness, yet helps find the index in BIT quickly.
