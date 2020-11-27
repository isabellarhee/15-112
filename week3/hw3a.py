#################################################
# hw3a.py
#
# Your name: Isabella Rhee
# Your andrew id: irhee
# section 1 G0
#################################################

import cs112_f20_week3_linter
import string, copy, random

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
# hw3a-standard
#################################################

#     resubmitted to insert comment code
# resubmitted part 2 to finish writing test cases lol
# resubmitted part 3 to add a helper function

def vowelCount(s):
    '''
    for loop through s char by char, checking if it's a vowel
    '''
    
    s = s.lower()
    vowels = 0  #counter
    for c in range(0, len(s)):
        if (s[c] =="a" or s[c] =="e" or s[c] =="i" or s[c]=="o" or s[c] =="u"):
            vowels += 1

    return vowels

def checkIndex(index):
    '''
    takes the index from applyCaesarCipher and checks 
    if it is greater than the length of the alphabet string
    then subtracts the two values to get the new index
    '''
    if (index > len(string.ascii_uppercase)-1):
        index = index - len(string.ascii_uppercase)
    return index


def applyCaesarCipher(message, shift):
    '''
    shifting each letter in a message shift number of times, 
    if goes past z, it wraps around back to the front of alphabet
    '''
    let = len(message)  #number of letters
    newMessage = ""
    
    for x in range(0, let):
        currLet = message[x]  #current letter

        if currLet.isdigit(): 
            return message
        
        if currLet == " ":
            tempChar = " "     
        elif currLet.isupper():
            tempIndex = (string.ascii_uppercase.index(currLet)) + shift
            tempIndex = checkIndex(tempIndex) #see checkIndex
            tempChar = string.ascii_uppercase[tempIndex] #sets the new character
        else:
            tempIndex = (string.ascii_lowercase.index(currLet)) + shift
            tempIndex = checkIndex(tempIndex)
            tempChar = string.ascii_lowercase[tempIndex]
        
        newMessage += tempChar
    return newMessage

def rotateStringLeft(s, n):
    '''
    If n is positive the letters rotate left, if negative rotates right
    '''
    newS = ""  #new string
    moveStr = ""  #part of the string that is being moved

    if (n == 0):  #doesn't rotate at all
        return s
    elif (n > 0):  #left
        if( n> len(s)):
            n%=len(s)
        moveStr = s[:n]
        newS = s[n:] + moveStr
    else:    #right
        n = abs(n)
        if(n>len(s)):
            n%=len(s)
        moveStr = s[len(s)-n:]
        newS = moveStr+ s[:len(s)-n]
    
    return newS

def isRotation(s, t):
    '''
    loops # of times of characters and calls the 
    rotateStringLeft to check if its the same as 
    string t
    '''
    charS = len(s)  #number of characters in each string
    charT = len(t)
    if (charS != charT): #cant be diff lengths
        return False
    elif (s == t):
        return False
    else:
        for x in range(1, charS):
            if rotateStringLeft(s, x) == t:
                return True
        return False


#################################################
# hw3a-spicy
#################################################

def encodeRightLeftRouteCipher(text, rows):
    return 42

def decodeRightLeftRouteCipher(cipher):
    return 42

def getEvalSteps(expr):
    return 42

#################################################
# Test Functions
#################################################

def testVowelCount():
    print('Testing vowelCount()...', end='')
    assert(vowelCount('abcdefg') == 2)
    assert(vowelCount('ABCDEFG') == 2)
    assert(vowelCount('') == 0)
    assert(vowelCount('This is a test.  12345.') == 4)
    assert(vowelCount(string.ascii_lowercase) == 5)
    assert(vowelCount(string.ascii_lowercase*100) == 500)
    assert(vowelCount(string.ascii_uppercase) == 5)
    assert(vowelCount(string.punctuation) == 0)
    assert(vowelCount(string.whitespace) == 0)
#--------------------------------------------------
    assert(vowelCount('Hello World') == 3)
    assert(vowelCount('13') == 0)
    assert(vowelCount('isabellarhee')==6)
    assert(vowelCount('aeiou') == 5)
    assert(vowelCount("     e") == 1)
    print('Passed!')

def testApplyCaesarCipher():
    print('Testing applyCaesarCipher()...', end='')
    assert(applyCaesarCipher('abcdefghijklmnopqrstuvwxyz', 3) ==
                             'defghijklmnopqrstuvwxyzabc')
    assert(applyCaesarCipher('We Attack At Dawn', 1) == 'Xf Buubdl Bu Ebxo')
    assert(applyCaesarCipher('1234', 6) == '1234')
    assert(applyCaesarCipher('abcdefghijklmnopqrstuvwxyz', 25) ==
                             'zabcdefghijklmnopqrstuvwxy')
    assert(applyCaesarCipher('We Attack At Dawn', 2)  == 'Yg Cvvcem Cv Fcyp')
    assert(applyCaesarCipher('We Attack At Dawn', 4)  == 'Ai Exxego Ex Hear')
    assert(applyCaesarCipher('We Attack At Dawn', -1) == 'Vd Zsszbj Zs Czvm')
    # And now, the whole point...
    assert(applyCaesarCipher(applyCaesarCipher('This is Great', 25), -25)
           == 'This is Great')
    #-----------------------------------------------------------------
    assert(applyCaesarCipher('Isabella', 1) == 'Jtbcfmmb')
    assert(applyCaesarCipher('Hello World', -1) == "Gdkkn Vnqkc")
    assert(applyCaesarCipher('bop', 0) == 'bop')
    print('Passed.')

