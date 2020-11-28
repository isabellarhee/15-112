#term projedct ting by Isabella Rhee

#cmu graphics from 
#http://www.cs.cmu.edu/~112/notes/notes-animations-part3.html#sidescrollerExamples
from cmu_112_graphics import *
import random
import math

#---------------------------------Start mode----------------------------------
class StartMode(Mode): 
    def appStarted(mode):
        #following picture from https://twitter.com/cmubuggy
        mode.background = mode.loadImage('buggy.png')
        mode.background = mode.scaleImage(mode.background, 5/3)

    def redrawAll(mode, canvas):
        canvas.create_image(mode.width/2, mode.height/2,\
            image=ImageTk.PhotoImage(mode.background))
        #add background music
        font = 'Impact 55'
        canvas.create_text(mode.width//2, 100, text = "CMU Buggy Racer", fill =\
           'black', font = font )
        canvas.create_text(mode.width//2, mode.height-100,\
             text = 'press any button to continue', font = 'Impact 20')
        
    def keyPressed(mode, event):
        mode.app.setActiveMode(mode.app.MenuMode)

#-----------------------other stuff--------------------------------------------

#https://www.cs.cmu.edu/~112/notes/notes-2d-lists.html
def make2dList(rows, cols):
    return [ ([False] * cols) for row in range(rows) ]   

#--------------------------Racer Class------------------------------------------
class Racer(object):
    def __init__(self, name, appwidth, appheight):
        self.name = name
        self.color = 'red'
        #self.image =
        self.xc = appwidth//2
        self.yc = appwidth//2
        self.scrollX = 0
        self.scrollY = 0
        self.angle = 0
        self.length = 30
        self.width = 10
        self.points = [(self.xc-self.width, self.yc-self.length),\
            (self.xc-self.width, self.yc+self.length),\
                (self.xc+self.width, self.yc+self.length),\
                    (self.xc+self.width, self.yc-self.length)]
        self.pictures = [f'{self.color}SideL.png', f'{self.color}TurnL.png',\
             f'{self.color}Str.png', f'{self.color}TurnR.png',\
                 f'{self.color}SideR.png']
        self.currPic = self.pictures[2]
        '''
        pic = mode.loadImage(mode.player.currPic)
        pic = mode.scaleImage(pic, 1/3)
        '''
        self.picNum = 2
        
class Opponent(Racer):
    def __init__(self, appwidth, appheight):
        super().__init__('CPU', appwidth, appheight)
        self.character = 'blue'
        #self.xc =
        #self.yc =

#--------------------------drawing the track-----------------------------------

def setTrack(grid, rows, cols): #going to make this randomly generating
    for row in range(rows):
        grid[row][10] = True

