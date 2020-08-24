# Pow(x, n)

https://leetcode.com/problems/powx-n/

## Solution

`n` can be positive, negative, and zero. When it's zero, we return 1. When it's negative, we can reduce the problem to
the positive case, and return `1/v` as result. Then, let's talk about the positive case.

The power can be represented in its binary form, and the corresponding power values at the `1` bits can be easily
computed. Therefore, we make a table of the following values

```
order  0    1    2    3    ...
powers 1    2    4    8    ...
vals   x**1 x**2 x**4 x**8 ...
```

We find the 1 bits and reduce them with multiplication. For example, `13 = (1101)_2`, so

```
x**13 = (x**1) * (x**4) * (x**8) 
```
