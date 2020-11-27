#################################################
# hw4.py
#
# Your name: Isabella Rhee
# Your andrew id: irheee
#section 1G0
#################################################

import cs112_f20_week4_linter
import string
from cmu_112_graphics import *

def appStarted(app):
    '''
    Initializaes all the variables
    '''
    app.rows = 10
    app.cols = 10
    app.cW = (app.width - 10) / app.cols
    app.cH = (app.height - 40) / app.rows
    app.score = 0
    app.dotRow = 0
    app.dotCol = 0
    app.dotDir = True #goes right if True, left if False
    app.dotColor = "blue"
    app.dotR = (app.cW / 2 - 6) #radius of dot
    app.expOn = False  #if there is an active explosion
    app.expX = 0  #explosion coordinates
    app.expY = 0
    app.expR = 10 #explosion radius
    app.dotHit = False #checks to see if it makes it all the way through
                            #  to subtract -1 to score if still False
    
    app.isPaused = False

def mousePressed(app, event):
    if(not app.expOn): #only creates new explosion if there isn't one currently
        app.expX = event.x #                         active
        app.expY = event.y
        app.expOn = True

def keyPressed(app, event):
    key = event.key
    if(key in string.digits): #if it's number, makes the new grid
        if (int(key) < 4):
            sizeGrid = (int(key) + 10)
        else:
            sizeGrid = int(key)
        app.rows = sizeGrid
        app.cols = sizeGrid
        app.score = 0          #reset all the variables
        app.dotCol = 0
        app.dotRow = 0
        app.cW = (app.width - 10) / app.cols #new column and width size 
        app.cH = (app.height - 40) / app.rows # scaled to screen
        app.dotR = (app.cW / 2 - 6) 
        
    if(key == 'p'):  #pause the dot
        app.isPaused = not app.isPaused
    if(key == 's' and app.isPaused): #do one step when pressed
        doStep(app)
    
    if(key == 'r'):  #reset the game
        app.score = 0
        app.dotRow = 0
        app.dotCol = 0
        app.dotColor = 'blue'
        app.expX = 600
        

def explosionIntersectsDot(app):
    '''
    checks to see if the dots are within the two radii added together or less
    if not, it just returns and does nothing
    '''
    radii = app.dotR + app.expR #radius of dot and explosion
    x0,y0,x1,y1 = getCellBounds(app, app.dotRow, app.dotCol) #the corners of dot
    dotX = (x0 + x1)/2 #actual x,y coordinates of dot
    dotY = (y0 + y1)/2 
    if(not (abs(dotX - app.expX) <= radii and abs(dotY - app.expY) <= radii )):
        return  #if not intersecting, return do nothing

    if(app.dotColor == 'blue'): 
        app.dotColor = 'red' 
        app.expOn = False  #end explosion
        app.score += app.expR//10  #add to score
    else:
        app.dotColor = 'blue' #switches to blue if red
        app.expOn = False
        app.score += 10
 
    app.dotCol = 0  #reset dot back to top, moving right
    app.dotRow = 0
    app.dotDir = True
    app.expX = 600 #puts explosion off screen so it doesn't intersect the dot

    
def moveDot(app):  
    '''
    is called in the timerFired to move the dot one cell
    '''
    if(app.dotDir):  #if direction is to the right
        app.dotCol += 1
        if(app.dotCol >= app.cols-1 and app.dotRow >= app.rows-1):  #at the end
            app.dotRow = 0  #                              of the grid
            app.dotCol = 0  #goes back to top left
            if(app.dotHit == False):  #subtracts if never hit by explosion
                app.score -= 1
        elif (app.dotCol >= app.cols): #end of row, switch to next row
            app.dotRow += 1
            app.dotCol = app.cols-1
            app.dotDir = False #swithces direction
        
    else:  #direction to the left
        app.dotCol -= 1
        if(app.dotCol <= 0 and app.dotRow >= app.rows-1): #at end of grid
            app.dotRow = 0
            app.dotCol = 0
            app.dotDir = True #switches direction to right
            if(app.dotHit == False):
                app.score -= 1
        elif(app.dotCol < 0): #at end of the row on the left
            app.dotRow += 1
            app.dotCol = 0
            app.dotDir = True

    

def growExplosion(app): 
    '''
    adds 10 pixels until it reaches 50
    '''
    app.expR += 10
    if(app.expR > 50): #resets if it gets bigger than radius 50
        app.expX = 600 #move off screen
        app.expR = 0
        app.expOn = False
    

def timerFired(app):
    if(app.expOn == False and app.expR != 0): #if there is no active explosion
        app.expR = 10  #          reset explosion radius

    if(not app.isPaused): #if paused, nothing happens
        doStep(app)

    explosionIntersectsDot(app)

def doStep(app): 
    '''
    does one instant of both moving the dot and grow explosion
    '''
    moveDot(app)
    growExplosion(app)
   
    

def drawTitleAndScore(app, canvas):
    '''
    writes Hw4 Game! and the score at the top
    '''
    canvas.create_text(app.width/2, 20,
                       text='Hw4 Game!')
    canvas.create_text(app.width-90, 20,
                       text='Score: '+ str(app.score))

def drawGrid(app,canvas):
    '''
    TODO: draw the 10x10 grid
    '''
    for row in range(app.rows):
        for col in range(app.cols):
            x0, y0, x1, y1 = getCellBounds(app, row, col)
            canvas.create_rectangle(x0, y0, x1, y1)

def getCellBounds(app,r,c): #from recitation
    '''
    Model to View (MTV)
    TODO: return the (x0, y0, x1, y1) rectangle that draws this cill
    '''
    x0 = c * app.cW + 5  #add the margins so the grid is in the middle
    y0 = r * app.cH + 35
    x1 = x0 + app.cW
    y1 = y0 + app.cH
    return x0, y0, x1, y1

def drawDot(app, canvas):  
    '''
    draw Blue/red dot based on current location
    '''
    r = (app.cW/2) - app.dotR #to scale the dot to fit in the box
    x0,y0,x1,y1 = getCellBounds(app,app.dotRow,app.dotCol)
    canvas.create_oval(x0+r, y0+r, x1-r, y1-r, fill = app.dotColor)
    

def drawExplosion(app, canvas):
    '''
    draws orange circle based on location and current size
    '''
    if(app.expOn):  #only draws if there is an active explosion
        x0 = app.expX - app.expR
        y0 = app.expY - app.expR
        x1 = app.expX + app.expR
        y1 = app.expY + app.expR
        canvas.create_oval(x0,y0,x1,y1, fill = 'orange', width = 1)
    pass

def redrawAll(app, canvas):
    
    drawTitleAndScore(app, canvas)
    drawGrid(app, canvas)
    drawDot(app, canvas)
    drawExplosion(app, canvas)

def main():
    cs112_f20_week4_linter.lint()
    runApp(width=510, height=540)

if __name__ == '__main__':
    main()