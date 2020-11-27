#################################################
# hw6b.py
#
# Name: Isabella Rhee
# Andrew Id:  irhee
# section 1 G0
#################################################

import cs112_f20_week6_linter
import basic_graphics
import string, copy, random, math

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
# hw6b-standard
#################################################
def wordInHand(word, hand):
    '''
    takes in a word and a hand and sees if said word can be made with the hand
    '''
    hand = copy.copy(hand) #always gotta make dat copy
    index = 0
    while index < len(word):
        letter = word[index]
        if letter in hand:
            hand.pop(hand.index(letter))  #to account for repeat letters
            index += 1
        else:
            return False  #if any letter isn't in the hand it can't be a match

    return True #if it makes it through the whole word 

def wordScore(word, letterScores):
    '''
    takes a word and the list of letter scores and calculates the score of word
    '''
    score = 0
    for letter in word:
        letIndex = string.ascii_lowercase.find(letter) #corresponding index
        score += int(letterScores[letIndex])  #add value 

    return score

def bestScrabbleScore(dictionary, letterScores, hand):
    '''
    finds highest scoring word that can be made with hand given in dictionary
    returns the highest scoring word(s) and the score
    '''
    highScore = 0
    highWord = []
    for word in dictionary: #loops through given dictionary
        if wordInHand(word, hand): #if the word can be made with given hand
            if wordScore(word, letterScores) == highScore: #if it ties
                highWord.append(word)
            elif wordScore(word, letterScores) > highScore: #new best!
                highScore = wordScore(word, letterScores)
                highWord.clear()  #get rid of da old stuff
                highWord.append(word)

    if len(highWord) == 0: #if no words were found
        return None
    elif len(highWord) == 1:  #if only one word was the best
        return (highWord[0], highScore)
    else:
        return (highWord, highScore)


def isVowel(letter):
    '''
    check if the letter is a vowel :)
    '''
    vowels = 'aeiou'
    if letter in vowels:
        return True
    return False

def calculate(text):
    '''
    calculates the totals and percents to be printed in the pie chart
    '''
    vowels, cons, other, totalChars = 0, 0, 0, 0
    vowelPerc, consPerc, otherPerc = 0, 0 ,0
    text = text.lower()
    for char in text:
        if char.isalpha(): #if it's a letter
            if isVowel(char): #is vowel
                vowels += 1
            else:   #is consonant
                cons += 1
            totalChars += 1
        elif not char.isspace(): #other character but not a space
            other += 1
            totalChars += 1

    return vowels, cons, other, totalChars

def drawPieWedge(canvas, cx, cy, r, category, color, characters, total, start):
    '''
    if the char is not the total
        draw the arc based on the parameter
        calculate the angle of the text -> the (x,y) coordinates
        draw text
    else:
        draw an oval
        draw text in the center
    '''
    ex = (characters/total) * 360  #from recitation
    angle = start + (ex/2)  #angle to calculate the coordinates of
    angle = math.radians(angle)       #the text in slice
    x = cx + r/2 * math.cos(angle)
    y = cy - r/2 * math.sin(angle)

    if characters == total:  #if it's all the same type of characters
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill = color)
        canvas.create_text(cx, cy,text=f'{category} ({total} of {total}, 100%)'\
            ,font = 'Arial 12 bold')
    else:
        canvas.create_arc(cx-r, cy-r, cx+r, cy+r, start = start,\
            extent = ex, fill = color) #draws slice of the pie chart
        canvas.create_text(x, y, text=f'{category} ({characters} of {total}'+ \
            f' {round((characters / total ) * 100)}%)' \
            , font = 'Arial 12 bold')
        
    return None

def drawLetterTypePieChart(canvas, text, cx, cy, r):
    '''
    take # and % vowels, consonants and other characters in a text
    and displays it as a pie chart
    if 0, handle 0 case
    '''
    vowels, cons, other, total = calculate(text)
    canvas.create_text(cx, cy-r-20, text='Text = ' + repr(text),\
         font='Arial 18 bold')  

    start = 90  #first wedge goes to the left starting from top middle

    if (vowels == cons == other == 0): #if the string is only spaces
        canvas.create_text(cx,cy,text="No data to display",font='Arial 12 bold')
    else:
        if vowels != 0: #skips drawing if it's 0
            drawPieWedge(canvas, cx, cy, r, 'vowels', 'pink',
                vowels, total, start)
            start += (vowels/total) * 360  #extent of da vowel piece
        
        if cons != 0:  
            drawPieWedge(canvas, cx, cy, r, 'consonants', 'cyan', cons, total,
                start)
            start += (cons/total) * 360  #extent of the consonants piece

        if other != 0:
            drawPieWedge(canvas, cx, cy, r, 'other', 'green', other, total,
                start)


    

