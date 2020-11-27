#collab12
#Isabella Rhee

def hasConsecutiveDigits(n):
    #we did this as a group but I wasnt sure if i needed to write it down
    if n < 0:
        return hasConsecutiveDigits(abs(n))
    #base case
    if n < 10:
        return False
    else: #recursive case
        lastDigit = n % 10
        secondToLastDigit = (n//10) % 10
        if lastDigit == secondToLastDigit:
            return True
        else:
            return hasConsecutiveDigits(n // 10)

def wordCounter(path, word):
    wordList = wordCounterHelper(path, word).split()
    countWords = countWords(wordList, word, 0)
    return countWords

def wordCounterHelper(path, word):
    if os.path.isfile(path):
        return [path]
    else:
        files = os.listdir(path)
        return wordCounterHelper(files)  #idk

def countWords(wordList, word, count):
    if wordList == []:
        return 0
    else:
        if wordList[0] == word:
            return countWords(wordList[1:], word, count+1)
        else:
            return countWords(wordList[1:], word, count)

def increasingPath(board):
    if findPath(board, 0, 0):
        return True
    return False
    
def findPath(board, row, col) 
    if row == len(board) - 1 and col == len(board[0]) - 1:
        return True
    moves = [(1, 0) , (0, 1), (-1, 0), (0, -1)]
    for drow, dcol in moves:
            if isValid(board, row, col, drow, dcol):
                row += drow
                col += dcol
                findPath(board, row, col)

    #like if it looks in all directions and cant find a valid move go back
    #but idk how to do that
    findPath(board, previousRow, previousCol)
    #return False somewhere

def isValid(board, row, col, drow, dcol):
    newR = row+drow
    newC = col+dcol
    if newR >= len(board) or newC >= len(board[0]) or newR < 0 or newC < 0 or \
            board[newR][newC] <= board[row][col]:
        return False
    else:
        return True

def testWordCounter():
    print("Testing wordCounter...", end="")
    assert(wordCounter("Files", "class") == 5)
    assert(wordCounter("Files", "recursion") == 1)
    assert(wordCounter("Files", "case") == 3)
    assert(wordCounter("Files", "kosbie") == 0)
    assert(wordCounter("Files", "fox") == 1)
    assert(wordCounter("Files", "the") == 25)
    assert(wordCounter("Files", "a") == 20)
    assert(wordCounter("Files", "time") == 4)
    assert(wordCounter("Files", "lorem") == 4)
    assert(wordCounter("Files", "and") == 19)
    assert(wordCounter("Files", "style") == 5)
    assert(wordCounter("Files", "solve") == 2)
    print("Passed!")

def testHasConsecutiveDigits():
  print("Beginning hasConsecutiveDigits test cases...")
  assert(hasConsecutiveDigits(1123) == True)
  assert(hasConsecutiveDigits(-1123) == True)
  assert(hasConsecutiveDigits(1234) == False)
  assert(hasConsecutiveDigits(0) == False)
  assert(hasConsecutiveDigits(1233) == True)
  print("Passed!")



def testAll():
    testHasConsecutiveDigits()
    testWordCounter()


def main():
    testAll()