def testRotateStringLeft():
    print('Testing rotateStringLeft()...', end='')
    assert(rotateStringLeft('abcde', 0) == 'abcde')
    assert(rotateStringLeft('abcde', 1) == 'bcdea')
    assert(rotateStringLeft('abcde', 2) == 'cdeab')
    assert(rotateStringLeft('abcde', 3) == 'deabc')
    assert(rotateStringLeft('abcde', 4) == 'eabcd')
    assert(rotateStringLeft('abcde', 5) == 'abcde')
    assert(rotateStringLeft('abcde', 25) == 'abcde')
    assert(rotateStringLeft('abcde', 28) == 'deabc')
    assert(rotateStringLeft('abcde', -1) == 'eabcd')
    assert(rotateStringLeft('abcde', -24) == 'bcdea')
    assert(rotateStringLeft('abcde', -25) == 'abcde')
    assert(rotateStringLeft('abcde', -26) == 'eabcd')
    #------------------------------------------------------
    assert(rotateStringLeft('hello', 2) == 'llohe')
    assert(rotateStringLeft('kosbie', -1)== 'ekosbi')
    assert(rotateStringLeft('ono',3) == "ono")
    print('Passed!')

def testIsRotation():
    print('Testing isRotation()...', end='')
    assert(isRotation('a', 'a') == False) # a string is not a rotation of itself
    assert(isRotation('', '') == False) # a string is not a rotation of itself
    assert(isRotation('ab', 'ba') == True)
    assert(isRotation('abcd', 'dabc') == True)
    assert(isRotation('abcd', 'cdab') == True)
    assert(isRotation('abcd', 'bcda') == True)
    assert(isRotation('abcd', 'abcd') == False)
    assert(isRotation('abcd', 'bcd') == False)
    assert(isRotation('abcd', 'bcdx') == False)
    #---------------------------------------------------
    assert(isRotation('kosbie', 'ekosbi') == True)
    assert(isRotation('isabella', 'bellaisa') == True)
    assert(isRotation('hello', 'world') == False)
    print('Passed!')

def testEncodeRightLeftRouteCipher():
    print('Testing encodeRightLeftRouteCipher()...', end='')
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",4) ==
                                      "4WTAWNTAEACDzyAKT")
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",3) ==
                                      "3WTCTWNDKTEAAAAz") 
    assert(encodeRightLeftRouteCipher("WEATTACKATDAWN",5) ==
                                      "5WADACEAKWNATTTz") 
    #
    print('Passed!')

def testDecodeRightLeftRouteCipher():
    print('Testing decodeRightLeftRouteCipher()...', end='')
    assert(decodeRightLeftRouteCipher("4WTAWNTAEACDzyAKT") ==
                                      "WEATTACKATDAWN")
    assert(decodeRightLeftRouteCipher("3WTCTWNDKTEAAAAz") ==
                                      "WEATTACKATDAWN") 
    assert(decodeRightLeftRouteCipher("5WADACEAKWNATTTz") ==
                                      "WEATTACKATDAWN") 
    text = "WEATTACKATDAWN"
    cipher = encodeRightLeftRouteCipher(text, 6)
    plaintext = decodeRightLeftRouteCipher(cipher)
    assert(plaintext == text)
    print('Passed!')

def testEncodeAndDecodeRightLeftRouteCipher():
    testEncodeRightLeftRouteCipher()
    testDecodeRightLeftRouteCipher()

def testGetEvalSteps():
    print("Testing getEvalSteps()...", end="")
    assert(getEvalSteps("0") == "0 = 0")
    assert(getEvalSteps("2") == "2 = 2")
    assert(getEvalSteps("3+2") == "3+2 = 5")
    assert(getEvalSteps("3-2") == "3-2 = 1")
    assert(getEvalSteps("3**2") == "3**2 = 9")
    assert(getEvalSteps("31%16") == "31%16 = 15")
    assert(getEvalSteps("31*16") == "31*16 = 496")
    assert(getEvalSteps("32//16") == "32//16 = 2")
    assert(getEvalSteps("2+3*4") == "2+3*4 = 2+12\n      = 14")
    assert(getEvalSteps("2*3+4") == "2*3+4 = 6+4\n      = 10")
    assert(getEvalSteps("2+3*4-8**3%3") == """\
2+3*4-8**3%3 = 2+3*4-512%3
             = 2+12-512%3
             = 2+12-2
             = 14-2
             = 12""")
    assert(getEvalSteps("2+3**4%2**4+15//3-8") == """\
2+3**4%2**4+15//3-8 = 2+81%2**4+15//3-8
                    = 2+81%16+15//3-8
                    = 2+1+15//3-8
                    = 2+1+5-8
                    = 3+5-8
                    = 8-8
                    = 0""")
    print("Passed!")

#################################################
# testAll and main
#################################################

def testAll():
    # hw3a-standard
    testVowelCount()
    testApplyCaesarCipher()
    testRotateStringLeft()
    testIsRotation()

    # hw3a-spicy
    #testEncodeAndDecodeRightLeftRouteCipher()
    #testGetEvalSteps()

def main():
    cs112_f20_week3_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
