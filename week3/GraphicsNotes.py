#Create an Empty Canvas
import basic_graphics

def draw(canvas, width, height):
    pass # replace with your drawing code!

basic_graphics.run(width=400, height=400)
#canvas coordinates - y axis grows down instead of up
#(0,0) is at the top left corner and bottom right is
#(width,height)

#Draw a Line
def draw(canvas, width, height):
    # create_line(x1, y1, x2, y2) draws a line from (x1, y1) to (x2, y2)
    canvas.create_line(25, 50, width/2, height/2)

#Draw a Rectangle with create_rectangle(left, top, right, bottom)
def draw(canvas, width, height):
    # The first four parameters are the upper-left (x,y)
    # and the lower-right (x,y) of the rectangle
    canvas.create_rectangle(0,0,150,150)
#Graphics Parameters
def draw(canvas, width, height):
    # most graphics functions allow you to use optional parameters
    # to change the appearance of the object. These are written with the code
    # paramName=paramValue
    # after the core parameters in the code

    # fill changes the internal color of the shape
    canvas.create_rectangle(  0,   0, 150, 150, fill="yellow")
    # width changes the size of the border
    canvas.create_rectangle(100,  50, 250, 100, fill="orange", width=5)
    # outline changes the color of the border
    canvas.create_rectangle( 50, 100, 150, 200, fill="green",
                                                outline="red", width=3)
    # width=0 removes the border entirely
    canvas.create_rectangle(125,  25, 175, 190, fill="purple", width=0)

#
#Draw Other Shapes and Text
def draw(canvas, width, height):
    # ovals provide the coordinates of the bounding box
    canvas.create_oval(100, 50, 300, 150, fill="yellow")
    # polygons and lines provide the (x,y) coordinates of each point
    # polygons must have 3+ points; lines must have 2+
    canvas.create_polygon(100,30,200,50,300,30,200,10, fill="green")
    canvas.create_line(100, 50, 300, 150, fill="red", width=5)
    # text provides a single (x,y) point, then anchors the text there
    # text also requires the text, and can have a font
    canvas.create_text(200, 100, text="Amazing!",
                       fill="purple", font="Helvetica 26 bold underline")
    canvas.create_text(200, 100, text="Carpe Diem!", anchor="sw",
                       fill="darkBlue", font="Times 28 bold italic")

#Draw Custom Colors
def rgbString(red, green, blue):
    # Don't worry about how this code works yet.
    return "#%02x%02x%02x" % (red, green, blue)

def draw(canvas, width, height):
    pistachio = rgbString(147, 197, 114)
    maroon = rgbString(176, 48, 96)
    canvas.create_rectangle(0, 0, width/2, height/2, fill=pistachio)
    canvas.create_rectangle(width/2, height/2, width, height, fill=maroon)

#Draw Centered Shapes
def draw(canvas, width, height):
    margin = 10
    # Approach #1: Add margin to top/left, subtract margin from bottom/right:
    canvas.create_rectangle(margin, margin, width-margin, height-margin,
                            fill="darkGreen")
    # Approach #2: add/subtract width/height from center (cx, cy)
    (cx, cy) = (width/2, height/2)
    (rectWidth, rectHeight) = (width/4, height/4)
    canvas.create_rectangle(cx - rectWidth/2, cy - rectHeight/2,
                            cx + rectWidth/2, cy + rectHeight/2,
                            fill="orange")

#Graphics Helper Functions
def drawBelgianFlag(canvas, x0, y0, x1, y1):
    # draw a Belgian flag in the area bounded by (x0,y0) in
    # the top-left and (x1,y1) in the bottom-right
    width = (x1 - x0)
    canvas.create_rectangle(x0, y0, x0+width/3, y1, fill="black", width=0)
    canvas.create_rectangle(x0+width/3, y0, x0+width*2/3, y1,
                            fill="yellow", width=0)
    canvas.create_rectangle(x0+width*2/3, y0, x1, y1, fill="red", width=0)

def draw(canvas, width, height):
    # Draw a large Belgian flag
    drawBelgianFlag(canvas, 25, 25, 175, 150)

    # And draw a smaller one below it
    drawBelgianFlag(canvas, 75, 160, 125, 200)

    # Now let's have some fun and draw a whole grid of Belgian flags!
    flagWidth = 30
    flagHeight = 25
    margin = 5
    for row in range(4):
        for col in range(6):
            left = 200 + col * flagWidth + margin
            top = 50 + row * flagHeight + margin
            right = left + flagWidth - margin
            bottom = top + flagHeight - margin
            drawBelgianFlag(canvas, left, top, right, bottom)

    #Dynamically sizing text
def draw(canvas, width, height):
    # Dynamically sizing text is harder, but possible!
    # Just compute the font size based on the width or height
    # Some guesswork helps to get the ratio right
    textSize = width // 10
    canvas.create_text(width/2, height/2, text="Hello, World!",
                        font=f'Arial {textSize} bold')

#--------example-------------
import math

