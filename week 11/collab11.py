#Isabella Rhee and Nathan Zhu
#collab 11
# teddy problem thing


from cmu_112_graphics import *

def appStarted(app):
    app.level = 0

def rgbString(r, g, b):
    # Don't worry about the :02x part, but for the curious,
    # it says to use hex (base 16) with two digits.
    return f'#{r:02x}{g:02x}{b:02x}'

def teddyFace(app, canvas, xc, yc, r):
    teddyColor = 'firebrick3'
    canvas.create_oval(xc-r,yc-r,xc+r,yc+r, fill = teddyColor, width = r//15 )
    #snout
    snoutR = r // 2
    snoutColor = rgbString(217, 188, 126)
    canvas.create_oval(xc-snoutR,yc+10-snoutR,xc+snoutR, yc+10+snoutR, \
        fill = snoutColor, width = r//15)
    dotR = r // 5
    #nose
    canvas.create_oval(xc-dotR, yc-dotR+5, xc+dotR, yc+dotR+5, fill = 'black')
    #eyes
    canvas.create_oval(xc-r//2, yc-r//2, (xc-r//2)+dotR, \
    (yc-r//2)+dotR, fill = 'black')
    canvas.create_oval(xc+r//2, yc-r//2, (xc+r//2)+dotR, \
    (yc-r//2)+dotR, fill = 'black')

    

def drawFractal(app, canvas, level, xc, yc, r):
    if level == 0:
        teddyFace(app, canvas, xc, yc, r)
    else:
        teddyFace(app, canvas, xc, yc, r)
        drawFractal(app, canvas, level - 1, xc-r, yc-r, r//2)
        drawFractal(app, canvas, level - 1, xc+r, yc-r, r//2)

def keyPressed(app, event):
    if event.key in ['Up', 'Right'] and app.level < 6:
        app.level += 1
    elif (event.key in ['Down', 'Left']) and (app.level > 0):
        app.level -= 1

def redrawAll(app, canvas):
    margin = min(app.width, app.height)//10
    otherParams = None
    drawFractal(app, canvas, app.level, app.width//2, app.height//2, 100)
    canvas.create_text(app.width/2, 0,
                       text = f'Level {app.level} Fractal',
                       font = 'Arial ' + str(int(margin/3)) + ' bold',
                       anchor='n')
    canvas.create_text(app.width/2, margin,
                       text = 'Use arrows to change level',
                       font = 'Arial ' + str(int(margin/4)),
                       anchor='s')
    

runApp(width=400, height=400)

#-----------------Knight Tour---------------------------

def make2dList(rows, cols): #from 112 notes websit
    return [ ([0] * cols) for row in range(rows)]

def placeKnight(board, row, col, knightNumber):
    #checking bounds
    if row < 0 or row > len(board):
        return False
    elif col < 0 or row > len(board[0]):
        return False

    board[row][col] = knightNumber
    #base case
    if knightNumber >= rows*cols:
        return True

    moves = [[2,1] , [2,-1] , [-2,1] , [-2,-1]  [1,2] , [-1,2] , [1,-2],\
        [-1,-2]]

    for m in moves:
        newRow, newCol = row+m[0], col+m[1]
        if placeKnight(board, newRow, newCol, knightNumber+1):
            return True

    board[row][col] = 0
    return False

def knightsTour(n):
    board = make2dList(n, n)

    for row in range(n):
        for col in range(n):
            placeKnight(board, row, col, 1)


    return None

def print2dList(board, row, col):
    #draw da ting