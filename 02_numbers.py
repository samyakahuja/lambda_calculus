"""
So how do you represent the natural numbers given this constraint?

We create an **abstraction** where given a function f we execute
that function on a quantity x the amount of times represented
by that number.

For example, for number 3 we apply f to x 3 times. No regard is given
to what f and x are.

Note : f has to be a single argument function.
"""


ONE = lambda f: lambda x: f(x)
TWO = lambda f: lambda x: f(f(x))
THREE = lambda f: lambda x: f(f(f(x)))
...

# Testing the concept
incr = lambda x: x + 1
assert incr(0) == ONE(incr)(0)
assert incr(incr(0)) == TWO(incr)(0)

"""
what do you thing THREE(TWO) is?
    It's exponentiation. We apply function TWO, THREE times.
"""

assert THREE(TWO)(incr)(0) == 8

"""
Defining Zero

Don't apply f to x at all.
"""

ZERO = lambda f: lambda x: x

assert ZERO(incr)(0) == 0

'''
One thing to note here that the function f is not
the one defining the numbers. It is how many times
it is applied that is important.

We can define some other function f different than incr
that has some other starting point to visualize the numbers.

In case of function stars, the starting point is the empty string.
'''

def stars(x):
    return '*' + x

ZERO(stars)('') == ''
THREE(stars)('') == '***'


'''
So far we have been hard-coding the numbers. To do math
we need a better way to do this.

We can count to the next number. For example if X is a number
then so is its successor. We start from 0 since starting point
of natural numbers is zero.

We try to implement a successor function that takes a number
and returns its successor. For example SUCC(TWO) ---> THREE
'''

SUCC = lambda n: lambda f: lambda x: f(n(f)(x))

assert SUCC(TWO)(incr)(0) == THREE(incr)(0) == 3
assert SUCC(THREE)(incr)(0) == 4

# SUCC(SUCC(TWO)) == FOUR
assert SUCC(SUCC(TWO))(incr)(0) == 4

'''
Defining addition and multiplication Operations

Note: We are not addressing subtraction here since we don't
know how to undo the operation f.
'''

# ADD is just applying SUCC x times to y
ADD = lambda x: lambda y: y(SUCC)(x)

assert ADD(TWO)(THREE)(incr)(0) == 5


# MUL is like applying ((f) x times) y times
MUL = lambda x: lambda y: lambda f: y(x(f))

assert MUL(TWO)(THREE)(incr)(0) == 6
