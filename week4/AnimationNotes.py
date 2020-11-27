#lecture notes animations

from cmu_112_graphics import*

def appStarted(app):
    app.counter = 0 

def keyPresed(app,event):
    app.counter += 1

def redrawAll(app, canvas):
    canvas.create_text(app.width/2, app.height/2, 
        text = f'{app.counter} keypresses', font = "Arial 30 bold")


runApp(width = 400, height = 400)