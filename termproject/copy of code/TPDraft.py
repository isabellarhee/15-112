#term project ting by Isabella Rhee

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
        font = 'Impact 65'
        canvas.create_text(mode.width//2, 100, text = "CMU Buggy Racer", fill =\
           'black', font = font )
        canvas.create_text(mode.width//2, mode.height-100,\
             text = 'press any button to continue', font = 'Impact 25')
        
    def keyPressed(mode, event):
        mode.app.setActiveMode(mode.app.PickPlayerMode)

#-----------------------other stuff--------------------------------------------

#https://www.cs.cmu.edu/~112/notes/notes-2d-lists.html
def make2dList(rows, cols):
    return [ ([False] * cols) for row in range(rows) ]   

#--------------------------Racer Class------------------------------------------
class Racer(object):
    def __init__(self, name, appwidth, appheight, color):
        self.name = name
        self.color = color
        self.xc = appwidth//2
        self.yc = appwidth//2
        self.scrollX = 0
        self.scrollY = 0
        # I made all of the little car pictures myself using snapchat lol
        self.pictures = [f'{self.color}SideL.png', f'{self.color}TurnL.png',\
             f'{self.color}Str.png', f'{self.color}TurnR.png',\
                 f'{self.color}SideR.png']
        self.picNum = 2         
        self.currPic = self.pictures[self.picNum]
    
class Opponent(Racer):
    def __init__(self, appwidth, appheight, color):
        super().__init__('ugly', appwidth, appheight, color)
        
        self.xc = 230
        self.yc = 250
        self.offsetX = 0
        self.offsetY = 0
        self.visited = []
        self.inPastCell = False
        self.direction = 'Up'

