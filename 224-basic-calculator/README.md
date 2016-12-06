# Basic Calculator

* Make use of Reverse Polish Notation.
* [Infix to Postfix](https://en.wikipedia.org/wiki/Shunting-yard_algorithm).
* [Evaluate Postfix](https://en.wikipedia.org/wiki/Reverse_Polish_notation).

## Infix to Postfix

* In short,
  * stack for operators and parentheses
  * queue for result
* ![](infix-to-postfix.svg)
* Operator token: +-*/^
  * +-: 2, left
  * \*/: 3, left
  * ^: 4, right
* Number token: 0-9
* Push number token into queue
* Push operator token onto stack
  * before pushing, pop operator with >= priority for left associative ones.
    (no = for right associative ones).
* Parenthesis
  * Push ( onto stack
  * If it's ), pop till the matching ( appears.
* Popped tokens go to queue

## Compute Postfix

* In short,
  * Stack for operands.
* Push operands onto stack
* If it's operator,
  * Pop `op2`
  * Pop `op1`
  * Do `op1 op op2`
  * Push result onto stack
* Return the stack top.
