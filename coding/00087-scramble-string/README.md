# Scramble String

* String can be swapped according to pivot.
* Left and right side of the pivot are two sub-problems.
* Solve the sub-problems with divide and conquer.
* The sub-problems can be characterized by two ranges in proposal and target.
* The zero problem is that only one char is left and they are equal
  in proposal and target.
* Cache the intermediate results in case it's further used.
