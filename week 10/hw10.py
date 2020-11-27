#################################################
# hw10.py
#
# Your name: Isabella Rhee
# Your andrew id: irhee
# section: 1G0
#################################################

import cs112_f20_week10_linter
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

def hasAdjacentValues(L):
    '''
    takes a list L of N integers, returns True if (v-1) or (v+1), or both, 
    are also in L, O(n) time
    '''
    S = set(L)  #get rid of repeats  #O(n)

    for num in S:  #O(n)
        temp1 = num - 1  #adjacent numbers to check
        temp2 = num + 1
        if temp1 in S or temp2 in S: #O(1)
            return True

    return False

def hasTriplicate(L):
    '''
    takes list L of N integers, returns True if exists v such that there are
    at least 3 instances of it false otherwise, O(n) time
    '''
    itemDict = dict() #maps each value to a counter for each instance
    for item in L: #O(n)
        if item not in itemDict: #O(n)
            itemDict[item] = 1
        else:
            itemDict[item] += 1
        
        if itemDict[item] >= 3:  #O(n)
            return True

    return False

def boxesAnInteger(L):
    '''
    takes list of non negative floats, return true if there exists exactly
    one integer that goes in between any of the floats, false otherwise
    O(nlogn) time
    '''
    L.sort() #O(nlogn)
    temp = -1 #to store last value and compare to current
    for num in range(len(L)): #O(n)
        if math.floor(L[num]) == math.ceil(temp) and \
                math.floor(L[num]) < L[num] and math.ceil(temp) > temp:  #O(1)
            return True   #^makes sure the floor/ceil numbers aren't ints
        temp = L[num]                               #initially

    return False

#################################################
# Test Functions    
#################################################

def testHasAdjacentValues():
    print('Testing hasAdjancentValues()...', end='')
    assert(hasAdjacentValues([1,5,8,2]) == True)
    assert(hasAdjacentValues([1,5,8,0]) == True)
    assert(hasAdjacentValues([1,5,8,4]) == True)
    assert(hasAdjacentValues([1,5,8,6]) == True)
    assert(hasAdjacentValues([1,5,8,3]) == False)
    assert(hasAdjacentValues([1,5,8,-5]) == False)
    assert(hasAdjacentValues([ ]) == False)
    assert(hasAdjacentValues([2,0,-2]) == False)
    assert(hasAdjacentValues([1,-1,2,0]) == True)
    assert(hasAdjacentValues([-15,16,19,-21,0]) == False)
    assert(hasAdjacentValues([-15,16,-16,-21,0]) == True)
    #---------------------------------------------------
    assert(hasAdjacentValues([-1,5,8,-2]) == True)
    assert(hasAdjacentValues([1,3,5,7]) == False)
    assert(hasAdjacentValues([0,0,0,0]) == False)
    assert(hasAdjacentValues([1,2,3,4]) == True)
    print('Passed! (pending O() check)')

def testHasTriplicate():
    print('Testing hasTriplicate()...', end='')
    assert(hasTriplicate([ 1, 1, 1 ]) == True)
    assert(hasTriplicate(list(range(10))*3 ) == True)
    assert(hasTriplicate([ ]) == False)
    assert(hasTriplicate(list(range(100))*2) == False)
    assert(hasTriplicate([ 1, 2, 3 ]) == False)
    assert(hasTriplicate([ 1, 2, 3, 1 ]) == False)
    assert(hasTriplicate([1, 5, 1, 1, 2]) == True)
    assert(hasTriplicate([-3, -2, 1, -2, -2, 3]) == True)
    assert(hasTriplicate([-3, -2, 1, -2, 2, -3]) == False)
    assert(hasTriplicate(list(range(-1000, 1000))) == False)
    assert(hasTriplicate(list(set([1, 5, 1, 1, 2]))) == False)
    assert(hasTriplicate(list("Axolotls")) == False)
    assert(hasTriplicate(list("mushroom soup")) == True)
    assert(hasTriplicate(list("Bumfuzzle Cattywampus Gardyloo")) == True)
    #-------------------------------------------
    assert(hasTriplicate([ 1, 2, 3, 1, 1 ]) == True)
    assert(hasTriplicate(list("boo")) == False)
    assert(hasTriplicate(list("booo")) == True)
    print('Passed! (pending O() check)')

def testBoxesAnInteger():
    print('Testing boxesAnInteger()...', end='')
    assert(boxesAnInteger([ 2.3, 9.4, 1.7 ]) == True)
    assert(boxesAnInteger([ 2.3, 9.4, 0.7 ]) == False)
    assert(boxesAnInteger([ 2.0, 9.4, 1.7 ]) == False)
    assert(boxesAnInteger([ ]) == False)
    assert(boxesAnInteger([ 15.0, 15.0 ]) == False)
    assert(boxesAnInteger([ 0.0, 2.1, 3.5, 14.8 ]) == True)
    assert(boxesAnInteger([ 2.1, 0.0, 0.9, 15.2, 13.66 ]) == False)
    #------------------------------------------------
    assert(boxesAnInteger([ 2.5, 3.5, 4.5 ]) == True)
    assert(boxesAnInteger([ 1.0, 5.0]) == False)
    assert(boxesAnInteger([ 1.9, 9.4, 2.1 ]) == True)
    print('Passed! (pending O() check)')

#################################################
# testAll and main
#################################################

def testAll():
    testHasAdjacentValues()
    testHasTriplicate()
    testBoxesAnInteger()

def main():
    cs112_f20_week10_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
