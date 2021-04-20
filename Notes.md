

# Lecture 1

- Declarative knowledge: statements of fact

- imperative knowledge: recipe -> algorithm
    - steps
    - flow of control
    - when to stop

Algorithm ->  how to perform computation, with a set of instructions and flow of control, as well as hw use combine them (the main difference between languages). convergence achieved when the termination condition is achieved.



**Computer evolution**

1. initial: with fixed program
2. stored program computer
input => memory <-> control unit <-> arithmetic logic unit => output
to memory: The input value is the same as the set of instructions (program)

as an interpreter

6 primitives: move left, move right, read, write, scan, do nothing


**programming language components**

- syntax,

- static semantics, syntactically valid strings that has meanings

- semantics: the meaning of the phrase



**program fails** (ascending order of seriousness)

- crash

- never stop - infinite loop

- run to completion but wrong answer

**objects**
scalar: int, float, bool, NoneType
non-scalar


**Good feature of Python**

- easy to learn
- most popular in life science
- easy to debug (because this is a interpreter language, with error message more understandable)

<u>Types of language</u>

- interpreted
- compiled (error message in object language, but this is more efficient)



# Lecture 2

**Integrated development environment (IDLE)**

text editor with syntax highlighting

debugger

shell



Objects

everything in python is an object

python code itself is an object

each object has a type, built in `type()`

scalar type - indivisible

- int
- float (floats are not the same thing as real number) (it is only the computer approximation of the real number)
- Boolean (`True/False`)
- NoneType
- string (there is no type char)

non-scalar

-



Expression - sequence of operands (objects) and operator

overloaded operators have a meaning that depends upon the types of operands (for example: `/` for float and int; `+` for int and string)

Program = script: a sequence of commands

variable is a way to name an object

assignment binds a name to an object

**types of program**

1. straight line programs (without loop or divisions), each command execute once

2. branching programs, each command execute at most once

   conditional statement (if, else, elif)

3. Turing complete language

   Looping construct - iteration

> how long it takes to run the program
>
> - straight line dependent on the independent of the input
> - braching program is also not proportional to the input
> - should depend on the input





# Recitation 1





# Lecture 3

**Decrementing function**

guarantee to terminate

1. map set of program variables to integer
2. starts with non-negative value
3. when the value <= 0, loop terminates
4. decreased each time through the loop



exhaustive enumeration

brute force



Approximation:

find a y such that y*y = x +- e



Faster algorithm

**Bisection search**

1. Cut the search space in half in each iteration
