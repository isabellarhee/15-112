import basic_graphics
import math

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

basic_graphics.run(width=400, height=400)