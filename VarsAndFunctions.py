#variables and functions notes
# we put a value in a variable using an = sign
x = 5
print(x) # x evaluates to 5
print(x*2) # evaluates to 10
#can assign diff types to one variable
y = 10
print(y - 2)

y = True
print(y)
# A function is composed of two parts: the header and the body.

# The header defines the name and parameters.
# A function header is written as follows: def functionName(parameters):
# The parameters are variables that will be provided when the function is called.
# The header ends with a colon to indicate that a body will follow.

# The body contains the actions (statements) that the function performs.
# The body is written under the function with an indent.
# When the lines are no longer indented, the function body ends.
# Functions usually contain a return statement. This will provide the result when the function is called.

# Example:

def double(x):
    print("I'm in the double function!")
    return 2 * x

# To call the function, we use the function's name,
# followed by parentheses which contain the data values we want to use, called function arguments.
# This function call will evaluate to an expression.

print(double(2)) # will print 4
print(double(5)) # will print 10
print(double(1) + 3) # will print 5
# can have any # of parameteres
def f(x, y, z):
    return x + y + z

print(f(1, 3, 2)) # returns 6

def g():
    return 42

print(g()) # returns 42

# Note - the number of arguments provided must match the number of parameters!
print(g(2)) # will crash
print(f(1, 2)) # would also crash if it ran

# Some functions are already provided by Python

print("Type conversion functions:")
print(bool(0))   # convert to boolean (True or False)
print(float(42)) # convert to a floating point number
print(int(2.8))  # convert to an integer (int)

print("And some basic math functions:")
print(abs(-5))   # absolute value
print(max(2,3))  # return the max value
print(min(2,3))  # return the min value
print(pow(2,3))  # raise to the given power (pow(x,y) == x**y)
print(round(2.354, 1)) # round with the given number of digits

import math #gotta do this to use some built in functions

def f(x):
    print("x:", x)
    y = 5
    print("y:", y)
    return x + y
print(f(4))
print(x) # will crash!
print(y) # would also crash if we reached it!
def f(x):
    print("In f, x =", x)
    x += 5
    return x

def g(x):
    y = f(x*2)
    print("In g, x =", x)
    z = f(x*3)
    print("In g, x =", x)
    return y + z

print(g(2))

# Another example

def f(x):
    print("In f, x =", x)
    x += 7
    return round(x / 3)

def g(x):
    x *= 10
    return 2 * f(x)

def h(x):
    x += 3
    return f(x+4) + g(x)

print(h(f(1)))
# In general, you should avoid using global variables.
# You will even lose style points if you use them!
# Still, you need to understand how they work, since others
# will use them, and there may also be some very few occasions
# where you should use them, too!

g = 100

def f(x):
    return x + g

print(f(5)) # 105
print(f(6)) # 106
print(g)    # 100

# Another example

def f(x):
    # If we modify a global variable, we must declare it as global.
    # Otherwise, Python will assume it is a local variable.
    global g
    g += 1
    return x + g

print(f(5)) # 106
print(f(6)) # 108
print(g)    # 102

#return statements -> duh
# ^ end function immediately
#no return statement _> return None
#function composition
def f(w):
    return 10*w

def g(x, y):
    return f(3*x) + y

def h(z):
    return f(g(z, f(z+1)))

print(h(1)) # hint: try the "visualize" feature

# There are a few functions from modules you'll definitely want to use in the assignments

# First: the built-in round function has confusing behavior when rounding 0.5.
# Use our function roundHalfUp to fix this.

def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    # You do not need to understand how this function works.
    import decimal
    rounding = decimal.ROUND_HALF_UP
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

print(round(0.5)) # This evaluates to 0 - what!
print(round(1.5)) # And this will be 2 - so confusing!
print(roundHalfUp(0.5)) # Now this will always round 0.5 up (to 1)
print(roundHalfUp(1.5)) # This still rounds up too!

# Second: when comparing floats, == doesn't work quite right.
# Use almostEqual to compare floats instead

print(0.1 + 0.1 == 0.2) # True, but...
d1 = 0.1 + 0.1 + 0.1
d2 = 0.3
print(d1 == d2) # False!
print(d1)       # prints 0.30000000000000004 (uh oh)
print(d1 - d2)  # prints 5.55111512313e-17 (tiny, but non-zero!)
# Moral: never use == with floats!

# Python includes a builtin function math.isclose(), but that function
# has some confusing behavior when comparing values close to 0.
# Instead, let's just make our own version of isclose:

def almostEqual(x, y):
    return abs(x - y) < 10**-9

# This will now work properly!
print(almostEqual(0, 0.0000000000001))
print(almostEqual(d1, d2))
#example of a test function
def onesDigit(n):
    return n%10

def testOnesDigit():
    print("Testing onesDigit()...", end="")
    assert(onesDigit(5) == 5)
    assert(onesDigit(123) == 3)
    assert(onesDigit(100) == 0)
    assert(onesDigit(999) == 9)
    assert(onesDigit(-123) == 3) # Added this test
    print("Passed!")

testOnesDigit() # Crashed!  So the test function worked!
