# Unique Word Abbreviation

## Description

* Given str, returns bool, if it's the unique abbreviation.
* Abbreviation

* Nothing within.

```
it --> it
```

* Something within.

```
localization --> l10n
```

because there're 10 letters within `l` and `n`.

* Edge case: 

## Solution

* Build a `dict` that maps abbreviation to a set of words of the same abbr.
* When testing
  * if `word` is in it, assert the word set only contains that word.
  * Otherwise, assert the word set is empty, which is impossible.
