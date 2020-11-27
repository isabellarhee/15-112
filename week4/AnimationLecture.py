from cmu_112_graphics import *

def appStarted(app):
    app.cx = app.width/2
    app.cy = app.height/2
    app.r = 40

def keyPressed(app, event):
    if (event.key == 'Left'):
        app.cx -= 10
    elif (event.key == 'Right'):
        app.cx += 10

def redrawAll(app, canvas):
    canvas.create_text(app.width/2, 20,
                       text='Move dot with left and right arrows')
    canvas.create_oval(app.cx-app.r, app.cy-app.r,
                       app.cx+app.r, app.cy+app.r,
                       fill='darkGreen')

runApp(width=400, height=400)



#recitation notes------------------------------
'''
Kerry the cube
components:
Model:
- number of rows -> appStarted
- number of cols -> appStarted
- width of each cell
- height of each cell

Control:

View:
- drawing the grid

'''

def appStarted(app):
    '''
    TODO: Initialize all the variables relating to the grid
    '''
    app.rows = 8
    app.cols = 12
    app.cW = app.width / app.cols
    app.cH = app.height /app.rows

    app.kerryRow = 0
    app.kerryCol = 0
    app.kerryColor = "Blue"
    app.tomatoRow = random.randint(0, app.rows-1)
    app.tomatoCol = random.randint(0. app.cols-1)
    app.tomatoesEaten = 0
    app.gameOver = False

def getCell(app,x,y):
    '''
    View to Model (VTM)
    TODO: Return the (row,col) that this pixel is inside of
    '''
    c = int(x / app.cW)
    r = int(y/app.cH)
    return r,c

def getCellBounds(app,r,c):
    '''
    Model to View (MTV)
    TODO: return the (x0, y0, x1, y1) rectangle that draws this cill
    '''
    x0 = c * app.cW
    y0 = r * app.cH
    x1 = x0 + app.cW
    y2 = y0 + app.cH
    return x0, y0, x1, y1

def drawGrid(app,canvas):
    '''
    TODO: draw the 8x12 grid
    '''
    for row in range(app.rows):
        for col in range(app.cols):
            x0, y0, x1, y1 = getCellBounds(app,row,col)
            canvas.create_rectangle(x0,y0,x1,y1)

def redrawAll(app,canvas):
    drawGrid(app,canvas)


#    drawing Kerry
'''
Model:
-What row/col Kerry is in

Control:
-moving Kerry when keys are pressed w/o going out of bounds

View:
-drawing Kerry

'''
def moveKerry(app,drow,dcol):
    #TODO more kerry in direction (drow,dcol) without going out of bounds
    app.kerryRow += drow
    app.kerryCol += dcol
    if (app.kerryRow < 0 or app.kerryCol < 0 or 
        app.kerryCol >= app.cols or app.kerryRow >= app.rows)
        app.kerryRow -= drow
        app.kerryCol -= dcol

def keyPressed(app,event):
    #TODO move kerry when presing up/down/l/r buttons
    if (app.gameOver): return

    if (event.key == 'Up'): moveKerry(app, -1, 0)
    if (event.key == 'Down'): moveKerry(app, 1, 0)
    if (event.key == 'Left'): moveKerry(app, 0, -1)
    if (event.key == 'Right'): moveKerry(app, 0, 1)

    if (app.kerryRow == app.tomatoRow and app.kerryCol == app.tomatoCol):
        app.tomatoesEaten +=1
        if( app.tomatoesEaten == 10):
            app.gameOver = True
            app.kerryColor = "green"
        else:
            app.tomatoRow = random.randint(0, app.rows-1)
            app.tomatoCol = random.randint(0, app.cols-1)



def drawKerry(app,canvas):
    #todo draw kerry as blue rect in correct spot
    x0, y0, x1, y1 = getCellBounds(app, app.kerryRow, app.kerryCol)
    canvas.create_rectangle(x0,y0,x1,y1, fill=app.kerryColor)
    canvas.create_text(x0 + app.cW/2, y0 + app.cH/2, text = str(app.tomatoesEaten), fill = "white")


def drawTomato(app,canvas):
    x0,y0,x1,y1 = getCellBounds(app, app.tomatoRow, app.tomatoCol)


def mousePressed(app,event):
    if(app.gameOver):
        row,col = getCell(app, event.x, event.y)
        if(row == app.kerryRow and col == app.kerryCol):
            appStarted(app)

# enemy ------------------
'''
Model:
-where is the enemy
-what direction
control:
-move enemy periodically
-reverse enemy direction
-check if 

view:
-draw it

'''

def timerFired(app):
    #app.enemyCol += app.enemyDir
    # if app.enemyCol == 0 or app.enemyCol == app.Cols-1
    #   app.enemyDir += -1
    #copy tomato code to check if collide with Kerry
    # app.tomatoesEaten = 0


runApp(width=600, height=500)

'''
def keyPressed(app, event):
    app.message = f"event.key == '{event.key}'"

def redrawAll(app, canvas):
    canvas.create_text(app.width/2, 40, text=app.message, font='Arial 30 bold')
    
    keyNamesText = '''Here are the legal event.key names:
                      * Keyboard key labels (letters, digits, punctuation)
                      * Arrow directions ('Up', 'Down', 'Left', 'Right')
                      * Whitespace ('Space', 'Enter', 'Tab', 'Backspace')
                      * Other commands ('Delete', 'Escape')'''

    y = 80
    for line in keyNamesText.splitlines():
        canvas.create_text(app.width/2, y, text=line.strip(), font='Arial 20')
        y += 30


MOVING A DOT WITH ARROWS

def appStarted(app):
    app.cx = app.width/2
    app.cy = app.height/2
    app.r = 40

def keyPressed(app, event):
    if (event.key == 'Left'):
        app.cx -= 10
    elif (event.key == 'Right'):
        app.cx += 10

def redrawAll(app, canvas):
    canvas.create_text(app.width/2, 20,
                       text='Move dot with left and right arrows')
    canvas.create_oval(app.cx-app.r, app.cy-app.r,
                       app.cx+app.r, app.cy+app.r,
                       fill='darkGreen')

---do not change the model in the view (redrawAll ) part
'''


#--------recitation--------------
#grid based animation