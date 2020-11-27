#################################################
# collab3.py
#
# Your name: Isabella Rhee
# Your andrew id: irhee
# Collaborators (your partners): Willa Yang and Brandon Fafata
#
#################################################

import math
from tkinter import *
import random
import basic_graphics
import cs112_f20_week3_linter

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def rgbString(red, green, blue):
     return f'#{red:02x}{green:02x}{blue:02x}'

#################################################
# Functions for you to write
#################################################

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


    drawPattern(5, canvas, 800, 600)
   

#--------------------drawPattern3---------------------------
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


def drawFancyWheel(canvas, cx, cy, r, n, color):
    graphics.draw_oval(x-r, y-r, x + r, y +r)
    pass  #our grou did not get to this

def drawFancyWheels(canvas, width, height, rows, cols):
    pass

###Add your custom CTs below this line!###
def customCT(s, n):
    if len(s) % 2 == 0:
        firsthalf = string[:(len(s))//2]
        secondhalf = string[len(s)//2 :]
        return secondhalf+(3+len(string) //2)*firsthalf
    else:
        for k in range(len(string)):
            modified = string(-k+412098% len(s))
            return modified


#################################################
# Test Functions
# ignore_rest (tell autograder to ignore everything below here)
#################################################

def runDrawPattern2(points, width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # non-resizable
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawPattern2(points, canvas, width, height)
    root.mainloop()
    print("bye!")

def runDrawPattern3(points, width=300, height=300):
    root = Tk()
    root.resizable(width=False, height=False) # non-resizable
    canvas = Canvas(root, width=width, height=height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    drawPattern3(points, canvas, width, height)
    root.mainloop()
    print("bye!")


def testDrawPattern2():
    print('Testing drawPattern2()... (confirm visually)')
    print('Calling runDrawPattern2(5, 400, 400):')
    runDrawPattern2(5, 400, 400)
    print('runDrawPattern2(10, 800, 400):')
    runDrawPattern2(10, 800, 400)

def testDrawPattern3():
    print('Testing drawPattern3()... (confirm visually)')
    print('runDrawPattern3(5, 400, 400):')
    runDrawPattern3(5, 400, 400)
    print('runDrawPattern3(10, 800, 400)')
    runDrawPattern3(10, 800, 400)

def testDrawFancyWheels():
    print('Testing drawFancyWheels()... (confirm visually)')
    print('  drawFancyWheels: 1 row x 1 col, win size of 400x400...', end='')
    basic_graphics.run(1, 1, width=400, height=400, drawFn=drawFancyWheels)
    print('  drawFancyWheels: 4 rows x 6 cols, win size of 900x600...', end='')
    basic_graphics.run(4, 6, width=900, height=600, drawFn=drawFancyWheels)

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    # required
    testDrawPattern2()
    testDrawPattern3()
    testDrawFancyWheels()

def main():
    cs112_f20_week3_linter.lint()
    testAll()

if __name__ == '__main__':
    main()