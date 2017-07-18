import ccircle
window = ccircle.Window()
window.toggleMaximized()

print(window.getSize())

data = []
for i in range(2):
    row = [3]
    for j in range(7):
        row.append(5)
    data.append(row)

#def drawboard(data, window):



def getColumn(window): # Should return the column that the mouse is in each time called
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

def getRow(window):
    (x, y) = window.getMousePos()
    if x > 695 and x < 840:
        return 5
    if x > 556 and x < 695:
        return 4
    if x > 417 and x < 556:
        return 3
    if x > 278 and x < 417:
        return 2
    if x > 139 and x < 278:
        return 1
    if x > 0 and x < 139:
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

    # The pieces are in order from TOP TO BOTTOM
    # Column 0 FAR LEFT
    # TOP OF BOARD
    window.drawLine(0, 0, 228, 139, 4, 1, 1, 1)
    window.drawLine(0, 139, 228, 0, 4, 1, 1, 1)

    window.drawLine(0, 139, 228, 278, 4, 1, 1, 1)
    window.drawLine(0, 278, 228, 139, 4, 1, 1, 1)

    window.drawLine(0, 278, 228, 417, 4, 1, 1, 1)
    window.drawLine(0, 417, 228, 278, 4, 1, 1, 1)

    window.drawLine(0, 417, 228, 556, 4, 1, 1, 1)
    window.drawLine(0, 556, 228, 417, 4, 1, 1, 1)

    window.drawLine(0, 556, 228, 695, 4, 1, 1, 1)
    window.drawLine(0, 695, 228, 556, 4, 1, 1, 1)

    # BOTTOM OF BOARD
    window.drawLine(0, 695, 228, 840, 4, 1, 1, 1)
    window.drawLine(0, 840, 228, 695, 4, 1, 1, 1)

    # Column 1 MIDDLE LEFT
    # TOP OF BOARD
    window.drawLine(228, 0, 456, 139, 4, 1, 1, 1)
    window.drawLine(228, 139, 456, 0, 4, 1, 1, 1)

    window.drawLine(228, 139, 456, 278, 4, 1, 1, 1)
    window.drawLine(228, 278, 456, 139, 4, 1, 1, 1)

    window.drawLine(228, 278, 456, 417, 4, 1, 1, 1)
    window.drawLine(228, 417, 456, 278, 4, 1, 1, 1)

    window.drawLine(228, 417, 456, 556, 4, 1, 1, 1)
    window.drawLine(228, 556, 456, 417, 4, 1, 1, 1)

    window.drawLine(228, 556, 456, 695, 4, 1, 1, 1)
    window.drawLine(228, 695, 456, 556, 4, 1, 1, 1)

    # BOTTOM OF BOARD
    window.drawLine(228, 695, 456, 840, 4, 1, 1, 1)
    window.drawLine(228, 840, 456, 695, 4, 1, 1, 1)

    # Column 2 LEFT
    # TOP OF BOARD
    window.drawLine(456, 0, 684, 139, 4, 1, 1, 1)
    window.drawLine(456, 139, 684, 0, 4, 1, 1, 1)

    window.drawLine(456, 139, 684, 278, 4, 1, 1, 1)
    window.drawLine(456, 278, 684, 139, 4, 1, 1, 1)

    window.drawLine(456, 278, 684, 417, 4, 1, 1, 1)
    window.drawLine(456, 417, 684, 278, 4, 1, 1, 1)

    window.drawLine(456, 417, 684, 556, 4, 1, 1, 1)
    window.drawLine(456, 556, 684, 417, 4, 1, 1, 1)

    window.drawLine(456, 556, 684, 695, 4, 1, 1, 1)
    window.drawLine(456, 695, 684, 556, 4, 1, 1, 1)

    # BOTTOM OF BOARD
    window.drawLine(456, 695, 684, 840, 4, 1, 1, 1)
    window.drawLine(456, 840, 684, 695, 4, 1, 1, 1)

    # Column 3 MIDDLE
    # TOP OF BOARD
    window.drawLine(684, 0, 912, 139, 4, 1, 1, 1)
    window.drawLine(684, 139, 912, 0, 4, 1, 1, 1)

    window.drawLine(684, 139, 912, 278, 4, 1, 1, 1)
    window.drawLine(684, 278, 912, 139, 4, 1, 1, 1)

    window.drawLine(684, 278, 912, 417, 4, 1, 1, 1)
    window.drawLine(684, 417, 912, 278, 4, 1, 1, 1)

    window.drawLine(684, 417, 912, 556, 4, 1, 1, 1)
    window.drawLine(684, 556, 912, 417, 4, 1, 1, 1)

    window.drawLine(684, 556, 912, 695, 4, 1, 1, 1)
    window.drawLine(684, 695, 912, 556, 4, 1, 1, 1)

    # BOTTOM OF BOARD
    window.drawLine(684, 695, 912, 840, 4, 1, 1, 1) # color[3][5][0],color[3][5][1] ,color[3][5][2]
    window.drawLine(684, 840, 912, 695, 4, 1, 1, 1) # color[3][5][0], color[3][5][2], color[3][5][2]

    # Column 4 RIGHT
    # TOP OF BOARD
    window.drawLine(912, 0, 1140, 139, 4, 1, 1, 1)
    window.drawLine(1140, 0, 912, 139, 4, 1, 1, 1)

    window.drawLine(912, 139, 1140, 278, 4, 1, 1, 1)
    window.drawLine(1140, 139, 912, 278, 4, 1, 1, 1)

    window.drawLine(912, 278, 1140, 417, 4, 1, 1, 1)
    window.drawLine(1140, 278, 912, 417, 4, 1, 1, 1)

    window.drawLine(912, 417, 1140, 556, 4, 1, 1, 1)
    window.drawLine(1140, 417, 912, 556, 4, 1, 1, 1)

    window.drawLine(912, 556, 1140, 695, 4, 1, 1, 1)
    window.drawLine(1140, 556, 912, 695, 4, 1, 1, 1)

    # BOTTOM OF BOARD
    window.drawLine(912, 695, 1140, 840, 4, 1, 1, 1)
    window.drawLine(1140, 695, 912, 840, 4, 1, 1, 1)

    # Column 5 MIDDLE RIGHT
    # TOP OF BOARD
    window.drawLine(1140, 0, 1368, 139, 4, 1, 1, 1)
    window.drawLine(1368, 0, 1140, 139, 4, 1, 1, 1)

    window.drawLine(1140, 139, 1368, 278, 4, 1, 1, 1)
    window.drawLine(1368, 139, 1140, 278, 4, 1, 1, 1)

    window.drawLine(1140, 278, 1368, 417, 4, 1, 1, 1)
    window.drawLine(1368, 278, 1140, 417, 4, 1, 1, 1)

    window.drawLine(1140, 417, 1368, 556, 4, 1, 1, 1)
    window.drawLine(1368, 417, 1140, 556, 4, 1, 1, 1)

    window.drawLine(1140, 556, 1368, 695, 4, 1, 1, 1)
    window.drawLine(1368, 556, 1140, 695, 4, 1, 1, 1)

    # BOTTOM OF BOARD
    window.drawLine(1140, 695, 1368, 840, 4, 1, 1, 1)
    window.drawLine(1368, 695, 1140, 840, 4, 1, 1, 1)

    # Column 6 FAR RIGHT
    # TOP OF BOARD
    window.drawLine(1368, 0, 1600, 139, 4, 1, 1, 1)
    window.drawLine(1600, 0, 1368, 139, 4, 1, 1, 1)

    window.drawLine(1368, 139, 1600, 278, 4, 1, 1, 1)
    window.drawLine(1600, 139, 1368, 278, 4, 1, 1, 1)

    window.drawLine(1368, 278, 1600, 417, 4, 1, 1, 1)
    window.drawLine(1600, 278, 1368, 417, 4, 1, 1, 1)

    window.drawLine(1368, 417, 1600, 556, 4, 1, 1, 1)
    window.drawLine(1600, 417, 1368, 556, 4, 1, 1, 1)

    window.drawLine(1368, 556, 1600, 695, 4, 1, 1, 1)
    window.drawLine(1600, 556, 1368, 695, 4, 1, 1, 1)

    # BOTTOM OF BOARD
    window.drawLine(1368, 695, 1600, 840, 4, 1, 1, 1)
    window.drawLine(1600, 695, 1368, 840, 4, 1, 1, 1)

    #for i in range(len(data)):
        #print(data)

    #drawboard(data, window)


    window.update()