#################################################
# hw6b-bonus
#################################################

def solvesCryptarithm(puzzle, solution):
    return 42

def allSublists(L):
    yield 42

def solveSubsetSum(L):
    return 42

def heapsAlgorithmForPermutations(L):
    # from https://en.wikipedia.org/wiki/Heap%27s_algorithm
    yield 42

def solveCryptarithmWithMaxDigit(puzzle, maxDigit):
    return 42

def getAllSingletonCryptarithmsWithMaxDigit(words, maxDigit):
    return 42

#################################################
# Test Functions
#################################################

def testBestScrabbleScore():
    print("Testing bestScrabbleScore()...", end="")
    def dictionary1(): return ["a", "b", "c"]
    def letterScores1(): return [1] * 26
    def dictionary2(): return ["xyz", "zxy", "zzy", "yy", "yx", "wow"] 
    def letterScores2(): return [1+(i%5) for i in range(26)]
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("ace")) ==
                                        (["a", "c"], 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("b")) ==
                                        ("b", 1))
    assert(bestScrabbleScore(dictionary1(), letterScores1(), list("z")) ==
                                        None)
    # x = 4, y = 5, z = 1
    # ["xyz", "zxy", "zzy", "yy", "yx", "wow"]
    #    10     10     7     10    9      -
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyz")) ==
                                         (["xyz", "zxy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyzy")) ==
                                        (["xyz", "zxy", "yy"], 10))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("xyq")) ==
                                        ("yx", 9))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("yzz")) ==
                                        ("zzy", 7))
    assert(bestScrabbleScore(dictionary2(), letterScores2(), list("wxz")) ==
                                        None)
                                    
    #----------------------------------------------------------------
    def dictionary3(): return ['this','class','is','the','best', 'tec']
    def letterScores3(): return [i for i in range(1,27)]
    assert(bestScrabbleScore(dictionary3(), letterScores3(), list("hibtse")) == 
                                         ('this', 56))
    assert(bestScrabbleScore(dictionary3(), letterScores3(), list("hikoz")) ==
                                         None)
    assert(bestScrabbleScore(dictionary3(), letterScores3(), list("tices")) ==
                                         (["is", "tec"], 28))
    assert(bestScrabbleScore(dictionary3(), letterScores3(), list("class")) ==
                                         ('class', 54))

    print("Passed!")

def drawLetterTypePieCharts1(canvas, width, height):
    r = min(width,height)*0.2
    canvas.create_line(width/2, 0, width/2, height)
    canvas.create_line(0, height/2, width, height/2)
    drawLetterTypePieChart(canvas, "AB, c de!?!", width/4, height/4, r)
    drawLetterTypePieChart(canvas, "AB e", width/4, height*3/4, r)
    drawLetterTypePieChart(canvas, "A", width*3/4, height/4, r)
    drawLetterTypePieChart(canvas, "               ", width*3/4, height*3/4, r)

def drawLetterTypePieCharts2(canvas, width, height):
    rA = min(width,height)*0.15
    rB = min(width,height)*0.2
    drawLetterTypePieChart(canvas, "aLpHaBeT!", width*0.175, height*0.575, rA)
    drawLetterTypePieChart(canvas, "I ordered 2 eggs & 1 waffle for breakfast!",
                           width/2, height*0.375, rB)
    drawLetterTypePieChart(canvas, "A_E_I_O_U", width*0.825, height*0.575, rA)
    drawLetterTypePieChart(canvas, "#fbrkyz", width*0.5, height*0.8, rA)

def testDrawLetterTypePieChart():
    print('Testing drawLetterTypePieChart()...')
    basic_graphics.run(drawFn=drawLetterTypePieCharts1, width=800, height=800)
    basic_graphics.run(drawFn=drawLetterTypePieCharts2, width=800, height=800)
    print('Do a visual inspection to verify this passed!')

def testSolvesCryptarithm():
    print("Testing solvesCryptarithm()...", end="")
    assert(solvesCryptarithm("SEND + MORE = MONEY","OMY--ENDRS") == 
                                  True)
    # from http://www.cryptarithms.com/default.asp?pg=1
    assert(solvesCryptarithm("NUMBER + NUMBER = PUZZLE", "UMNZP-BLER") ==
                                  True)
    assert(solvesCryptarithm("TILES + PUZZLES = PICTURE", "UISPELCZRT") ==
                                  True)
    assert(solvesCryptarithm("COCA + COLA = OASIS", "LOS---A-CI") ==
                                  True)
    assert(solvesCryptarithm("CROSS + ROADS = DANGER", "-DOSEARGNC") ==
                                  True)

    assert(solvesCryptarithm("SEND + MORE = MONEY","OMY--ENDR-") == False)
    assert(solvesCryptarithm("SEND + MORE = MONEY","OMY-ENDRS") == False)
    assert(solvesCryptarithm("SEND + MORE = MONY","OMY--ENDRS") == False)
    assert(solvesCryptarithm("SEND + MORE = MONEY","MOY--ENDRS") == False)
    print("Passed!")

