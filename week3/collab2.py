import basic_graphics

# def draw(canvas, width, height):
#     canvas.create_line(width/2, 0, width/2, height)
#     canvas.create_line(0, height/2, width, height/2)

#Willa, Brandon, & Isabella  collab3

basic_graphics.run(width=800, height=600)

def drawPattern2(points, canvas, width, height):

    canvas.create_line(width/2, 0, width/2, height)
    canvas.create_line(0, height/2, width, height/2)

    intervalX = (width/2) / (points - 1)
    intervalY = (height/2) / (points - 1)
    currX1 = width/2
    currY1 = 0
    currX2 = width/2
    currY2 = height/2

    for x in range(0, points-2):
        canvas.create_line(currX1, currY1, currX2, currY2)

        currY2 = currY2 + intervalY
        currX2 = currX2 + intervalX


#drawPattern(5, canvas, 800, 600)

#--------------------------------------------------------------------------
def drawSquare(x, y, width, height):
    canvas.create_line(x,y, x+width, y)
    canvas.create_line(x,y, x, y+height)
    canvas.create_line(x+width,y,y+height, x)
    canvas.create_line(x, y+height, x+width, y)
    pass

def drawTriangle(x, y, width, height):
    canvas.create_line(x , y, x + width, height)
    canvas.create_line(x , y, x + (width/2), height)
    canvas.create_line(x+width, y, x + (width/2), height)
    pass

def drawPattern3(points, canvas, width, height):

    triangle = True
    for rows in range(0, points-1):
        for col in range (0, (width / (points-1))):
            if(triangle):
                drawTriangle(rows, col, (width/(points-1), height/ (points-1)))
            else:
                drawSquare(rows, col, (width/ (points-1), height/ (points-1))

        if (not triangle):
            triangle = True
        else:
            triangle = False

drawPattern3(4, 200,200)

#--------------------------------------------------
def drawPattern4(points, canvas, width, height):
    pass #our gorup didnt get to this