#--------------------------drawing the track-----------------------------------

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
        if depth > 80: # this doesnt work like i want it to
            return False

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
#---------------------------drawing 2d list for debugging---------------------
# from https://www.cs.cmu.edu/~112/notes/notes-2d-lists.html#printing

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
        name = mode.app.PickPlayerMode.name
        mode.player = Racer(name, mode.width, mode.height,\
             mode.app.PickPlayerMode.chosen)
        mode.player.currPic = mode.loadImage(mode.player.currPic)
        mode.player.currPic = mode.scaleImage(mode.player.currPic, 1/2)
        mode.friction = 1
        mode.topSpeed = 30
        mode.racers = []
        mode.racers.append(mode.player)
        mode.offsetX = -1*(mode.cellSize*(mode.cols//2))
        mode.offsetY = -1*(mode.cellSize*(mode.rows-1))
        mode.opponent = Opponent(mode.width, mode.height, 'blue')
        mode.opponent.currPic = mode.loadImage(mode.opponent.currPic)
        mode.opponent.currPic = mode.scaleImage(mode.opponent.currPic, 1/2)
        mode.opponent.direction = mode.chooseDirection()
        mode.oppTopSpeed = 8
        mode.started = False
        mode.timer = 59
        mode.timer2 = 0
        mode.goal = (-1, -1)
        for c in range(mode.cols):
            if mode.grid[0][c] == True:
                mode.goal = (0, c) #for the AI
        mode.winner = 'No One rn'

    def keyPressed(mode, event):
        if event.key == 'm':
            mode.app.setActiveMode(mode.app.MenuMode)
            mode.appStarted()
        elif event.key in ['Right', 'Left', 'Up', 'Down'] and mode.started:
            mode.moveRacer(event.key, mode.player)

#------------------------------racer stuff-------------------------------------

    def moveRacer(mode, direction, player):
        if direction == 'Right':
            if not mode.playerOnTrack(player.xc, player.yc):
                if mode.playerOnTrack(player.xc + 30, player.yc):
                    player.scrollX = 0
                    mode.offsetX -= 5
                else:
                    player.scrollX = 0
            elif player.scrollX <= mode.topSpeed:
                player.scrollX += 5     
        elif direction == 'Left':
            if not mode.playerOnTrack(player.xc, player.yc):
                if mode.playerOnTrack(player.xc - 30, player.yc):
                    player.scrollX = 0
                    mode.offsetX += 5
                else:
                    player.scrollX = 0
            elif player.scrollX >= -1*mode.topSpeed:
                player.scrollX -= 5
        elif direction == 'Up':
            if not mode.playerOnTrack(player.xc, player.yc):
                if mode.playerOnTrack(player.xc, player.yc - 30):
                    player.scrollY = 0
                    mode.offsetY += 5
                else:
                    player.scrollY = 0
            elif player.scrollY >= -1*mode.topSpeed:
                player.scrollY -= 5
        elif direction == 'Down':
            if not mode.playerOnTrack(player.xc, player.yc):
                if mode.playerOnTrack(player.xc, player.yc + 30):
                    player.scrollY = 0
                    mode.offsetY -= 5
                else:
                    player.scrollY = 0
            elif player.scrollY <= mode.topSpeed:
                player.scrollY += 5

        mode.turnRacer(player, direction)

    def playerOnTrack(mode, x, y):
        #check if player is within bounds of track
        row, col = mode.getCell(x, y)
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

    def getCellCoordinates(mode, row, col):
        #remember offsetx and offsety are negative numbers
        x0 = (col * mode.cellSize) + mode.offsetX
        y1 = (row * mode.cellSize) + mode.offsetY
        x = x0 + int(.5*mode.cellSize)
        y = y1 + int(.5*mode.cellSize)
        return x, y

#--------------------------------------------------------------------------
    def turnRacer(mode, player, direction):
        #update which picture is being drawn based on direction
        if direction == 'Right':
            if player.picNum < 4:
                player.picNum += 1
        elif direction == 'Left':
            if player.picNum > 0:
                player.picNum -= 1
        elif direction == 'Up':  
            if player.picNum < 2:
                player.picNum += 1
            elif player.picNum > 2:
                player.picNum -= 1
        elif direction == 'Down':
            if player.picNum < 4 and player.picNum > 2:
                player.picNum += 1
            elif player.picNum > 0 and player.picNum <= 2:
                player.picNum -= 1

    def updateRacer(mode, player):
        mode.offsetX -= player.scrollX
        mode.offsetY -= player.scrollY
        player.currPic = mode.loadImage(player.pictures[player.picNum])
        player.currPic = mode.scaleImage(player.currPic, 1/2)

    def updateOpponent(mode, opponent): #TO DO idk
        opponent.offsetX -= mode.player.scrollX
        opponent.offsetY -= mode.player.scrollY
        
        print("opponent x: " + str(opponent.xc) + "opponent y: " \
            + str(opponent.yc))
        opponent.currPic = mode.loadImage(opponent.pictures[opponent.picNum])
        opponent.currPic = mode.scaleImage(opponent.currPic, 1/2)

    def chooseDirection(mode):
        #change scrollx and scrolly of opponent
        o = mode.opponent #so i dont have to keep typing it
        #get the current cell
        row, col = mode.getCell(o.xc, o.yc)
        print(row, col)
        if (row, col) not in o.visited:
            o.visited.append((row, col))
        dirx = 0
        diry = 0

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dy, dx in directions:
            if (0 <= row+dx < mode.rows) and (0 <= col+dy < mode.cols): 
                print("yay")
                if not (row+dx, col+dy) in o.visited\
                     and mode.grid[row+dx][col+dy]:
                    dirx, diry = dy, dx #idk why these r swtiched it makes no sense but it works
                    print(dx, dy)
                    break

        if dirx < 0:
            direction = 'Left'
        elif dirx > 0:
            direction = 'Right'
        elif diry < 0:
            direction = 'Up'
        else:
            direction = 'Down'
  
        print(direction)
        print('turning')
        return direction

    def inMiddleOfCell(mode):
        o = mode.opponent
        row, col = mode.getCell(o.xc, o.yc)
        midx, midy = mode.getCellCoordinates(row, col)
        x0 = midx-5
        y0 = midy-5
        x1 = midx+5
        y1 = midy+5
            #use this to check if the car is *close* to the middle of the box
            #aka if the coordinates of the center are within this 8x8 box 
            #which is in the middle of the cell


        if (o.direction == 'Left' or o.direction == 'Right') and \
             x0 <= o.xc <= x1:
             print('middle')
             return True
        elif (o.direction == 'Up' or o.direction == 'Down') and \
            y0 <= o.yc <= y1:
            print('middlee')
            return True
        else:
            return False


    def moveOpponent(mode):
        direction = mode.opponent.direction
        scrollX = 0
        scrollY = 0

        if direction == 'Right':
            scrollX = 7
            scrollY = 0
        elif direction == 'Left':
            scrollX = -7
            scrollY = 0
        elif direction == 'Up':
            scrollX = 0
            scrollY = -7
        else:
            scrollX = 0
            scrollY = 7

        print('moving')
        return scrollX, scrollY

    def atFinish(mode, player):
        row, col = mode.getCell(player.xc, player.yc)
        if (row, col) == mode.goal:
            return True
        else:
            return False

    #-----------------------Drawing Stuff--------------------------------

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

    def drawPlayer(mode, canvas, player):
        canvas.create_image(player.xc, player.yc,\
            image = ImageTk.PhotoImage(player.currPic))
        canvas.create_text(player.xc, player.yc-40,\
            text=player.name)
    
    def drawOpponent(mode, canvas, opponent):
        canvas.create_image(opponent.xc + opponent.offsetX,\
             opponent.yc+opponent.offsetY,\
                 image = ImageTk.PhotoImage(opponent.currPic))
        canvas.create_text(opponent.xc + opponent.offsetX,\
             opponent.yc-40 + opponent.offsetY,\
            text=opponent.name)

    def drawTrack(mode, canvas):
        #setTrack(mode.grid, mode.rows, mode.cols)
        for r in range(mode.rows):
            for c in range(mode.cols):
                if mode.grid[r][c] == True:
                    color = 'white'
                else:
                    color = 'black'
                mode.drawCell(canvas, r, c, color)

    def drawTimer(mode, canvas):
        font = 'Impact 45'
        if mode.timer <= 15:
            canvas.create_text(mode.width//2, 25,\
                text = 'GO!', font = font)
        else:
            canvas.create_text(mode.width//2, 100,\
                text = f'{int(mode.timer // 15)}', font = font)

    def redrawAll(mode, canvas):
        mode.drawTrack(canvas)
        canvas.create_text(mode.width-100, 10,\
            text ="press ctrl-p to pause, m for main menu", font = 'Arial 12')
        mode.drawPlayer(canvas, mode.player)
        mode.drawOpponent(canvas, mode.opponent)
        mode.drawTimer(canvas)
    
    def timerFired(mode):
        if not mode.started:
            mode.timer -= 1.5
            if mode.timer <= 0:
                mode.started = True
                mode.player.xc, mode.player.yc
        else:
            #AI opponent shit
            '''
            mode.timer2 += 1
            if int(mode.timer // 7) == (mode.timer // 7):
            '''
            if mode.inMiddleOfCell(): #turn if in the middle of a cell
                mode.opponent.direction = mode.chooseDirection()
              #otherwise move in the direction it was going
            mode.opponent.scrollX, mode.opponent.scrollY = mode.moveOpponent()
                
            mode.opponent.xc += mode.opponent.scrollX
            mode.opponent.yc += mode.opponent.scrollY
            mode.turnRacer(mode.opponent, mode.opponent.direction)

            #slowing down the thingy
            for car in [mode.player, mode.opponent]:
                if mode.atFinish(car):
                    mode.winner = car.name
                    mode.app.setActiveMode(mode.app.GameOver)
                    

                if mode.playerOnTrack(car.xc, car.yc):
                    if car == mode.player:
                        mode.updateRacer(car)
                    else:
                        mode.updateOpponent(car)

                    if car.scrollX > 0:
                        car.scrollX -= mode.friction
                    elif car.scrollX < 0:
                        car.scrollX += mode.friction
                    
                    if car.scrollY > 0:
                        car.scrollY -= mode.friction
                    elif car.scrollY < 0:
                        car.scrollY += mode.friction

       
#-----------------------------Menu Mode----------------------------------------

class MenuMode(Mode):

    def appStarted(mode):
        #following picture from https://www.cmu.edu/brand/brand-guidelines/visual-identity/colors.html
        mode.background = mode.loadImage('tartan.png')
        mode.background = mode.scaleImage(mode.background, 5/3)

    def redrawAll(mode, canvas):
        canvas.create_image(mode.width/2, mode.height/2,\
            image=ImageTk.PhotoImage(mode.background))
        font = 'Impact 80'
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
    def appStarted(mode):
        
        mode.pictures = ['redStr.png' , 'blueStr.png', 'greenStr.png', \
            'yellowStr.png']
        mode.redpic = mode.loadImage(mode.pictures[0])
        mode.redpic = mode.scaleImage(mode.redpic, 3/5)
        mode.bluepic = mode.loadImage(mode.pictures[1])
        mode.bluepic = mode.scaleImage(mode.bluepic, 3/5)
        mode.greenpic = mode.loadImage(mode.pictures[2])
        mode.greenpic = mode.scaleImage(mode.greenpic, 3/5)
        mode.yellowpic = mode.loadImage(mode.pictures[3])
        mode.yellowpic = mode.scaleImage(mode.yellowpic, 3/5)
        mode.chosen = 'red'
        mode.name = mode.getUserInput('Enter your name:')
    def redrawAll(mode, canvas):
        canvas.create_text(mode.width//2, 50, text = 'Choose your racer color',\
            font = 'Impact 45')

        canvas.create_text(mode.width//2, 700,\
             text = f'Current color: {mode.chosen}', font = 'Impact 30')

        #back button
        canvas.create_rectangle(10, 10, 60, 40, fill = 'red')
        canvas.create_text(35, 25, text = 'Menu', font = 'Arial 12')

        #color choices
        #red
        canvas.create_rectangle(50, 300, 150, 500, fill = 'white', width = 0)
        canvas.create_image(100, 400,image=ImageTk.PhotoImage(mode.redpic))

        #blue
        canvas.create_rectangle(250, 300, 350, 500, fill = 'white', width = 0)
        canvas.create_image(300, 385,image=ImageTk.PhotoImage(mode.bluepic))

        #green
        canvas.create_rectangle(450, 300, 550, 500, fill = 'white', width = 0)
        canvas.create_image(500, 385,image=ImageTk.PhotoImage(mode.greenpic))

        #yellow
        canvas.create_rectangle(650, 300, 750, 500, fill = 'white', width = 0)
        canvas.create_image(700, 400,image=ImageTk.PhotoImage(mode.yellowpic))
     
    def mousePressed(mode, event):
        if ((10 <= event.x <= 60) and\
            (10 <= event.y <= 40)):
            mode.app.setActiveMode(mode.app.MenuMode)
        elif ((50 <= event.x <= 150) and (300 <= event.y <= 500)):
            mode.chosen = 'red'
        elif ((250 <= event.x <= 350) and (300 <= event.y <= 500)):
            mode.chosen = 'blue'
        elif ((450 <= event.x <= 550) and (300 <= event.y <= 500)):
            mode.chosen = 'green'
        elif ((650 <= event.x <= 750) and (300 <= event.y <= 500)):
            mode.chosen = 'yellow'
        else:
            mode.chosen = 'red'

#----------------------------Game Over Mode-------------------------------------

class GameOver(Mode):
    def appStarted(mode):
        mode.winner = mode.app.GameMode.winner

    def drawButtons(mode, canvas):
        #back to menu
        font = 'Impact 30'
        canvas.create_rectangle(mode.width/2-200, 250, mode.width/2+200, 350, \
            fill = 'red')
        canvas.create_text(mode.width/2, 300, text = 'Main Menu', font=font)
        #exit game
        canvas.create_rectangle(mode.width/2-200, 450, mode.width/2+200, 550, \
            fill = 'red')
        canvas.create_text(mode.width/2, 500, text = 'Exit Game',\
             font = font)

    def redrawAll(mode, canvas):
        canvas.create_rectangle(0, 0, mode.width, mode.height, fill = 'black')
        canvas.create_text(mode.width/2, 100, text='Game Over', fill = 'red',\
            font = 'Impact 24')
        canvas.create_text(mode.width/2, 150, text=f'Winner: {mode.winner}',\
            fill = 'red', font = 'Impact 24')
        mode.drawButtons(canvas)

    def mousePressed(mode, event):
        #clicked start
        cx = mode.width/2
        if ((cx-200 <= event.x <= cx+200) and\
            (250 <= event.y <= 350)):
            mode.app.setActiveMode(mode.app.MenuMode)
        elif ((cx-200 <= event.x <= cx+200) and\
            (450 <= event.y <= 550)):
            sys.exit()

#----------------------------app setup-----------------------------------------
class MyModalApp(ModalApp):
    def appStarted(app):
        app.StartMode = StartMode()
        app.GameMode = GameMode()
        app.MenuMode = MenuMode()
        app.PickPlayerMode = PickPlayerMode()
        app.GameOver = GameOver()
        app.setActiveMode(app.StartMode)
        app.timerDelay = 50

app = MyModalApp(width=800, height=800)
