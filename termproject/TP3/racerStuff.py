# this file is dedicated to functions dealing with moving the racer and the opponent
from cellStuff import *

def moveRacer(mode, direction, player):
    if direction == 'Right':
        if not playerOnTrack(mode, player.xc, player.yc):
            if playerOnTrack(mode, player.xc + 30, player.yc):
                player.scrollX = 0
                mode.offsetX -= 5
            else:
                player.scrollX = 0
        elif player.scrollX <= mode.topSpeed:
            player.scrollX += 5     
    elif direction == 'Left':
        if not playerOnTrack(mode, player.xc, player.yc):
            if playerOnTrack(mode, player.xc - 30, player.yc):
                player.scrollX = 0
                mode.offsetX += 5
            else:
                player.scrollX = 0
        elif player.scrollX >= -1*mode.topSpeed:
            player.scrollX -= 5
    elif direction == 'Up':
        if not playerOnTrack(mode, player.xc, player.yc):
            if playerOnTrack(mode, player.xc, player.yc - 30):
                player.scrollY = 0
                mode.offsetY += 5
            else:
                player.scrollY = 0
        elif player.scrollY >= -1*mode.topSpeed:
            player.scrollY -= 5
    elif direction == 'Down':
        if not playerOnTrack(mode, player.xc, player.yc):
            if playerOnTrack(mode, player.xc, player.yc + 30):
                player.scrollY = 0
                mode.offsetY -= 5
            else:
                player.scrollY = 0
        elif player.scrollY <= mode.topSpeed:
            player.scrollY += 5

    turnRacer(mode, player, direction)

def playerOnTrack(mode, x, y):
    #check if player is within bounds of track
    row, col = getCell(mode, x, y)
    if mode.grid[row][col] == True:
        return True
    
    return False

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
    player.currPic = mode.loadImage(player.pictures[player.picNum])
    player.currPic = mode.scaleImage(player.currPic, 1/2)
    
def updateRacer(mode, player):
    mode.offsetX -= player.scrollX
    mode.offsetY -= player.scrollY
    mode.opponent.offsetX -= mode.player.scrollX
    mode.opponent.offsetY -= mode.player.scrollY
    
def updateOpponent(mode, opponent): #TO DO idk
    print("opponent x: " + str(opponent.xc) + "opponent y: " \
        + str(opponent.yc))
    opponent.currPic = mode.loadImage(opponent.pictures[opponent.picNum])
    opponent.currPic = mode.scaleImage(opponent.currPic, 1/2)

def chooseDirection(mode):
    #change scrollx and scrolly of opponent
    o = mode.opponent #so i dont have to keep typing it
    #get the current cell
    row, col = getCell(mode, o.xc + o.offsetX, o.yc + o.offsetY)
    print(row, col)
    if (row, col) not in o.visited:
        o.visited.append((row, col))
    dirx = 0
    diry = 0

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for dy, dx in directions:
        #if its a valid move
        if (0 <= row+dx < mode.rows) and (0 <= col+dy < mode.cols): 
            if not (row+dx, col+dy) in o.visited\
                    and mode.grid[row+dx][col+dy]:
                dirx, diry = dy, dx #idk why these r swtiched it makes no sense but it works
                break

    if dirx < 0:
        direction = 'Left'
    elif dirx > 0:
        direction = 'Right'
    elif diry < 0:
        direction = 'Up'
    else:
        direction = 'Down'

    
    return direction

def moveOpponent(mode):
    direction = mode.opponent.direction
    scrollX = 0
    scrollY = 0
    turnRacer(mode, mode.opponent, mode.opponent.direction)
    if mode.app.MenuMode.wins <= 5: #capping off the opponent speed
        factor = mode.app.MenuMode.wins
    else:
        factor = 5

    if direction == 'Right':
        scrollX = 10 + (2 * factor)
        scrollY = 0
    elif direction == 'Left':
        scrollX = -1*(10 + (2 * factor))
        scrollY = 0
    elif direction == 'Up':
        scrollX = 0
        scrollY = -1*(10 + (2 * factor))
    else:
        scrollX = 0
        scrollY = 10 + (2 * factor)

    print('moving')
    return scrollX, scrollY

def atFinish(mode, player):
    row, col = getCell(mode, player.xc, player.yc)
    if (row, col) == mode.goal:
        return True
    else:
        return False