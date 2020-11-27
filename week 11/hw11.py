#################################################
# hw11.py
#
# Your name: Isabella Rhee
# Your andrew id: irhee
# section 1G0
#################################################

import cs112_f20_week11_linter
import math, copy, os

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
def alternatingSum(L):
    '''
    wrapper function to send the List and depth (starting at 0)
    '''
    return altSumRec(L, 0)

def altSumRec(L, depth):
    '''
    recursively gets alternating sum/difference of the ints in list L
    '''
    if len(L) == 0: #if list is empty return 0
        return 0

    first = L[0]
    rest = L[1:]

    if depth % 2 == 0: 
        return first + altSumRec(rest, depth+1) #alternates +/-
    else:
        return (-1 * first) + altSumRec(rest, depth+1)

def onlyEvenDigits(L):
    '''
    returns list of the nums in L but only their odd digits
    '''
    evenList = []
    if len(L) == 0:
        return L

    currentNum = onlyEvens(L[0], 0) #get new number for first element in L
    rest = L[1:]
    evenList.append(currentNum)  #add new value t
    evenList += onlyEvenDigits(rest) #add current list contents

    return evenList

def onlyEvens(n, depth):
    '''
    takes number returns only even digits in it
    '''
    if n == 0:  #at this point we went through all the digits
        return 0

    lastDig = n % 10
    rest = n // 10

    if lastDig % 2 == 0:   #if even
        return onlyEvens(rest, depth+1) + (lastDig*(10**depth)) #keep the digit
    else:
        return onlyEvens(rest, depth)  #move on to next digit

def powersOf3ToN(n):
    '''
    takes float or int n, returns list of powers of 3 up to and including n
    start at 1 and check if each sequential power is <= n i guess
    '''
    return powersOf3ToNHelper(n, 1)
    
def powersOf3ToNHelper(n, powersOf3):
    '''
    takes n and a power of 3 and returns a list of all powers of 3 up to
    and including n starting w powersOf3
    '''
    powersOf3List = []
    if powersOf3 == n:
        return [powersOf3]
    elif powersOf3 < n:  #if the power of 3 less than n
        powersOf3List.append(powersOf3)  #add to end of list
        powersOf3List += powersOf3ToNHelper(n, powersOf3*3) #check for next
                                                    #power of 3

    return powersOf3List

def findLargestFile(path):
    '''
    takes a string path to a folder and returns the full path to the largest 
    file in terms of bytes in the folder (and all its subfolders)
    '''
    bestPath, bestSize = findLargestFileAndSize(path)
    
    return bestPath #I think 

def findLargestFileAndSize(path):
    # Returns (bestPath, bestSize) starting from this path, which could
    # be to either a folder or a file
    if os.path.isfile(path):
        return path, os.path.getsize(path)
    else: 
        files = os.listdir(path)
        findLargestFileAndSizeInDir(path, files)

    #return bestPath, bestSize

def findLargestFileAndSizeInDir(path, files):
    # This assumes that path is to a folder, and it returns
    # (bestPath, bestSize) for all the files/folders in this folder.
    # The second parameter, files, is a list of files in this folder,
    # as returned by os.listdir().
    if len(files) == 0: #somewhere in here compare the file to see 
        return path, os.path.getsize(path)  #  if it's the biggest one
    else:
        firstFile = files[0] 
        rest = files[1:]
        findLargestFileAndSizeInDir(firstFile,rest)

#################################################
# Test Functions
#################################################

def testAlternatingSum():
    print('Testing alternatingSum()...', end='')
    assert(alternatingSum([1,2,3,4,5]) == 1-2+3-4+5)
    assert(alternatingSum([ ]) == 0)
    print('Passed!')

def testOnlyEvenDigits():
    print('Testing onlyEvenDigits()...', end='')
    assert(onlyEvenDigits([43, 23265, 17, 58344]) == [4, 226, 0, 844])
    assert(onlyEvenDigits([ ]) == [ ])
    print('Passed!')

def testPowersOf3ToN():
    print('Testing powersOf3ToN()...', end='')
    assert(powersOf3ToN(10.5) == [1, 3, 9])
    assert(powersOf3ToN(27) == [1, 3, 9, 27])
    assert(powersOf3ToN(26.999) == [1, 3, 9])
    assert(powersOf3ToN(-1) == [ ])
    print('Passed!')

def testFindLargestFile():
  
    print('Testing findLargestFile()...', end='')
    assert(findLargestFile('sampleFiles/folderA') ==
                           'sampleFiles/folderA/folderC/giftwrap.txt')
    assert(findLargestFile('sampleFiles/folderB') ==
                           'sampleFiles/folderB/folderH/driving.txt')
    assert(findLargestFile('sampleFiles/folderB/folderF') == '')
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    testAlternatingSum()
    testOnlyEvenDigits()
    testPowersOf3ToN()
    testFindLargestFile()

def main():
    cs112_f20_week11_linter.lint()
    testAll()

if (__name__ == '__main__'):
    main()
