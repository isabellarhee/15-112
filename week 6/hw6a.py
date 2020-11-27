#################################################
# hw6a.py
#
# Name: Isabella Rhee
# Andrew Id: irhee
#section 1G0
#################################################

import cs112_f20_week6_linter
import copy
import math
#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Functions for you to write
#################################################

#################################################
# hw6a-standard
#################################################

def alternatingSum(L):
    '''
    takes list of nums and alternates adding/subtracting the elements
    '''
    sum = 0

    if len(L) == 0:
        return 0
    
    for num in range(len(L)):
        if num % 2 == 0:    #starts by adding every other
            sum += L[num]
        else:      #then subtracting every other
            sum -= L[num]
    
    return sum

def median(L):
    '''
    takes a list, sorts it, then picks middle value,
    if an even # of elements returns average of two middle ones
    '''
    L = copy.copy(L)
    L.sort()  
    med = None

    if len(L) == 0:
        return None
    elif len(L) % 2 == 1: #has an odd # of elements
        med = L[len(L) // 2]
    else:   #even # of elements
        med = (L[(len(L) // 2) - 1]) + (L[len(L) // 2]) #average two middle term
        med /= 2

    return med

def nondestructiveRemoveRepeats(L):
    '''
    copies L, then sorts through and removes repeated elements
    '''
    newL = []
    for el in L: #iterates throughe each element in da list
        if not (el in newL):  
            newL.append(el)  #add unique element to da new list
  
    return newL

def destructiveRemoveRepeats(L):
    '''
    takes L, then sorts through and removes repeated elements
    '''
    repeatIndexes = []  #list of the indexes of repeated elements
    repeatEl = []    #list of actual repeat values, without repeats
    for el in range(len(L)):   
        if L.count(L[el]) > 1 and not L[el] in repeatEl: #first repeated #
            repeatEl.append(L[el])         #adds to list of repeat values
        elif L.count(L[el]) > 1 and L[el] in repeatEl: #if a repeat but not 1st
            repeatIndexes.append(el)

    index = 0 
    numPop = 0  #number of times we have popped
    while index < len(repeatIndexes):
        L.pop(repeatIndexes[index] - numPop)#sub numPop to compensate for new
        numPop += 1                                 #length of list
        index += 1

    return None

def evalPolynomial(coeffs, x):
    '''
    takes list of coefficients that represents a polynomial
    and evaluates it at x
    '''
    total = 0
    index = len(coeffs) - 1 #the exponent starts at length - 1
    for i in coeffs: 
        total += i * (x ** index) #coefficient times x to respective exponent
        index -= 1

    return total

def areaOfPolygon(L):
    '''
    takes a list of coordinates and finds the area of the polygon created
    by said points
    '''
    L = copy.copy(L)
    L.append(L[0])  #add first term to the end for the last coordinate
    area = 0

    for i in range(len(L)-1): #goes until second to last term
        term1 = L[i][0] * L[i+1][1]  #x1*y2
        term2 = L[i+1][0] * L[i][1]  #x2*y1
        area += (term1-term2)  #add this to total

    area = abs(area / 2)    
    return area

#################################################
# hw6a-spicy
#################################################

def runSimpleProgram(program, args):
    return 42

#################################################
# Test Functions
#################################################

def _verifyAlternatingSumIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    # ignore result, just checking for destructiveness here
    alternatingSum(a)
    return (a == b)

def testAlternatingSum():
    print('Testing alternatingSum()...', end='')
    assert(_verifyAlternatingSumIsNondestructive())
    assert(alternatingSum([ ]) == 0)
    assert(alternatingSum([1]) == 1)
    assert(alternatingSum([1, 5]) == 1-5)
    assert(alternatingSum([1, 5, 17]) == 1-5+17)
    assert(alternatingSum([1, 5, 17, 4]) == 1-5+17-4)
    #----------------------------------------------
    assert(alternatingSum([5,3,8,4]) == 6)
    assert(alternatingSum([56, 4, 3,7]) == 56-4+3-7)
    assert(alternatingSum([1,2,3,4,5,6,7]) == 1-2+3-4+5-6+7)
    print('Passed.')

def _verifyMedianIsNondestructive():
    a = [1,2,3]
    b = copy.copy(a)
    # ignore result, just checking for destructiveness here
    median(a)
    return (a == b)

def testMedian():
    print('Testing median()...', end='')
    assert(_verifyMedianIsNondestructive())
    assert(median([ ]) == None)
    assert(median([ 42 ]) == 42)
    assert(almostEqual(median([ 1 ]), 1))
    assert(almostEqual(median([ 1, 2]), 1.5))
    assert(almostEqual(median([ 2, 3, 2, 4, 2]), 2))
    assert(almostEqual(median([ 2, 3, 2, 4, 2, 3]), 2.5))
    #--------------------------------------------------
    assert(median([0,5,3]) == 3)
    assert(almostEqual(median([0, 10, 4, 6]), 5))
    assert(almostEqual(median([1,1,1,1,1,1,1,1]), 1))
    print('Passed')

def _verifyNondestructiveRemoveRepeatsIsNondestructive():
    a = [3, 5, 3, 3, 6]
    b = copy.copy(a)
    # ignore result, just checking for destructiveness here
    nondestructiveRemoveRepeats(a)
    return (a == b)

def testNondestructiveRemoveRepeats():
    print("Testing nondestructiveRemoveRepeats()...", end="")
    assert(_verifyNondestructiveRemoveRepeatsIsNondestructive())
    assert(nondestructiveRemoveRepeats([1,3,5,3,3,2,1,7,5]) == [1,3,5,2,7])
    assert(nondestructiveRemoveRepeats([1,2,3,-2]) == [1,2,3,-2])
    #-----------------------------------------------------------
    assert(nondestructiveRemoveRepeats([1,2,3,2,4,4,5]) == [1,2,3,4,5])
    assert(nondestructiveRemoveRepeats([1,1,1,1,1,1,1,1]) == [1])
    assert(nondestructiveRemoveRepeats([3,2,2,4,4,5,5,6]) == [3,2,4,5,6])
    print("Passed.")

def testDestructiveRemoveRepeats():
    print("Testing destructiveRemoveRepeats()...", end="")
    a = [1,3,5,3,3,2,1,7,5]
    assert(destructiveRemoveRepeats(a) == None)
    assert(a == [1,3,5,2,7])
    b = [1,2,3,-2]
    assert(destructiveRemoveRepeats(b) == None)
    assert(b == [1,2,3,-2])
    print("Passed.")

def _verifyEvalPolynomialIsNondestructive():
    a = [2,3,0,4]
    b = copy.copy(a)
    # ignore result, just checking for destructiveness here
    evalPolynomial(a, 4)
    return (a == b)

def testEvalPolynomial():
    print("Testing evalPolynomial()...", end="")
    assert(_verifyEvalPolynomialIsNondestructive())
    # f(x) = 2x^3 + 3x^2 + 4, f(4) = 180
    assert(evalPolynomial([2,3,0,4], 4) == 180)
    # f(x) = 6, f(42) = 6
    assert(evalPolynomial([6], 42) == 6)
    # f(x) = 6x^2 -2x - 20, f(-1) = -12
    assert(evalPolynomial([6,-2,-20], -1) == -12)
    # f(x) = 6x^5-8x^3-8x, f(2) = 112, f(1) = -10, f(0) = 0
    assert(evalPolynomial([6,0,-8,0,-8,0], 2) == 112)
    assert(evalPolynomial([6,0,-8,0,-8,0], 1) == -10)
    assert(evalPolynomial([6,0,-8,0,-8,0], 0) == 0)
    #----------------------------------------------
    assert(evalPolynomial([0], 3) == 0)
    assert(evalPolynomial([1,2,3], -1) == 2)
    assert(evalPolynomial([-1,-1,2], 1) == 0)
    print("Passed.")

def _verifyAreaOfPolygonIsNondestructive():
    a = [(4,10), (9,7), (11,2), (2,2)]
    b = copy.deepcopy(a)
    # ignore result, just checking for destructiveness here
    areaOfPolygon(a)
    return (a == b)

def testAreaOfPolygon():
    print("Testing areaOfPolygon()...", end="")
    assert(_verifyAreaOfPolygonIsNondestructive())
    assert(almostEqual(areaOfPolygon([(4,10), (9,7), (11,2), (2,2)]), 45.5))
    assert(almostEqual(areaOfPolygon([(9,7), (11,2), (2,2), (4, 10)]), 45.5))
    assert(almostEqual(areaOfPolygon([(0, 0), (0.5,1), (1,0)]), 0.5))
    assert(almostEqual(areaOfPolygon([(0, 10), (0.5,11), (1,10)]), 0.5))
    assert(almostEqual(areaOfPolygon([(-0.5, 10), (0,-11), (0.5,10)]), 10.5))
    #-----------------------------------------------------------
    assert(almostEqual(areaOfPolygon([(0, 0), (0, 4), (4, 4), (4, 0)]), 16.0))
    assert(almostEqual(areaOfPolygon([(0, 0), (0, 4), (3, 0)]), 6.0))
    assert(almostEqual(areaOfPolygon([(0, 0),(1, 0)]), 0))
    print("Passed!")

def testRunSimpleProgram():
    print("Testing runSimpleProgram()...", end="")
    largest = """! largest: Returns max(A0, A1)
                   L0 - A0 A1
                   JMP+ L0 a0
                   RTN A1
                   a0:
                   RTN A0"""
    assert(runSimpleProgram(largest, [5, 6]) == 6)
    assert(runSimpleProgram(largest, [6, 5]) == 6)

    sumToN = """! SumToN: Returns 1 + ... + A0
                ! L0 is a counter, L1 is the result
                L0 0
                L1 0
                loop:
                L2 - L0 A0
                JMP0 L2 done
                L0 + L0 1
                L1 + L1 L0
                JMP loop
                done:
                RTN L1"""
    assert(runSimpleProgram(sumToN, [5]) == 1+2+3+4+5)
    assert(runSimpleProgram(sumToN, [10]) == 10*11//2)
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    # hw6a-standard
    testAlternatingSum()
    testMedian()
    testNondestructiveRemoveRepeats()
    testDestructiveRemoveRepeats()
    testEvalPolynomial()
    testAreaOfPolygon()

    # hw6a-spicy
    #testRunSimpleProgram()
 
def main():
    cs112_f20_week6_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
