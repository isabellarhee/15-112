#################################################
# hw3b.py
#
# Your name:Isabella Rhee
# Your andrew id: irhee
#section 1 G0
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
# hw3b-standard (no spicy on hw3b)
#################################################

def checkMatch(targetChar, guessChar):
    '''
    checks if 
    characters are the same and returns True
    '''
    if (targetChar == guessChar):
        return True
    return False
    

def checkPartial(target, guess):
    '''
    loops through both strings to see if any characters
    in any index are in common, returns counter
    '''
    partialCtr = 0
    isDone = False

    while(not isDone): #must loop through both until all matches found
        isDone = True
        for c in range(0, len(target)): #loops through both strings to look for
            for c2 in range(0, len(guess)): #any common characters, if so,
                
                if c > len(target)-1 or c2 > len(guess)-1:
                    break
                
                if (target[c] == guess[c2]):#removes chars from both strings and
                    partialCtr += 1        #starts the loops over :)
                    if(c == 0):
                        target = target[1:]
                    else:
                        target = target[:c] + target[c+1:]

                    if (c2 == 0):
                        guess = guess[1:]
                    else:
                        guess = guess[:c2] + guess[c2+1:]

                    isDone = False  #goes back throught the for-loops again
                    
    return partialCtr

def pickOutput(matchCtr, partialCtr):
    '''
    returns output based on the values of the counters
    '''
    partialStr = ""
    exactStr = ""
    if (matchCtr == 0 and partialCtr == 0):
        return "No matches"
    elif (matchCtr == 0 and partialCtr == 1):
        return ("%d partial match" % partialCtr)
    elif (matchCtr == 0):
        return ("%d partial matches" % partialCtr)
    elif (partialCtr == 0 and matchCtr == 1):
        return ("%d exact match" % matchCtr)
    elif (partialCtr == 0):
        return ("%d exact matches" % matchCtr)
    elif (matchCtr == 1 and partialCtr == 1):
        return("%d exact match, %d partial match" % (matchCtr, partialCtr))
    elif (matchCtr == 1):
        return ("%d exact match, %d partial matches" % (matchCtr, partialCtr))
    elif (partialCtr == 1):
        return ("%d exact matches, %d partial match" % (matchCtr, partialCtr))
    else:
        return ("%d exact matches, %d partial matches" (matchCtr, partialCtr))

def mastermindScore(target, guess):
    '''
    takes two string and checks for matching letters, 
    either in the same index, or any index (partial matches)
    then returns the number of each
    '''

    if(target == guess):
        return "You win!!!"

    matchCtr = 0
    partialCtr = 0
    isDone = False

    while(not isDone): #once you get one and remove the chars, the strings
        isDone = True     #need to be checked again from the start
        for c in range(0, len(target)):#this loop first checks for and removes 
            if (c > len(target)-1):
                break
            
            currT = target[c]  #perfect matches
            currG = guess[c]
            if checkMatch(currT, currG):  #checks if there is a perfect match
                matchCtr += 1  
                if (c == 0):
                    target = target[1:]
                    guess = guess[1:]
                else:
                    target = target[:c] + target[c+1:]  #splits both and removes
                    guess = guess[:c] + guess[c+1:]  #the matching char from 
                c -= 1                                  #both
                isDone = False  #goes back through for-loop again
            
    partialCtr = checkPartial(target, guess)
    output = pickOutput(matchCtr, partialCtr)
    return output

def playPoker(deck, players):
    return 42

#################################################
# hw3b-bonus
#################################################

def topLevelFunctionNames(code):
    return 42

def bonusEncode1(msg):
    return 42

def funDecode1(msg):
    return 42

def bonusEncode2(msg):
    return 42

def funDecode2(msg):
    return 42

def bonusEncode3(msg):
    return 42

def funDecode3(msg):
    return 42

#################################################
# Test Functions
#################################################

def testMastermindScore():
    print("Testing mastermindScore()...", end="")
    assert(mastermindScore('abcd', 'aabd') ==
                           '2 exact matches, 1 partial match')
    assert(mastermindScore('efgh', 'abef') ==
                           '2 partial matches')
    assert(mastermindScore('efgh', 'efef') ==
                           '2 exact matches')
    assert(mastermindScore('ijkl', 'mnop') ==
                           'No matches')
    assert(mastermindScore('cdef', 'cccc') ==
                           '1 exact match')
    assert(mastermindScore('cdef', 'bccc') ==
                           '1 partial match')
    assert(mastermindScore('wxyz', 'wwwx') ==
                           '1 exact match, 1 partial match')
    assert(mastermindScore('wxyz', 'wxya') ==
                           '3 exact matches')
    assert(mastermindScore('wxyz', 'awxy') ==
                           '3 partial matches')
    assert(mastermindScore('wxyz', 'wxyz') ==
                           'You win!!!')
    #----------------------------------------------------------------
    assert(mastermindScore('haji', 'lmpa') == '1 partial match')
    assert(mastermindScore('hey', 'hey') == 'You win!!!')
    assert(mastermindScore('heyo', 'helo') == '3 exact matches')
    assert(mastermindScore('hihi','ihih') == '4 partial matches')
    assert(mastermindScore('haha', 'ahah') == '4 partial matches')
    assert(mastermindScore('kosb', 'jotk') == '1 exact match, 1 partial match')
    assert(mastermindScore('hee', 'cee') == '2 exact matches')
    print("Passed!'")

