# wordSearch1.py

def wordSearch(board, word):
    (rows, cols) = (len(board), len(board[0]))
    for row in range(rows):
        for col in range(cols):
            result = wordSearchFromCell(board, word, row, col)
            if (result != None):
                return result
    return None

def wordSearchFromCell(board, word, startRow, startCol):
    for drow in [-1, 0, +1]:
        for dcol in [-1, 0, +1]:
            if ((drow != 0) or (dcol != 0)):
                result = wordSearchFromCellInDirection(board, word,
                                                       startRow, startCol,
                                                       drow, dcol)
                if (result != None):
                    return result
    return None

def wordSearchFromCellInDirection(board, word, startRow, startCol, drow, dcol):
    (rows, cols) = (len(board), len(board[0]))
    dirNames = [ ["up-left"  ,   "up", "up-right"],
                 ["left"     ,   ""  , "right"   ],
                 ["down-left", "down", "down-right" ] ]
    for i in range(len(word)):
        row = startRow + i*drow
        col = startCol + i*dcol
        if ((row < 0) or (row >= rows) or
            (col < 0) or (col >= cols) or
            (board[row][col] != word[i])):
            return None
    return (word, (startRow, startCol), dirNames[drow+1][dcol+1])

def testWordSearch():
    board = [ [ 'd', 'o', 'g' ],
              [ 't', 'a', 'c' ],
              [ 'o', 'a', 't' ],
              [ 'u', 'r', 'k' ],
            ]
    print(wordSearch(board, "dog")) # ('dog', (0, 0), 'right')
    print(wordSearch(board, "cat")) # ('cat', (1, 2), 'left')
    print(wordSearch(board, "tad")) # ('tad', (2, 2), 'up-left')
    print(wordSearch(board, "cow")) # None

testWordSearch()
testWordSearchWithWildcardsAndWraparound()

def testWordSearchWithWildcardsAndWraparound():
    print('Testing wordSearchWithWildcardsAndWraparound()...', end='')
    board = [ [ 'd', 'o', 'g' ],
              [ 't', 'a', 'c' ],
              [ '?', 'r', 't' ],
              [ 'u', 'r', 'k' ],
            ]
    assert(wordSearch(board, "dog") == ('dog', (0, 0), 'right'))
    assert(wordSearch(board, "roar") == ('roar', (3, 1), 'down'))
    assert(wordSearch(board, "rug") == ('rug', (2, 1), 'down-left'))

    #Wildcards should still work!
    assert(wordSearch(board, "tort") == ('tort', (2, 2), 'right')) 
    assert(wordSearch(board, "rat") == ('rat', (2, 1), 'left'))
    
    #Note: Your function *may* return one of two different (but still correct) answers!
    #      One is not obvious, and counts the second letter as 'o' in (0, 1). 
    #      Adding (-1,-1) for 'up-left' then puts us at (-1, 0) which should
    #      wrap around to the 'u' at (3, 0). Which does your code return?
    assert((wordSearch(board, "c?u") == ('c?u', (1, 2), 'up-left'))
            or (wordSearch(board, "c?u") == ('c?u', (1, 2), 'down-left')))
    
    assert(wordSearch(board, "tur?") == None) #Can't use two wildcards though!
    assert(wordSearch(board, "cow") == None)