def draw(canvas, width, height):
    (cx, cy, r) = (width/2, height/2, min(width, height)/3)
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill="yellow")
    r *= 0.85 # make smaller so time labels lie inside clock face
    for hour in range(12):
        hourAngle = math.pi/2 - (2*math.pi)*(hour/12)
        hourX = cx + r * math.cos(hourAngle)
        hourY = cy - r * math.sin(hourAngle)
        label = str(hour if (hour > 0) else 12)
        canvas.create_text(hourX, hourY, text=label, font="Arial 16 bold")

#-------------------------example CLOCKS!------------------------------
import math

def drawClock(canvas, x0, y0, x1, y1, hour, minute):
    # draw a clock in the area bounded by (x0,y0) in
    # the top-left and (x1,y1) in the bottom-right
    # with the given time
    # draw an outline rectangle
    canvas.create_rectangle(x0, y0, x1, y1, outline="black", width=1)

    # find relevant values for positioning clock
    width = (x1 - x0)
    height = (y1 - y0)
    r = min(width, height)/2
    cx = (x0 + x1)/2
    cy = (y0 + y1)/2

    # draw the clock face
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, outline="black", width=2)

    # adjust the hour to take the minutes into account
    hour += minute/60.0

    # find the hourAngle and draw the hour hand
    # but we must adjust because 0 is vertical and
    # it proceeds clockwise, not counter-clockwise!
    hourAngle = math.pi/2 - 2*math.pi*hour/12
    hourRadius = r*1/2
    hourX = cx + hourRadius * math.cos(hourAngle)
    hourY = cy - hourRadius * math.sin(hourAngle)
    canvas.create_line(cx, cy, hourX, hourY, fill="black", width=1)

    # repeat with the minuteAngle for the minuteHand
    minuteAngle = math.pi/2 - 2*math.pi*minute/60
    minuteRadius = r*9/10
    minuteX = cx + minuteRadius * math.cos(minuteAngle)
    minuteY = cy - minuteRadius * math.sin(minuteAngle)
    canvas.create_line(cx, cy, minuteX, minuteY, fill="black", width=1)

def draw(canvas, width, height):
    # Draw a large clock showing 2:30
    drawClock(canvas, 25, 25, 175, 150, 2, 30)

    # And draw a smaller one below it showing 7:45
    drawClock(canvas, 75, 160, 125, 200, 7, 45)

    # Now let's have some fun and draw a whole grid of clocks!
    width = 40
    height = 40
    margin = 5
    hour = 0
    for row in range(3):
        for col in range(4):
            left = 200 + col * width + margin
            top = 50 + row * height + margin
            right = left + width - margin
            bottom = top + height - margin
            hour += 1
            drawClock(canvas, left, top, right, bottom, hour, 0)

#-----------basic_graphics.run()-----------
import basic_graphics

# See how the extra arguments to draw are provided 
# as the first arguments to basic_graphics.run()

def draw(canvas, width, height, message, color):
    canvas.create_text(width/2, height/2, text=message, fill=color)

basic_graphics.run('This is cool!', 'blue', width=400, height=300)

import basic_graphics

# See how we can specify the draw function to use.
# This lets us place multiple draw functions in the same file.

def drawBigDot(canvas, width, height, color):
    cx, cy, r = width/2, height/2, min(width,height)/3
    canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill=color)

basic_graphics.run('purple', drawFn=drawBigDot)

#------------------------Lecture Notes-----------------------------------
#have to download basic graphic file 

#basic_graphics.run(width = 800, length = 600)
#to make the screen
'''
n ne e se s sw w nw
'''

#------------------Collab notes------------------------
def drawFancyWheel(canvas, cx, cy,r,n,color):
    canvas.create_oval(cx-r,cy-r,cx+r,cy+r, outline = color)
    for pt1 in range(n):
        theta1 = pi/2 + pt1*2*pi/n
        x1 = cx + r*math.cos(theta1)
        y1 = cy + r*math.sin(theta1)
        for pt2 in range(n):
            if(pt1 != pt2):
                theta2 = pi/2 + pt2*2*pi/n
                x2 = cx + r*math.cos(theta2)
                y2 = cy - r*math.sin(theta2)
                canvas.create_line(x1, y1, x2, y2, fill = color)

def drawFancyWheels(canvas, width, height, rows, cols):
    rowHeight = height/rows
    colWidth = width/ cols
    r = 0.9*min(rowHeight, colWidth)/2
    for row in range(rows):
        for col in range(cols):
            cx = colWidth*(0.5+col)
            cy = rowHeight*(0.5+row)
            n = 4 + rows + cols
            red = 0 if (row ==1) else 255*row // (rows-1)
            green = 0 if (cols == 1) else 255*col //(cols-1)
            green = 255 - green
            blue = 0
            color = rgbString(red,green,blue)
            drawFancyWheel(canvas, cx, cy, r,n, color)



def draw(canvas, width, height):
    t = math.pi / 2
    n = 5
    dt = 3 * (2 * math.pi) / n
    r = 100
    x = width / 2
    y = height / 2
    canvas.create_oval(x-r, y-r, x+r, y+r)
    x0, y0 = x, y - r
    for i in range(n+1):
        canvas.create_oval(x0-5, y0-5, x0+5, y0+5)
        x1 = x + r * math.cos(t)
        y1 = y - r * math.sin(t)
        canvas.create_line(x0, y0, x1, y1)
        x0, y0 = x1, y1
        t += dt
 