def createTrack(grid, rows, cols):
    #following derived from https://www.cs.cmu.edu/~112/notes/maze-solver.py
    #make it a little more likely to go straight ahead by adding it twice 
    #in my list
    directions = [(1,0), (0,1), (-1,0),(0,-1)]
    visited = set()
    targetRow = 0 #end in the top middle

        
    def findPath(row, col, depth):
        print(depth)
        '''
        if depth > 80:
            print('started over----------------------------------------------')
            row = rows-1
            col = cols//2
            depth = 0
            visited.clear()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) in visited:
                    grid[r][c] = 1
                else:
                    grid[r][c] = 0
        print2dList(grid)
        '''
        #base cases
        if (row, col) in visited:
            return False
        visited.add((row, col))
        if row == targetRow: return True
        #randomize directions
        random.shuffle(directions)
        for stepx, stepy in directions:
            depth += 1
            print(str(stepx) +" "+str(stepy))
            if isValid(grid, row+stepy, col+stepx, visited):
                if findPath(row+stepy, col+stepx, depth+1): return True

        visited.remove((row,col))
        return False

 
    if findPath(rows-1, cols//2, 0):
        for r,c in visited:
            grid[r][c] = True

    return grid

def isValid(grid, row, col, visited):
    rows,cols = len(grid),len(grid[0])
    if not (0 <= row < rows and 0 <= col < cols): 
        return False
    directions = [(1,0), (0,1), (-1,0),(0,-1)]
    sideCounter = 0
    #check to make sure it's not just a big blob, more of a "path"
    for drow, dcol in directions:
        if (drow+row, dcol+col) in visited:
            sideCounter += 1

    if sideCounter < 2:
        return True
    else:
        return False
#----------------------------------------------------------------------------

def maxItemLength(a):
    maxLen = 0
    rows = len(a)
    cols = len(a[0])
    for row in range(rows):
        for col in range(cols):
            maxLen = max(maxLen, len(str(a[row][col])))
    return maxLen

# Because Python prints 2d lists on one row,
# we might want to write our own function
# that prints 2d lists a bit nicer.
def print2dList(a):
    if (a == []):
        # So we don't crash accessing a[0]
        print([])
        return
    rows, cols = len(a), len(a[0])
    fieldWidth = maxItemLength(a)
    print('[')
    for row in range(rows):
        print(' [ ', end='')
        for col in range(cols):
            if (col > 0): print(', ', end='')
            print(str(a[row][col]).rjust(fieldWidth), end='')
        print(' ]')
    print(']')



#---------------------------Game Mode------------------------------------------

class GameMode(Mode):
    def appStarted(mode):
        mode.rows = 20
        mode.cols = 20
        mode.grid = make2dList(mode.rows, mode.cols)
        mode.grid = createTrack(mode.grid, mode.rows, mode.cols)
        mode.cellSize = 500

        #name = mode.getUserInput('Enter your name:')
        mode.player = Racer('name', mode.width, mode.height)
        mode.friction = 1
        mode.topSpeed = 25
        mode.racers = []
        mode.racers.append(mode.player)
        mode.offsetX = -1*(mode.cellSize*(mode.cols//2))
        mode.offsetY = -1*(mode.cellSize*(mode.rows-1))
        #mode.direction = 'Up'

    def keyPressed(mode, event):
        if event.key == 'm':
            mode.app.setActiveMode(mode.app.MenuMode)
            mode.appStarted()
        elif event.key in ['Right', 'Left', 'Up', 'Down']:
            mode.moveRacer(event.key)

    def moveRacer(mode, direction):
        if direction == 'Right':
            if not mode.playerOnTrack():
                mode.player.scrollX = 0
            elif mode.player.scrollX <= mode.topSpeed:
                mode.player.scrollX += 5
            if mode.player.angle <= 30:
                mode.player.angle += 10
                mode.turnRacer(mode.player)
        elif direction == 'Left':
            if not mode.playerOnTrack():
                mode.player.scrollX = 0
            elif mode.player.scrollX >= -1*mode.topSpeed:
                mode.player.scrollX -= 5
            if mode.player.angle >= -30: 
                mode.player.angle -= 10
                mode.turnRacer(mode.player)
        elif direction == 'Up':
            if not mode.playerOnTrack():
                mode.player.scrollY = 0
            elif mode.player.scrollY >= -1*mode.topSpeed:
                mode.player.scrollY -= 5
        elif direction == 'Down':
            if not mode.playerOnTrack():
                mode.player.scrollY = 0
            elif  mode.player.scrollY <= mode.topSpeed:
                mode.player.scrollY += 5

    def playerOnTrack(mode):
        row, col = mode.getCell(mode.player.xc,mode.player.yc)
        if mode.grid[row][col] == True:
            return True
        
        return False

#-------------------------------------------------------------------------
#derived from https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html
    def getCell(mode, x, y):
        # aka "viewToModel"
        # return (row, col) in which (x, y) occurred or (-1, -1) if outside grid
        #if (not mode.pointInGrid(x, y)):
            #return (-1, -1)

        row = int((y - mode.offsetY) / mode.cellSize) 
        col = int((x - mode.offsetX) / mode.cellSize)

        return row, col

    def pointInGrid(mode, x, y):
    # return True if (x, y) is inside the grid defined by app.
        return ((-1*mode.offsetX<= x <=(mode.cols*mode.cellSize)-mode.offsetX)\
         and (-1*mode.offsetY<= y <=(mode.rows*mode.cellSize)-mode.offsetY))

#--------------------------------------------------------------------------

#https://stackoverflow.com/questions/36620766/rotating-a-square-on-tkinter-canvas
    def rotateRacer(mode, points, angle, center):
        angle = math.radians(angle)
        cos_val = math.cos(angle)
        sin_val = math.sin(angle)
        cx, cy = center
        new_points = []
        for x_old, y_old in points:
            x_old -= cx
            y_old -= cy
            x_new = x_old * cos_val - y_old * sin_val
            y_new = x_old * sin_val + y_old * cos_val
            new_points.append([x_new + cx, y_new + cy])
        return new_points

    def turnRacer(mode, player):
        center = (player.xc, player.yc)
        player.points = \
            mode.rotateRacer(player.points, player.angle, center)

    def updateRacer(mode, player):
        mode.offsetX -= player.scrollX
        mode.offsetY -= player.scrollY

    def drawCell(mode, canvas, row, col, color):
        x0 = (mode.cellSize * col) + mode.offsetX
        y0 = (mode.cellSize * row)  + mode.offsetY
        x1 = x0 + mode.cellSize
        y1= y0 + mode.cellSize
        x0 -= mode.player.scrollX
        x1 -= mode.player.scrollX
        y0 -= mode.player.scrollY
        y1 -= mode.player.scrollY
        canvas.create_rectangle(x0, y0, x1, y1, fill= color, outline='black', \
                width = 1)    

    def drawPlayer(mode, canvas):
        #canvas.create_polygon(mode.player.points, fill='red')
        canvas.create_image(mode.player.xc, mode.player.yc,\
            image = ImageTk.PhotoImage(mode.player.currPic))
        canvas.create_text(mode.player.xc, mode.player.yc-15,\
            text=mode.player.name)

    def drawTrack(mode, canvas):
        #setTrack(mode.grid, mode.rows, mode.cols)
        for r in range(mode.rows):
            for c in range(mode.cols):
                if mode.grid[r][c] == True:
                    color = 'plum'
                else:
                    color = 'white'
                mode.drawCell(canvas, r, c, color)

    def redrawAll(mode, canvas):
        canvas.create_text(mode.width/2, 10,\
            text ="press ctrl-p to pause, m for main menu", font = 'Arial 12')
        mode.drawTrack(canvas)
        mode.drawPlayer(canvas)
    
    def timerFired(mode):
        mode.updateRacer(mode.player)
        #slowing down the thingy
        
        if mode.player.scrollX > 0:
            mode.player.scrollX -= mode.friction
        elif mode.player.scrollX < 0:
            mode.player.scrollX += mode.friction
        
        if mode.player.scrollY > 0:
            mode.player.scrollY -= mode.friction
        elif mode.player.scrollY < 0:
            mode.player.scrollY += mode.friction

        
#-----------------------------Menu Mode----------------------------------------

class MenuMode(Mode):
    def appStarted(mode):
        buttons = []
        #following picture from https://www.cmu.edu/brand/brand-guidelines/visual-identity/colors.html
        mode.background = mode.loadImage('tartan.png')
        mode.background = mode.scaleImage(mode.background, 5/3)

    def redrawAll(mode, canvas):
        canvas.create_image(mode.width/2, mode.height/2,\
            image=ImageTk.PhotoImage(mode.background))
        font = 'Impact 50'
        canvas.create_text(mode.width/2, 100, text='Main Menu',fill = 'red',\
            font=font)
        mode.drawButtons(canvas)

    def drawButtons(mode, canvas):
        #start game button
        font = 'Arial 24 bold'
        canvas.create_rectangle(mode.width/2-100, 250, mode.width/2+100, 280, \
            fill = 'red')
        canvas.create_text(mode.width/2, 260, text = 'Start game', font=font)
        #pick character button
        canvas.create_rectangle(mode.width/2-100, 300, mode.width/2+100, 330, \
            fill = 'red')
        canvas.create_text(mode.width/2, 310, text = 'pick character',\
             font = font)
        #other buttons

    def mousePressed(mode, event):
        #clicked start
        cx = mode.width/2
        if ((cx-100 <= event.x <= cx+100) and\
            (265-10 <= event.y <= 265+10)):
            mode.app.setActiveMode(mode.app.GameMode)
        elif ((cx-100 <= event.x <= cx+100) and\
            (315-10 <= event.y <= 315+10)):
            mode.app.setActiveMode(mode.app.PickPlayerMode)

#-----------------------Pick Player Mode--------------------------------------
    
class PickPlayerMode(Mode):

    def redrawAll(mode, canvas):
        canvas.create_rectangle(10, 10, 60, 40, fill = 'red')
        canvas.create_text(35, 25, text = 'back', font = 'Arial 12')
        
    def mousePressed(mode, event):
        if ((10 <= event.x <= 60) and\
            (10 <= event.y <= 40)):
            mode.app.setActiveMode(mode.app.MenuMode)

#----------------------------app setup-----------------------------------------
class MyModalApp(ModalApp):
    def appStarted(app):
        app.StartMode = StartMode()
        app.GameMode = GameMode()
        app.MenuMode = MenuMode()
        app.PickPlayerMode = PickPlayerMode()
        app.setActiveMode(app.StartMode)
        app.timerDelay = 50

app = MyModalApp(width=800, height=800)
