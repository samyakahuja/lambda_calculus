"""
Limitation on the system
========================

    - **Only** *single* argument functions are allowed. Nothing else.
    - Following among others are not allowed:
        
        - No packages
        - No objects
        - No Control Statements
        - No numbers
        - No strings
        - No Datatypes

"""

"""
We first try to emulate a switch that gets
two inputs. One Left and One Right. We can
implement it as such.

Here LEFT return the Left of the two items
example - LEFT("1")("2") return "1"

Here RIGHT returns the Right of the two items
example - RIGHT("1")("2") returns "2"

"""

def LEFT(x):
    return lambda y: x

def RIGHT(x):
    return lambda y: y

assert LEFT("1")("2") == "1"
assert RIGHT("1")("2") == "2"


"""
We can take the above logic to implement
True and False. (LEFT = TRUE, RIGHT = FALSE)
"""

def TRUE(x):
    return lambda y: x

def FALSE(x):
    return lambda y: y

assert TRUE("1")("2") == "1"
assert FALSE("1")("2") == "2"

"""
We can now use TRUE and FALSE to implement Boolean Logic
"""

def NOT(x):
    return x(FALSE)(TRUE)

assert NOT(TRUE) is FALSE
assert NOT(FALSE) is TRUE


"""
We can also implement AND and OR.

AND:

    How is AND implemented in python?
        
        >>> 2 and 3
        3
        >>> 0 and 3
        0

    This means that 
        - if x is TRUE then y is the result.
        - if x is FALSE then x is the result

OR:

    - if x is TRUE then x is the result.
    - if y is FALSE then y is the result.
"""

def AND(x):
    return lambda y: x(y)(x)

assert AND(TRUE)(TRUE) is TRUE
assert AND(TRUE)(FALSE) is FALSE
assert AND(FALSE)(TRUE) is FALSE
assert AND(FALSE)(FALSE) is FALSE

def OR(x):
    return lambda y: x(x)(y)

assert OR(TRUE)(TRUE) is TRUE
assert OR(TRUE)(FALSE) is TRUE
assert OR(FALSE)(TRUE) is TRUE
assert OR(FALSE)(FALSE) is FALSE
