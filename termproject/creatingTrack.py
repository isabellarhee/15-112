#this is all the code that is used to generate the random track

import random

def createTrack(grid, rows, cols):
    #following derived from https://www.cs.cmu.edu/~112/notes/maze-solver.py

    directions = [(1,0), (0,1), (-1,0),(0,-1)]
    visited = set()
    targetRow = 0 #end in the top middle

        
    def findPath(row, col, depth):
        
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


#https://www.cs.cmu.edu/~112/notes/notes-2d-lists.html
def make2dList(rows, cols):
    return [ ([False] * cols) for row in range(rows) ]  