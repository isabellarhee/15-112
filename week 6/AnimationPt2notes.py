#---------lecture notes----------
from cmu_112_graphics import*
import random
def appStarted(app):
    app.dotCenters = []

def mousePressed(app,event):
    app.dotCenters.append( (event.x, event.y) )

def keyPressed(app, event):
    pass

def redrawAll(app,canvas):
    r = 20
    for cx,cy in app.dotCenters:
        canvas.create_oval(cx-r,cy-r,cx+r,cy+r, fill = 'green')

runApp(width=400,height=400)

#--------snake-----------
from cmu_112_graphics import*
def appStarted(app):
    app.margin = 5
    app.rows = 10
    app.cols = 10
    resetApp(app)
    app.timerDelay = 250  #ms

def resetApp(app);
    app.snake = [ (1,1),(2,1),(3,1),(3,2) ]
    app.direction = (0, +1) #move to the right
    app.gameOver = False
    app.waitingForKey = False
    placeFood(app)

def mousePressed(app,event):
    pass

def takeStep(app):
    #take one step in app.direction
    (oldHeadRow, oldHeadCol) = app.snake[0]
    (drow, dcol) = app.direction
    newHeadRow = oldHeadRow + drow
    newHeadCol = oldHeadCol + dcol
    app.snake.insert(0,(newHeadRow, newHeadCol))

    #did we go off the board
    if(newHeadRow  < 0) or (newHeadRow >= app.rows) or (newHeadCol < 0) 
        or newHeadCol >= app.cols:
        app.gameOver = True
        app.waitingForKey = True

    #did we run into ourself?
    if ((newHeadRow, newHeadCol) in app.snake):
        app.gameOver = True
        app.waitingForKey = True

    # add new head before checking if we have to move the food
    app.snake.insert(0, (newHeadRow, newHeadCol)) #wut
    #did we eat the food
    if((newHeadRow, newHeadCol) = app.foodPosition):
        placeFood(app)
    else:
        app.snake.pop()

    #remove old tail
    app.snake.pop()

def placeFood(app):
    while True:
        row = random.randint(0,app.rows-1)
        col = random.randint(0,app.cols-1)
        if (row,col) in app.snake:
            app.foodPosition = row, col
            return
    

def timerFired

def keyPressed(app, event):

    if (app.waitingForKey):
        resetApp(app)
    elif (event.key == 't'):
        takeStep(app)
    elif (event.key == 'Down'):
        app.direction = (+1, 0)
    elif (event.key == 'Up'):
        app.direction = (-1, 0)
    elif (event.key == 'Left'):
        app.directino = (0, -1)
    elif (event.key == 'Right'):
        app.direction = (0, +1)

def drawBoard(app,canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            (x0,y0,x1,y1) = getCellBounds(app,row,col)
            canvas.create_rectangle(x0,y0,x1,y1,fill = 'white')

def drawSnake(app,canvas):
    for row,col in app.snake:
        (x0,y0,x1,y1) = getCellBounds(app,row,col)
        canvas.create_oval(x0,y0,x1,y1, fill = 'green')

def drawFood(app,canvas):
    row, col = app.foodPosition
    x0,y0,x1,y1 = getCellBound(app,row,col)
    canvas.create_oval(x0,y0,x1,y1, fill = 'purple')

def redrawAll(app,canvas):
    drawBoard(app, canvas)
    drawSnake(app, canvas)
    if app.gameOver:
        canvas.create_text(app.width/2, app.height/2, text = "Game over")

    if app.waitingForKey:
        canvas.create_text(app.width/2-20, app.height/2-20, text = "Game over")


runApp(width=400,height=400)

#--------------recitation----------------------------------------
#use basic graphics
#make everything lowercase
#helper function to draw one pie wedge
# parameters: cx, cy, r
#which category vowel = pink, consonat = cyan, other = green
#count of that category
#total # of chars
# starting angle
'''
logic
    start = starting angle in degrees
        if vowel, then 90
        if consonant then 90 +consonant extend
        if other, then 90 + vowel extent + consonant extent

    extent = how wide is the arc (not stopping angle) in degrees
        for each category, extent = (count/total) * 360
    
    drawing the text
        angle of text = start + (extend/2)
        convert to radians using math.radians()
        x = cx + r/2 * math.cos(angle)
        y = cy - r/2 * math.sin(angle)
        vowels (3 of 9, 33%)   <- format

main function:
    figure out all of parameters for each of 3 calls to piewedge
    since each of the starting angles based off previous
    handle special cases
        if # chars is 1 just draw an oval and put text at cx cy
        if # chars in a categoryis 0, dont draw arc
        if no non-whitespace just say no data to display
        .isspace()

'''

