# Candy

* Peek forward; handle three cases: ascendant, descendant, unchanged.
* Handle sequence cohort by cohort.
  * Hereby define a cohort as a strictly increasing/decreasing or unchanged sequence.

## Case discussion

### Ascendant cohort

```
3 | 2, 3, 4, 5 | 2
```

* The candy given to the first one depends on the previous cohort.
* The latter ones keep increasing 1's.

### Descendant cohort

```
3 | 5, 4, 3, 2 | 3
```

* The candy given to the first one not only depends on the previous cohort,
  but also constraint by the length of the sequence.

### Unchanged sequence

```
2 | 3, 3, 3, 3 | 2
```

* There's no constraints for those in the middle.
* Giving them one will make them happy.

## Rolling cohorts

* We we roll on the the next cohort, make the last one appear in the first place
  of the next cohort.
  
```
| 3, 4, 5 | 4, 3, 2, 1    -->    3, 4, | 5, 4, 3, 2, 1 |
```

* The initial number carries on for the reference of the next cohort.
* Edge case (here `5`) may need to be adjusted when the cohort size is greater than
  the candies assigned by the previous cohort.
