#################################################
# hw7.py: Tetris!
#
# Your name: Isabella Rhee
# Your andrew id: irhee
#
# Your partner's name: David Useche
# Your partner's andrew id: duseche
#################################################

import cs112_f20_week7_linter
import math, copy, random

from cmu_112_graphics import *

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
def gameDimensions():
    '''
    sets game dimensions 
    '''
    rows = 15
    cols = 10
    cellSize = 20 #side length
    margin = 25
    return rows, cols, cellSize, margin

def playTetris():
    '''
    sets up the app with its dimensions
    '''
    rows, cols, cellSize, margin = gameDimensions()
    width = 2 * margin + (cols * cellSize)
    height = 2 * margin + (rows * cellSize)
    runApp(width=width, height=height)

#https://www.cs.cmu.edu/~112/notes/notes-2d-lists.html
def make2dList(rows, cols, fill, app):
    '''
    creates 2d list
    '''
    return [ ([fill] * cols) for row in range(rows) ]

def appStarted(app):
    '''
    set all variables when app launched
    '''
    app.rows, app.cols, app.cellSize, app.margin = gameDimensions()
    app.emptyColor = 'blue'
    app.board = make2dList(app.rows, app.cols, app.emptyColor, app)
    app.tetrisPieces = tetrisPieces() #list of the pieces
    app.tetrisPieceColors = [ "red", "yellow", "magenta", \
                        "pink", "cyan", "green", "orange" ]
    app.fallingPiece = []
    app.fallingPieceColor = 'blue'
    app.fallingPieceRow = 0
    app.fallingPieceCol = 0
    newFallingPiece(app)
    app.isGameOver = False
    app.score = 0
    #bonus stuff
    app.paused = False
    app.bonus = False

def tetrisPieces():
    '''
    wanted to keep it more neat in the appStarted so made a helper function 
    for piece lists
    '''
    iPiece = [
        [  True,  True,  True,  True ]
    ]

    jPiece = [
        [  True, False, False ],
        [  True,  True,  True ]
    ]

    lPiece = [
        [ False, False,  True ],
        [  True,  True,  True ]
    ]

    oPiece = [
        [  True,  True ],
        [  True,  True ]
    ]

    sPiece = [
        [ False,  True,  True ],
        [  True,  True, False ]
    ]

    tPiece = [
        [ False,  True, False ],
        [  True,  True,  True ]
    ]

    zPiece = [
        [  True,  True, False ],
        [ False,  True,  True ]
    ]

    return [iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece]

