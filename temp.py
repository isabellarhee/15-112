def getCellCoordinates(row = 19, col = 10):
    rows, cols = 20, 20
    cellSize = 500
    offsetX = -1*(500*(cols//2))
    offsetY = -1*(500*(rows-1))
    print(offsetX, offsetY)
    x0 = col * 500 + offsetX
    y1 = row * 500 + offsetY
    
    x = x0 + int(.5*cellSize)
    y = y1 + int(.5*cellSize)
    print(x, y)

getCellCoordinates()