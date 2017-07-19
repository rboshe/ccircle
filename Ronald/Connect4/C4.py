import ccircle
window = ccircle.Window()
window.toggleMaximized()

ccircle.isMouseDown('left')
def click(c, p):
    if c == True and p == False:
        return True
    return False

past = False
current = False

data = [
    ["R", 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, "Y", 0, 0, 0]
]

def drawBoard(data, window):
    for y in range(6):
        for x in range(7):
            if data[y][x] == "R":
                window.drawLine(x*228, y*139, (x+1)*228, (y+1)*139, 4, 1, 0, 0)
                window.drawLine(x*228, y*139, (x+1)*228, (y+1)*139, 4, 1, 0, 0)
            if data[y][x] == "Y":
                window.drawLine(684, 695, 912, 840, 4, 1, 1, 0)
                window.drawLine(684, 840, 912, 695, 4, 1, 1, 0)
            '''if 5 == "R":
               pass
            if 0 == "Y":
                pass'''


def getColumn(): # Should return the column that the mouse is in each time called
    (x, y) = window.getMousePos()
    if x > 0 and x < 228:
        return 0
    if x > 228 and x < 456:
        return 1
    if x > 456 and x < 684:
        return 2
    if x > 456 and x < 912:
        return 3
    if x > 912 and x < 1140:
        return 4
    if x > 1140 and x < 1368:
        return 5
    if x > 1368 and x < 1596:
        return 6

def getRow():
    (x, y) = window.getMousePos()
    if y > 695 and y < 840:
        return 5
    if y > 556 and y < 695:
        return 4
    if y > 417 and y < 556:
        return 3
    if y > 278 and y < 417:
        return 2
    if y > 139 and y < 278:
        return 1
    if y > 0 and y < 139:
        return 0


while window.isOpen():
    window.clear(0, 0, 1)

    window.drawLine(228, 0, 228, 2000, 5, 0, 0, 0)
    window.drawLine(456, 0, 456, 2000, 5, 0, 0, 0)
    window.drawLine(684, 0, 684, 2000, 5, 0, 0, 0)
    window.drawLine(912, 0, 912, 2000, 5, 0, 0, 0)
    window.drawLine(1140, 0, 1140, 2000, 5, 0, 0, 0)
    window.drawLine(1368, 0, 1368, 2000, 5, 0, 0, 0)
    window.drawLine(0, 139, 2000, 139, 5, 0, 0, 0)
    window.drawLine(0, 278, 2000, 278, 5, 0, 0, 0)
    window.drawLine(0, 417, 2000, 417, 5, 0, 0, 0)
    window.drawLine(0, 556, 2000, 556, 5, 0, 0, 0)
    window.drawLine(0, 695, 2000, 695, 5, 0, 0, 0)

    drawBoard(data, window)

    if click(0, 0):
        print('Click')


    window.update()