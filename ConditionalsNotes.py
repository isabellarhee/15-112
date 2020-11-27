#if statement
def f(x):
    print("A", end="")
    if (x == 0):
        print("B", end="")
        print("C", end="")
    print("D")

f(0)
f(1)

# again, with same-line indenting

def abs2(n):
    if (n < 0): n = -n # only indent this way for very short lines (if at all)
    return n

#if - else statements -> we been knew

#elif statements
def f(x):
    print("A", end="")
    if (x == 0):
        print("B", end="")
        print("C", end="")
    elif (x == 1):
        print("D", end="")
    else:
        print("E", end="")
        if (x == 2):
            print("F", end="")
        else:
            print("G", end="")
    print("H")

f(0)
f(1)
f(2)
f(3)

# if-else expression (not an if-else statement!)

def abs7(n):
    return n if (n >= 0) else -n
