#MiniScheme#

MiniScheme is a tiny scheme interpreter written in Python 2.7. The interpreter is a single file (scheme.py) and is less than 40 lines of code.

##Usage##

1. Clone the repo:

        git clone git@github.com:cammckinnon/MiniScheme.git

2. Navigate to the MiniScheme directory and run the interpreter by typing:

        python scheme.py

   It accepts the scheme program as input from standard in and waits for the EOF before interpreting (CTRL-D). 

3.   Or you can read input from a file like this:

        cat program.ss | python scheme.py

##Features##

 - Four standard math functions (`+ - / *`) are included. They all take an arbitrary number of parameters, except `/` which only accepts 1 parameter.

 - Lambda:

        ((lambda (x)
           (+ 1 x) 1)
        => 2

 - Equality testing:

        (equal? 1 0) => false
        (equal? 1 1) => true

 - Conditional branching (with lazy evaluation):
        
        (if (equal? (2 2)) 1 0) => 1
        (if (equal? (2 3)) 1 0) => 0

##Tests##

In the `./tests` folder there is a series of tests that check the interpreter for correctness.

        python tests.py

You may find this useful if you wish to modify the interpreter's source code.

##Example##

 - Factorial - uses recursion to compute 10! = 3,628,800 .

        ((lambda (factorial)
           (factorial 10 factorial))
          (lambda (i recurse)
            (if (equal? i 1)
              1
              (* i (recurse (- i 1) recurse)))))


##Inspiration##

Inspired by http://www.brool.com/index.php/the-tiniest-lisp-in-python .

##What's next?

I will be writing a short tutorial series (likely 3 installments) that will explore the creation of a small scheme interpreter with error-checking, macro support, and a library of built-in functions. Watch http://programmercam.posterous.com/ for updates if you're interested.