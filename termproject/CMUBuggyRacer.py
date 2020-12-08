 #term project ting by Isabella Rhee

#game inspired by Nintendo's Mario Kart
#cmu graphics from 
#http://www.cs.cmu.edu/~112/notes/notes-animations-part3.html#sidescrollerExamples
from cmu_112_graphics import *
import random
import math
import playsound
from creatingTrack import *
from cellStuff import *
from racerStuff import *

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
        
        self.xc = 220
        self.yc = 250
        self.offsetX = 0
        self.offsetY = 0
        self.visited = []
        self.inPastCell = False
        self.direction = 'Up'
        

#---------------------------Game Mode------------------------------------------

class GameMode(Mode):
    
    def modeActivated(mode):
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
        mode.topSpeed = 18
        mode.racers = []
        mode.racers.append(mode.player)
        mode.offsetX = -1*(mode.cellSize*(mode.cols//2))
        mode.offsetY = -1*(mode.cellSize*(mode.rows-1))
        mode.opponent = Opponent(mode.width, mode.height, 'blue')
        mode.opponent.currPic = mode.loadImage(mode.opponent.currPic)
        mode.opponent.currPic = mode.scaleImage(mode.opponent.currPic, 1/2)
        mode.opponent.direction = chooseDirection(mode)
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
            moveRacer(mode, event.key, mode.player)

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
             opponent.yc + opponent.offsetY,\
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

        for c in range(mode.cols):
            if mode.grid[0][c] == True:
                x,y = getCellCoordinates(mode, 0, c)
                canvas.create_text(x, y, text='Finish!!', font='Impact 45')

    def drawTimer(mode, canvas):
        font = 'Impact 45'
        if mode.timer <= 15:
            canvas.create_text(mode.width//2, 25,\
                text = 'GO!', font = font)
        else:
            canvas.create_text(mode.width//2, 100,\
                text = f'{int(mode.timer // 15)}', font = font)

    def redrawAll(mode, canvas):
        x = -1*(mode.cellSize*(mode.cols//2)) - 100
        y = -1*(mode.cellSize*(mode.rows-1)) - 100
        x0 = ((mode.cellSize*mode.cols) - x) + 100
        y0 = ((mode.cellSize*mode.rows - y)) + 100

        canvas.create_rectangle(x, y, x0, y0, fill = 'black')
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
            
            if inMiddleOfCell(mode): #turn if in the middle of a cell
                mode.opponent.direction = chooseDirection(mode) 
                turnRacer(mode, mode.opponent, mode.opponent.direction)
              #otherwise move in the direction it was going

            mode.opponent.scrollX, mode.opponent.scrollY = moveOpponent(mode)
            mode.opponent.xc += mode.opponent.scrollX 
            mode.opponent.yc += mode.opponent.scrollY

            #if at the last celll
            if atFinish(mode, mode.opponent):
                mode.winner = mode.opponent.name
                mode.app.MenuMode.losses += 1
                mode.app.setActiveMode(mode.app.GameOver)
            elif atFinish(mode, mode.player):
                mode.winner = mode.player.name
                mode.app.MenuMode.wins += 1
                mode.app.setActiveMode(mode.app.GameOver)
            
            for car in [mode.player, mode.opponent]:
                    
                if playerOnTrack(mode, car.xc, car.yc):
                    if car == mode.player:
                        updateRacer(mode, car)
                    else:
                        updateOpponent(mode, car)
                   #slowing down the thingy
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
        mode.wins = 0
        mode.losses = 0

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
        #instructions button
        canvas.create_rectangle(mode.width/2-100, 350, mode.width/2+100, 380,\
            fill = 'red')
        canvas.create_text(mode.width/2, 365, text = 'instructions',\
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

        elif ((cx-100 <= event.x <= cx+100) and\
            (350 <= event.y <= 380)):
            mode.app.setActiveMode(mode.app.InstructionMode)

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

#----------------------------Instruction Mode-----------------------------------

class InstructionMode(Mode):
    def appStarted(mode):
        #following picture from https://www.cmu.edu/brand/brand-guidelines/visual-identity/colors.html
        mode.background = mode.loadImage('tartan.png')
        mode.background = mode.scaleImage(mode.background, 5/3)

    def redrawAll(mode, canvas):
        x0 = mode.width//2
        y0 = mode.height//2
        font = 'Impact 16'
        text = 'Instructions: Race your buggy against the AI opponent using' 
        text1 = '\n the arrow keys. First one to the finish is the winner!'

        canvas.create_image(mode.width/2, mode.height/2,\
            image=ImageTk.PhotoImage(mode.background))
        canvas.create_rectangle(x0-250, y0-100, x0+250, y0+100, fill='white')
        canvas.create_text(x0, y0, text = text + text1, fill = 'black', font = font)
        #back button
        canvas.create_rectangle(10, 10, 60, 40, fill = 'red')
        canvas.create_text(35, 25, text = 'Menu', font = 'Arial 12')

    def mousePressed(mode, event):
        if ((10 <= event.x <= 60) and\
            (10 <= event.y <= 40)):
            mode.app.setActiveMode(mode.app.MenuMode)

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
        canvas.create_text(mode.width/2, 180, text =f'{mode.winner}\'s  wins:'+\
        str(mode.app.MenuMode.wins) + "  loses: " +str(mode.app.MenuMode.losses)\
            , fill = 'red', font = 'Impact 20')
        mode.drawButtons(canvas)

    def mousePressed(mode, event):
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
        #music from Nintendo's Mario Kart 'Coconut Mall'
        #https://downloads.khinsider.com/game-soundtracks/album/mario-kart-7/Wii%2520-%2520Coconut%2520Mall.mp3
        playsound.playsound('CoconutMall.mp3', False)
        app.StartMode = StartMode()
        app.GameMode = GameMode()
        app.MenuMode = MenuMode()
        app.PickPlayerMode = PickPlayerMode()
        app.InstructionMode = InstructionMode()
        app.GameOver = GameOver()
        app.setActiveMode(app.StartMode)
        app.timerDelay = 50

app = MyModalApp(width=800, height=800)
