#lecture notes animations
from cmu_112_graphics import *
#model == struff we put inside of app # app.counter

#controller
def appStarted(app):
    app.cx = app.width/2
    app.cy = app.height/2
    app.r = 10

def timerFired(app):
    app.r +=5
    if (app.r > 100):
        app.r = 10


def mousePressed(app, event):
    app.cx = app.width/2
    app.cy = app.height/2
    app.r = 50

#controller
def keyPresed(app, event):
    if (event.key in 'aeiou'):
        app.counter += 1
    print(event.key) #shows which key was pressed

    #for oval thing
    if (event.key == "Up"):
        app.cy -= 10
    elif (event.key == "Down"):
        app.cy += 10
    elif (event.key == "Right"):
        app.cx += 10
        if (app.cx > app.width):
            app.cx = 0
    elif (event.key == "left"):
        app.cx -= 10
        if( app.cx - app.r < 0):
            app.cx = app.r

#view
def redrawAll(app, canvas):
    canvas.create_text(app.width/2, app.height/2, 
        text = f'{app.counter} keypresses', font = "Arial 30 bold")

    canvas.create_oval(app.cx-app.r, app.cy-app.r, app.cx+app.r, app.cy+app.r, fill = 'cyan')


runApp(width = 400, height = 400)