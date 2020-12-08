#all  functions that have to do with cells in the grid

#derived from https://www.cs.cmu.edu/~112/notes/notes-animations-part1.html
def getCell(mode, x, y):

    row = int((y - mode.offsetY) / mode.cellSize) 
    col = int((x - mode.offsetX) / mode.cellSize)

    return row, col

def pointInGrid(mode, x, y):
    # return True if (x, y) is inside the grid defined by app.
    return ((mode.offsetX<= x <=(mode.cols*mode.cellSize)-mode.offsetX)\
        and (mode.offsetY<= y <=(mode.rows*mode.cellSize)-mode.offsetY))

def getCellCoordinates(mode, row, col):
        #remember offsetx and offsety are negative numbers
    x0 = (col * mode.cellSize) + mode.offsetX
    y1 = (row * mode.cellSize) + mode.offsetY
    x = x0 + (mode.cellSize//2)
    y = y1 + (mode.cellSize//2)

    return x, y

def inMiddleOfCell(mode):
    o = mode.opponent
    row, col = getCell(mode, o.xc + o.offsetX , o.yc + o.offsetY)
    print('middle: ' + str(row) + " " + str(col))
    midx, midy = getCellCoordinates(mode, row, col)
    x0 = midx-10
    y0 = midy-10
    x1 = midx+10
    y1 = midy+10
            #use this to check if the car is *close* to the middle of the box
            #aka if the coordinates of the center are within this 10x10 box 
            #which is in the middle of the cell


    if (o.direction == 'Left' or o.direction == 'Right') and \
        x0 <= o.xc + o.offsetX <= x1:
        print('middle')
        return True
    elif (o.direction == 'Up' or o.direction == 'Down') and \
        y0 <= o.yc + o.offsetY <= y1:
        print('middlee')
        return True
    else:
        return False