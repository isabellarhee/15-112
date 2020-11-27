#term projedct ting by Isabella Rhee
#import pygame
#pygame.init() # wut figure out how to do this
from cmu_112_graphics import *
import random

#---------------------------------Start mode----------------------------------
class StartMode(Mode): 

    def redrawAll(mode, canvas):
        #draw an image for the title screen
        #add background music
        canvas.create_rectangle(0,0,mode.width,mode.height, fill = 'plum')
        canvas.create_text(mode.width//2, 150, text = "splashpage", fill = \
           'black' )
        
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
        self.character = 'red'
        #self.image =
        self.xc = appwidth//2
        self.xy = appwidth//2
        self.scrollX = 0
        self.scrollY = 0
        

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

#---------------------------Game Mode------------------------------------------

class GameMode(Mode):
    def appStarted(mode):
        mode.rows = 20
        mode.cols = 20
        mode.grid = make2dList(mode.rows, mode.cols)
        mode.cellSize = 20
        #name = mode.getUserInput('Enter your name:')
        mode.player = Racer('name', mode.width, mode.height)
        mode.friction = 1
        mode.topSpeed = 100

        
        
    def keyPressed(mode, event):
        if event.key == 'm':
            mode.app.setActiveMode(mode.app.MenuMode)
        elif event.key == 'Right' and mode.player.scrollX <= mode.topSpeed:
            mode.player.scrollX += 20
        elif event.key == 'Left' and abs(mode.player.scrollX) <= mode.topSpeed:
            mode.player.scrollX -= 20
        elif event.key == 'Up' and mode.player.scrollY <= mode.topSpeed:
            mode.player.scrollY -= 20
        elif event.key == 'Down' and abs(mode.player.scrollY) <= mode.topSpeed:
            mode.player.scrollY += 20

    def drawCell(mode, canvas, row, col, color):
        x0 = (mode.cellSize * col) + 200 
        y0 = (mode.cellSize * row)  + 150
        x1 = x0 + mode.cellSize
        y1= y0 + mode.cellSize
        x0 -= mode.player.scrollX
        x1 -= mode.player.scrollX
        y0 -= mode.player.scrollY
        y1 -= mode.player.scrollY
        canvas.create_rectangle(x0, y0, x1, y1, fill= color, outline='black', \
                width = 2)    

    def drawPlayer(mode, canvas):
        cx = mode.width/2
        cy = mode.width/2
        canvas.create_rectangle(cx, cy, cx+10, cy+30, fill = 'red')
        canvas.create_text(cx+5, cy-5, text = mode.player.name)

    def drawTrack(mode, canvas):
        setTrack(mode.grid, mode.rows, mode.cols)
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
    def appStarted(app):
        buttons = []

    def redrawAll(mode, canvas):
        canvas.create_rectangle(0,0,mode.width,mode.height, fill = 'honeydew')
        font = 'Arial 26 bold'
        canvas.create_text(mode.width/2, 100, text='Main Menu', font=font)
        #drawButtons(mode, canvas)

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

app = MyModalApp(width=800, height=600)
