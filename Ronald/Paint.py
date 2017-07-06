import ccircle
from math import *

window = ccircle.Window()
window.toggleMaximized()
window.hideMouse()

points = []

while window.isOpen():
    print(points)
    window.clear(0.2, 0.2, 0.2)
    mx, my = window.getMousePos()

    if ccircle.isMouseDown('left'):
        points.append((mx, my))

    for point in points:
        window.drawCircle(point[0], point[1], 8, 1, 1, 1)

    # == -> equal to
    # != -> not equal to
    # >  -> greater than
    # >= -> greater than or equal to
    # <  -> less than
    # <= -> less than or equal to
    # if len(points) >= 21:
    # window.drawCircle(points[20][0], points[20][1], 16, 255, 215, 0)
    window.drawCircle(mx, my, 8, 102, 255, 255)
    window.update()