def testAllSublists():
    print('  Testing allSublists()...', end='')
    def f(): yield 42
    assert(type(allSublists([1,2,3])) == type(f())) # generator
    assert(sorted(allSublists([1])) == [ [], [1] ])
    assert(sorted(allSublists([3, 5])) == [ [], [3], [3, 5], [5] ])
    assert(sorted(allSublists([6,7,8])) == [ [], [6], [6, 7], [6, 7, 8],
                                             [6, 8], [7], [7, 8], [8] ])
    print('Passed!')

def testSolveSubsetSum():
    def checkSubsetSum(L):
        solution = solveSubsetSum(L)
        for v in solution:
            assert(solution.count(v) <= L.count(v))
        assert(sum(solution) == 0)
    print('  Testing solveSubsetSum()...', end='')
    assert(solveSubsetSum([5,2,3,-4]) == None)
    checkSubsetSum([-1,5,2,3,-4])
    checkSubsetSum([8,19,31,27,52,-70,4])
    print('Passed!')

def testHeapsAlgorithmForPermutations():
    print('  Testing heapsAlgorithmForPermutations()...', end='')
    def f(): yield 42
    assert(type(heapsAlgorithmForPermutations([1])) == type(f())) # generator
    assert(sorted(heapsAlgorithmForPermutations([1])) == [[1]])
    assert(sorted(heapsAlgorithmForPermutations([1,2])) == [
            [1,2], [2,1]
        ])
    assert(sorted(heapsAlgorithmForPermutations([3,1,2])) == [
            [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]
        ])
    print('Passed!')

def testSolveCryptarithmWithMaxDigit():
    print('  Testing solveCryptarithmWithMaxDigit()...', end='')
    assert(solveCryptarithmWithMaxDigit('RAM + RAT = ANT', 4) == '''\
RAM + RAT = ANT
120 + 123 = 243''')
    assert(solveCryptarithmWithMaxDigit('ANT + CAT = EEL', 4) == None)
    assert(solveCryptarithmWithMaxDigit('ANT + CAT = EEL', 5) == '''\
ANT + CAT = EEL
125 + 315 = 440''')
    print('Passed!')

def testGetAllSingletonCryptarithmsWithMaxDigit():
    print('  Testing getAllSingletonCryptarithmsWithMaxDigit()...', end='')
    words = ['EEL', 'RAM', 'CAT', 'BEE', 'FLY',
             'HEN', 'RAT', 'DOG', 'ANT']
    assert(getAllSingletonCryptarithmsWithMaxDigit(words, 3) == '')
    assert(getAllSingletonCryptarithmsWithMaxDigit(words, 4) == '''\
RAM + RAT = ANT
120 + 123 = 243''')
    assert(getAllSingletonCryptarithmsWithMaxDigit(words, 5) == '''\
ANT + CAT = EEL
125 + 315 = 440
ANT + CAT = HEN
105 + 315 = 420
ANT + RAT = EEL
125 + 315 = 440
ANT + RAT = HEN
105 + 315 = 420
BEE + EEL = FLY
411 + 112 = 523''')

    words = ['DEER', 'BEAR', 'GOAT', 'MULE', 'PUMA',
             'COLT', 'ORCA', 'IBEX', 'LION', 'WOLF']
    assert(getAllSingletonCryptarithmsWithMaxDigit(words, 5) == '')
    assert(getAllSingletonCryptarithmsWithMaxDigit(words, 6) == '''\
BEAR + DEER = IBEX
4203 + 1223 = 5426
COLT + GOAT = ORCA
4635 + 1605 = 6240''')
    print('Passed!')

def testBonusCombinatoricsProblems():
    print('Testing spicy combinatorics problems...')
    testAllSublists()
    testSolveSubsetSum()
    testHeapsAlgorithmForPermutations()
    testSolveCryptarithmWithMaxDigit()
    testGetAllSingletonCryptarithmsWithMaxDigit()
    print('Passed!')

#################################################
# testAll and main
#################################################

def testAll():
    # hw6b-standard
    testBestScrabbleScore()
    testDrawLetterTypePieChart()
    # hw6b-bonus
   # testSolvesCryptarithm()
    #testBonusCombinatoricsProblems()

def main():
    cs112_f20_week6_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
