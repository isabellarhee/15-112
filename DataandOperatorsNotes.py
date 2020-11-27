#Data types and Operators Notes
import math
def f():
    print("This is a user-defined function")
    return 42

print("Some basic types in Python:")
print(type(2))           # int
print(type(2.2))         # float
print(type(2 < 2.2))     # bool (boolean)
print(type(type(42)))    # type

print("#####################################################")

print("And some other types we may see later in the course...")
print(type("2.2"))       # str (string or text)
print(type([1,2,3]))     # list
print(type((1,2,3)))     # tuple
print(type({1,2}))       # set
print(type({1:42}))      # dict (dictionary or map)
print(type(2+3j))        # complex  (complex number)

print("Some builtin constants:")
print(True)
print(False)
print(None)

print("And some more constants in the math module:")
import math
print(math.pi)
print(math.e)

print("The / operator does 'normal' float division:")
print(" 5/3  =", ( 5/3))
print()
print("The // operator does integer division:")
print(" 5//3 =", ( 5//3))
print(" 2//3 =", ( 2//3))
print("-1//3 =", (-1//3))
print("-4//3 =", (-4//3))

#mod
print(" 6%3 =", ( 6%3))
print(" 5%3 =", ( 5%3))
print(" 2%3 =", ( 2%3))
print(" 0%3 =", ( 0%3))
print("-4%3 =", (-4%3))
#print(" 3%0 =", ( 3%0))

def mod(a, b):
  return a - (a//b)*b  #basically what the % does but written out

print(41%14, mod(41,14)) #13
print(14%41, mod(14,41))#14
print(-32%9, mod(-32,9))#4
print(32%-9, mod(32,-9)) #-4

print(3 * 2)
print(3 * "abc")
print(3 + 2)
print("abc" + "def")
#print(3 + "def")  cant mix variable types

print("Precedence:")
print(2+3*4)  # prints 14, not 20
print(5+4%3)  # prints  6, not 0 (% has same precedence as *, /, and //)
print(2**3*4) # prints 32, not 4096 (** has higher precedence than *, /, //, and %)

print()

print("Associativity:")
print(5-4-3)   # prints -2, not 4 (- associates left-to-right)
print(4**3**2) # prints 262144, not 4096 (** associates right-to-left)

print(0.1 + 0.1 == 0.2)        # True, but...
#print(0.1 + 0.1 + 0.1 == 0.3)  # False!
print(0.1 + 0.1 + 0.1)         # prints 0.30000000000000004 (uh oh)
print((0.1 + 0.1 + 0.1) - 0.3) # prints 5.55111512313e-17 (tiny, but non-zero!)$

print("The problem....")
d1 = 0.1 + 0.1 + 0.1
d2 = 0.3
print(d1 == d2)                # False (never use == with floats!)

print()
print("The solution...")
epsilon = 10**-10
print(abs(d2 - d1) < epsilon)  # True!

print()
print("Once again, using a useful helper function, almostEqual:")

def almostEqual(d1, d2):
    epsilon = 10**-10
    return (abs(d2 - d1) < epsilon)

d1 = 0.1 + 0.1 + 0.1
d2 = 0.3
print(d1 == d2)            # still False, of course
print(almostEqual(d1, d2)) # True, and now packaged in a handy reusable function!

#short circuiting
def yes():
    return True

def no():
    return False

def crash():
    return 1/0 # crashes!

print(no() and crash()) # Works!
print(crash() and no()) # Crashes!
print (yes() and crash()) # Never runs (due to crash), but would also crash (without short-circuiting)


print(yes() or crash()) # Works!
print(crash() or yes()) # Crashes!
print(no() or crash())  # Never runs (due to crash), but would also crash (without short-circuiting)
#another example
def isPositive(n):
    result = (n > 0)
    print("isPositive(",n,") =", result)
    return result

def isEven(n):
    result = (n % 2 == 0)
    print("isEven(",n,") =", result)
    return result

print("Test 1: isEven(-4) and isPositive(-4))")
print(isEven(-4) and isPositive(-4)) # Calls both functions
print("----------")
print("Test 2: isEven(-3) and isPositive(-3)")
print(isEven(-3) and isPositive(-3)) # Calls only one function!
#--------------------------------------------------------------
# Both type and isinstance can be used to type-check
# In general, (isinstance(x, T)) will be more robust than (type(x) == T)

print(type("abc") == str)
print(isinstance("abc", str))

# We'll see better reasons for this when we cover OOP + inheritance later
# in the course.  For now, here is one reason:  say you wanted to check
# if a value is any kind of number (int, float, complex, etc). 
# You could do:

def isNumber(x):
    return ((type(x) == int) or
            (type(x) == float)) # are we sure this is ALL kinds of numbers?

print(isNumber(1), isNumber(1.1), isNumber(1+2j), isNumber("wow"))

# But this is cleaner, and works for all kinds of numbers, including
# complex numbers for example:

import numbers
def isNumber(x):
    return isinstance(x, numbers.Number) # works for any kind of number

print(isNumber(1), isNumber(1.1), isNumber(1+2j), isNumber("wow"))