def testPlayPoker():
    print('Testing playPoker()...', end='')
    assert(playPoker('QD-3S', 1) == 'Player 1 wins with a high card of QD')
    assert(playPoker('QD-QC', 1) == 'Player 1 wins with a pair to QD')
    assert(playPoker('QD-JS', 1) == 'Player 1 wins with a straight to QD')
    assert(playPoker('TD-QD', 1) == 'Player 1 wins with a flush to QD')
    assert(playPoker('QD-JD', 1) == 'Player 1 wins with a straight flush to QD')
    assert(playPoker('QD-JD', 2) == 'Not enough cards')

    assert(playPoker('AS-2H-3C-4D', 2) ==
                                    'Player 2 wins with a high card of 4D')
    assert(playPoker('5S-2H-3C-4D', 2) ==
                                    'Player 1 wins with a high card of 5S')
    assert(playPoker('AS-2H-3C-2D', 2) == 'Player 2 wins with a pair to 2H')
    assert(playPoker('3S-2H-3C-2D', 2) == 'Player 1 wins with a pair to 3S')
    assert(playPoker('AS-2H-2C-2D', 2) == 'Player 1 wins with a straight to 2C')
    assert(playPoker('AS-2H-2C-3D', 2) == 'Player 2 wins with a straight to 3D')
    assert(playPoker('AS-2H-4S-3D', 2) == 'Player 1 wins with a flush to 4S')
    assert(playPoker('AS-2H-4S-3H', 2) ==
                                    'Player 2 wins with a straight flush to 3H')
    assert(playPoker('2S-2H-3S-3H', 2) ==
                                    'Player 1 wins with a straight flush to 3S')

    assert(playPoker('AS-2D-3C-4C-5H-6D-7S-8D', 2) ==
                                    'Player 2 wins with a high card of 4C')
    assert(playPoker('AS-2D-3S-4C-5H-6D-7S-8D', 4) ==
                                    'Player 3 wins with a flush to 7S')
    print('Passed!')

def testTopLevelFunctionNames():
    print("Testing topLevelFunctionNames()...", end="")

    # no fn defined
    code = """\
# This has no functions!
# def f(): pass
print("Hello world!")
"""
    assert(topLevelFunctionNames(code) == "")

    # f is redefined
    code = """\
def f(x): return x+42
def g(x): return x+f(x)
def f(x): return x-42
"""
    assert(topLevelFunctionNames(code) == "f.g")

    # def not at start of line
    code = """\
def f(): return "def g(): pass"
"""
    assert(topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (''')
    code = """\
def f(): return '''
def g(): pass'''
"""
    assert(topLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (""")
    code = '''\
def f(): return """
def g(): pass"""
'''
    assert(topLevelFunctionNames(code) == "f")

    # triple-quote (''') in comment
    code = """\
def f(): return 42 # '''
def g(): pass # '''
"""
    assert(topLevelFunctionNames(code) == "f.g")

    # triple-quote (""") in comment
    code = '''\
def f(): return 42 # """
def g(): pass # """
'''
    assert(topLevelFunctionNames(code) == "f.g")

    # comment character (#) in quotes
    code = """\
def f(): return '#' + '''
def g(): pass # '''
def h(): return "#" + '''
def i(): pass # '''
def j(): return '''#''' + '''
def k(): pass # '''
"""
    assert(topLevelFunctionNames(code) == "f.h.j")
    print("Passed!")

def testFunDecoder(encodeFn, decodeFn):
    s1 = ''
    for c in range(15):
        if (random.random() < 0.80):
            s1 += random.choice(string.ascii_letters)
        else:
            s1 += random.choice(' \n\n') + random.choice(string.digits)
    for s in ['a', 'abc', s1]:
        if (decodeFn(encodeFn(s)) != s):
            raise Exception(f'Error in {decodeFn.__name__} on {repr(s)}')
    return True

def testFunDecoders():
    print('Testing funDecoders()...', end='')
    testFunDecoder(bonusEncode1, funDecode1)
    testFunDecoder(bonusEncode2, funDecode2)
    testFunDecoder(bonusEncode3, funDecode3)
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    # hw3b-standard
    testMastermindScore()
    #testPlayPoker()

    # hw3b-bonus
    #testTopLevelFunctionNames()
    #testFunDecoders()

def main():
    cs112_f20_week3_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
