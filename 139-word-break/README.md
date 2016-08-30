# Word Break

* Let `f[i]` be whether `s[:i]` can be segmented or not
* `f[i] = or_{w in dict and s[:i] ends with w}{ f[:i-len(w)] }`
* Edge case `f[<0] = False`
* Init `f[0] = True`