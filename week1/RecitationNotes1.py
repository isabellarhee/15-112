#distance
#Distance formula
# sqrt((x1-x2)^2 + (y1-y2)^2)
#in python
import math
def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

print(distance(0,0,0,1))
print(distance(1,1,4,5))


#casting-------------------------------------------
#just type the variable type before the thing ex string is str

#--------------------------------------------------
#  circlesIntersect
def circlesIntersect(x1,y1,r1,x2,y2,r2):
    d = distance(x1, y1, x2, y2)
    if (d > r1+r2):
        return 0
    elif (d = r1+r2):
        return 1
    else:
        return 2

# assert() function tests if something is true then continues executing
#if false, returns assertion error
#example assert(circlesIntersect(0, 0,2,3,0,2)==2)
#used to test functions


#is Factorish--------------------------------------
def isFactory(n):
    if not isInstance(n, int):
        return False
    n = abs(n)
    if !(n <= 999) or (n < 100):
        return False
    leftDigit = n // 100
    midDigit = (n //10) % 10
    rightDigit = n % 10
    if leftDigit != midDigit or midDigit != rightDigit:
        return False
    return leftDigit % 2 == 0

#write the function ^^ that takes a value n that can be of any type
#and returns True if n is a (possibly egative) integer with exactly
#3 dwual even digits (so all three digits are the same and are even)
# in all other cases, the function returns false (without crashing)

#first: check the type
#second: handle negatives
#third: handle the # of digits
#fourth: check that all digits are equal
#fifth: check that they are even