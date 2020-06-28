# Game of Life

* Iterative update needs two matrices.
* If interviewer insists on inplace, then encode the current state
  and the next state with one number. First bit is next; second bit
  is current.
  * `01` means current is alive, next will die.
