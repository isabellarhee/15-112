#Isabella Rhee and Laura Canseco

from cmu_112_graphics import *
import random

def appStarted(app):
    app.rows = 10
    app.cols = 10
    app.margin = 5 # margin around grid
    app.timerDelay = 250
    app.creativeMode = False 
    initSnakeAndFoodAndPoison(app)
    app.waitingForFirstKeyPress = True
    app.score = 0
    

def initSnakeAndFoodAndPoison(app):
    app.snake = [(0,0)]
    app.direction = (0, +1) # (drow, dcol)
    placeFood(app)
    if app.creativeMode: 
        placePoison(app)
    app.gameOver = False

# getCellBounds from grid-demo.py
def getCellBounds(app, row, col):
    # aka 'modelToView'
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    topMargin = 30
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    x0 = app.margin + gridWidth * col / app.cols
    x1 = app.margin + gridWidth * (col+1) / app.cols
    y0 = topMargin + gridHeight * row / app.rows
    y1 = topMargin + gridHeight * (row+1) / app.rows
    return (x0, y0, x1, y1)

def keyPressed(app, event):
    if (app.waitingForFirstKeyPress):
        app.waitingForFirstKeyPress = False
    elif (event.key == 'r'):
        initSnakeAndFoodAndPoison(app)
    elif app.gameOver:
        return
    elif (event.key == 'Up'):      app.direction = (-1, 0)
    elif (event.key == 'Down'):  app.direction = (+1, 0)
    elif (event.key == 'Left'):  app.direction = (0, -1)
    elif (event.key == 'Right'): app.direction = (0, +1)
    elif (event.key.isdigit()): 
        app.creativeMode = True 
    # elif (event.key == 's'):
        # this was only here for debugging, before we turned on the timer
        # takeStep(app)

def timerFired(app):
    if app.gameOver or app.waitingForFirstKeyPress: return
    takeStep(app)

def takeStep(app):
    (drow, dcol) = app.direction
    (headRow, headCol) = app.snake[0]
    (newRow, newCol) = (headRow+drow, headCol+dcol)
    if app.creativeMode: 
        if ((newRow < 0)):
            app.snake.insert(0, (app.rows - 1, newCol))
            app.snake.pop()
        elif (newRow >= app.rows):  
            app.snake.insert(0, (0, newCol))
            app.snake.pop()
        elif (newCol < 0): 
            app.snake.insert(0, (newRow, app.cols - 1))
            app.snake.pop()
        elif (newCol >= app.cols): 
            app.snake.insert(0, (newRow, 0))
            app.snake.pop()
        elif ((newRow, newCol) in app.snake):
            app.gameOver = True
        else:
            app.snake.insert(0, (newRow, newCol))
            if (app.foodPosition == (newRow, newCol)):
                placeFood(app)
                app.score += 1
            elif (app.poisonPosition == (newRow, newCol)): 
                app.gameOver = True
            else:
                # didn't eat, so remove old tail (slither forward)
                app.snake.pop()
    else: 
        if ((newRow < 0) or (newRow >= app.rows) or
        (newCol < 0) or (newCol >= app.cols) or
        ((newRow, newCol) in app.snake)):
            app.gameOver = True
        else:
            app.snake.insert(0, (newRow, newCol))
            if (app.foodPosition == (newRow, newCol)):
                placeFood(app)
            else:
                # didn't eat, so remove old tail (slither forward)
                app.snake.pop()


def placeFood(app):
    # Keep trying random positions until we find one that is not in
    # the snake. Note: there are more sophisticated ways to do this.
    while True:
        row = random.randint(0, app.rows-1)
        col = random.randint(0, app.cols-1)
        if (row,col) not in app.snake:
            app.foodPosition = (row, col)
            return

def placePoison(app): 
    while True: 
        row = random.randint(0, app.rows-1)
        col = random.randint(0, app.cols-1)
        if (row,col) not in app.snake and app.foodPosition:
            app.poisonPosition = (row, col)
            return


def drawScore(app, canvas):
    canvas.create_text(app.width/2, 15, text = f"Score: {app.score}", 
                                        font = 'Arial 20 bold')

def drawBoard(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = getCellBounds(app, row, col)
            canvas.create_rectangle(x0, y0, x1, y1, fill='white')

def drawSnake(app, canvas):
    for (row, col) in app.snake:
        color = 'blue'
        if (row, col) == app.snake[0]:
            color = 'pink'
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        canvas.create_oval(x0, y0, x1, y1, fill=color)

def drawFood(app, canvas):
    if (app.foodPosition != None):
        (row, col) = app.foodPosition
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        canvas.create_oval(x0, y0, x1, y1, fill='green')

def drawPoison(app, canvas): 
    if (app.poisonPosition != None): 
        (row, col) = app.poisonPosition
        (x0, y0, x1, y1) = getCellBounds(app, row, col)
        canvas.create_oval(x0, y0, x1, y1, fill='red')

def drawGameOver(app, canvas):
    if (app.gameOver):
        canvas.create_text(app.width/2, app.height/2, text='Game over!',
                           font='Arial 26 bold')
        canvas.create_text(app.width/2, app.height/2+40,
                           text='Press r to restart!',
                           font='Arial 26 bold')

def redrawAll(app, canvas):
    if (app.waitingForFirstKeyPress):
        canvas.create_text(app.width/2, app.height/2,
                    text='Welcome to Super Snake', font='Arial 26 bold')
        canvas.create_text(app.width/2, app.height/2 + 30 ,
                           text='Press any key to start!',
                           font= 'Arial 26')
    else:
        drawBoard(app, canvas)
        drawSnake(app, canvas)
        drawFood(app, canvas)
        drawGameOver(app, canvas)
        drawScore(app, canvas) 
        drawPoison(app, canvas)

runApp(width=400, height=430)