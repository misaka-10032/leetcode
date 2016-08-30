# Decode Ways

* Let `f[i]` be number of decode ways using `[0, i]` of the code.
* If last digit is valid, `f[i] += f[i-1]`.
* If last two digits is valid, `f[i] += f[i-2]`.