def newFallingPiece(app):
    '''
    randomly chooses a piece, set its color, position at the top middle of 
    screen 
    '''
    randomIndex = random.randint(0, len(app.tetrisPieces) - 1)
    app.fallingPiece = copy.deepcopy(app.tetrisPieces[randomIndex])
    app.fallingPieceColor = app.tetrisPieceColors[randomIndex]
    app.fallingPieceRow = 0  #top row
    numFallingPieceCols = len(app.fallingPiece[0])
    app.fallingPieceCol = (app.cols//2) - (numFallingPieceCols//2) #middle col

def keyPressed(app, event):
    '''
    for any action taken on keyboard buttons
    '''
    if (not app.isGameOver and not app.paused):
        if event.key == 'k': #for testing, makes a new falling piece
            newFallingPiece(app)
        elif event.key == 'Left':  #moving the falling piece
            drow = 0
            dcol = -1
            moveFallingPiece(app, drow, dcol)
        elif event.key == 'Right':
            drow = 0
            dcol = 1
            moveFallingPiece(app, drow, dcol)
        elif event.key == 'Up':
            rotateFallingPiece(app)
        elif event.key == 'Down':
            drow = 1
            dcol = 0
            moveFallingPiece(app, drow, dcol)
        elif event.key == 'Space':  #makes it drop to the bottom
            hardDrop(app)
        elif event.key == 'b':  #bonus mode
            app.bonus = not app.bonus
        
        
    if event.key == 'p'and app.bonus:  #pause
        app.paused = not app.paused

    if event.key == 'r':  #restart game
        appStarted(app)
        
def hardDrop(app):
    '''
    piece goes straight to bottom, or as far as legal
    '''
    placed = False  #if it's at the bottom

    while not placed:
        if not moveFallingPiece(app, 1, 0): #check if it's legal move, then
            placed = True             #repeat until it's at the bottom

def moveFallingPiece(app, drow, dcol):
    '''
    move falling piece given # of cols and rows
    '''
    app.fallingPieceRow += drow
    app.fallingPieceCol += dcol
    if(not fallingPieceIsLegal(app)):  #if it is off board or hits another piece
        app.fallingPieceRow -= drow
        app.fallingPieceCol -= dcol
        return False   #if it was an illegal move
    return True   #if moved successfully
    
def fallingPieceIsLegal(app):
    '''
    loops through every cell in the falling piece and checks if it's on the 
    board, the color on the board is an empty color. returns true or false
    '''
    for r in range(len(app.fallingPiece)):  #rows
        for c in range(len(app.fallingPiece[0])):  #cols
            if app.fallingPiece[r][c]:  #if falling piece cell has True value
                fallingPiecePosR = app.fallingPieceRow+r #for actual location
                fallingPiecePosC = app.fallingPieceCol+c 
                if (fallingPiecePosR < 0 or fallingPiecePosC < 0 or \
                    fallingPiecePosR >= app.rows or \
                        fallingPiecePosC >= app.cols): #on board
                    return False
                if (not app.board[fallingPiecePosR][fallingPiecePosC] == \
                        app.emptyColor):  #checks if empty color
                    return False
    return True

def rotateFallingPiece(app):
    '''
    Stores old dimensions and the piece itself into tempvariables
    Compute the number of new rows and new columns according to old dimensions.
    make new 2d list
    loop through all cells in the original piece, 
    move each value to its new location in the new piece.
    Set fallingPiece and the other variables equal to their new values.
    Check whether the new piece is legal, else revert to old piece
    '''
    oldNumRows = len(app.fallingPiece)
    oldNumCols = len(app.fallingPiece[0])
    newNumRows = oldNumCols
    newNumCols = oldNumRows
    oldFallingPieceRow = app.fallingPieceRow
    oldFallingPieceCol = app.fallingPieceCol
    rotatedPiece = make2dList(newNumRows, newNumCols, None, app)
    oldPiece = copy.copy(app.fallingPiece)#for reverting back if not legal

    for r in range(oldNumRows): 
        for c in range(oldNumCols):
            rotatedPiece[oldNumCols-1-c][r] = app.fallingPiece[r][c]
            #map old values into new List rotatedPiece

    app.fallingPiece = rotatedPiece
    app.fallingPieceRow = oldFallingPieceRow + oldNumRows//2 - newNumRows//2
    app.fallingPieceCol = oldFallingPieceCol + oldNumCols//2 - newNumCols//2

    if (not fallingPieceIsLegal(app)): #if not legal, revert to old piece
        app.fallingPiece = oldPiece
        app.fallingPieceRow = oldFallingPieceRow
        app.fallingPieceCol = oldFallingPieceCol

def placeFallingPiece(app):
    '''
    if it reaches the bottom, sets the color as a value on the board
    '''
    for r in range(len(app.fallingPiece)):
        for c in range(len(app.fallingPiece[0])):
            if (app.fallingPiece[r][c]): #for the True values in falling piece
                app.board[app.fallingPieceRow+r][app.fallingPieceCol+c] = \
                    app.fallingPieceColor  #sets the board of that row,col
                                        #to the piece color

def removeFullRows(app):
    '''
    if a whole row has no empty color cells, removes it from the board
    and moves everything down, adds to score the square of num rows that
    were removed
    '''
    numFullRows = 0
    newBoard = copy.deepcopy(app.board)  #temp board
    for r in range(app.rows):
        if not app.emptyColor in newBoard[r]: #no empty color cells
            newBoard.pop(r) #pop whole row from the board
            newBoard.insert(0, [app.emptyColor]*app.cols) #adds new row to top
            numFullRows += 1

    app.board = copy.deepcopy(newBoard)  #copies to the real board
    app.score += numFullRows**2

def timerFired(app):
    '''
    makes stuff move incrementally
    '''
    if (not app.isGameOver and not app.paused): 
        if(not moveFallingPiece(app, +1, 0)): #if falling piece at bottom
            placeFallingPiece(app)   #places piece
            newFallingPiece(app)     #creates new falling piece
            if (not fallingPieceIsLegal(app)):  #if instantlly illegal
                app.isGameOver = True      #game is over
            removeFullRows(app)    #checks for full rows

def redrawAll(app, canvas):
    '''
    draws background color, board, falling piece, score, and message banners
    '''
    canvas.create_rectangle(0,0,app.width,app.height, fill = 'orange')
    drawBoard(app, canvas)
    drawFallingPiece(app, canvas)
    drawScore(app, canvas)

    if (app.isGameOver):   #game over banner
        canvas.create_rectangle(0, app.cellSize+app.margin,app.width,\
                (app.cellSize*3)+app.margin, fill = 'black')
        canvas.create_text(app.width//2,(app.cellSize*2)+app.margin, \
                text = 'Ayo you suck!', font = 'Arial 20 bold', fill = 'purple')
    
    if (app.paused):  #paused banner
        canvas.create_rectangle(0, app.cellSize+app.margin,app.width,\
                (app.cellSize*3)+app.margin, fill = 'magenta')
        canvas.create_text(app.width//2,(app.cellSize*2)+app.margin, \
                text = 'paused <3', font = 'Arial 20 bold', fill = 'white')

def drawScore(app, canvas):
    '''
    write the score at the top
    '''
    canvas.create_text(app.width//2, app.margin//2, \
            text = f'Score: {app.score}', font = 'Arial 14 bold', fill = 'blue')

def drawBoard(app, canvas):
    '''
    loops through rows and cols, calls drawCell for each
    '''
    for r in range(app.rows):
        for c in range(app.cols):
            drawCell(app, canvas, r, c, app.board[r][c])

def drawCell(app, canvas, row, col, color):
    '''
    draws one square at given coordinates
    '''
    x0 = (app.cellSize * col) + app.margin
    y0 = (app.cellSize * row) + app.margin
    x1 = x0 + app.cellSize
    y1= y0 + app.cellSize
    canvas.create_rectangle(x0, y0, x1, y1, fill= color, outline = 'black', \
            width = 4)

def drawFallingPiece(app, canvas):
    '''
    draws the piece with it's respective color over the board
    '''
    for r in range(len(app.fallingPiece)):
        for c in range(len(app.fallingPiece[0])):  
            if app.fallingPiece[r][c]:
                drawCell(app, canvas, r+app.fallingPieceRow, \
                c+app.fallingPieceCol, app.fallingPieceColor)

  
#################################################
# main
#################################################

def main():
    cs112_f20_week7_linter.lint()
    playTetris()

if __name__ == '__main__':
    main()
