import ccircle
window = ccircle.Window()
window.toggleMaximized()

print(window.getSize())

def getColumn(window):  #  Should return the column that the mouse is in each time called
    (x,y) = window.getMousePos()
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


while window.isOpen():
    window.clear(0, 0, 1)

    window.drawLine(228, 0, 228, 2000, 5, 1, 1, 1)
    window.drawLine(456, 0, 456, 2000, 5, 1, 1, 1)
    window.drawLine(684, 0, 684, 2000, 5, 1, 1, 1)
    window.drawLine(912, 0, 912, 2000, 5, 1, 1, 1)
    window.drawLine(1140, 0, 1140, 2000, 5, 1, 1, 1)
    window.drawLine(1368, 0, 1368, 2000, 5, 1, 1, 1)
    window.drawLine(0, 139, 2000, 139, 5, 1, 1, 1)
    window.drawLine(0, 278, 2000, 278, 5, 1, 1, 1)
    window.drawLine(0, 417, 2000, 417, 5, 1, 1, 1)
    window.drawLine(0, 556, 2000, 556, 5, 1, 1, 1)
    window.drawLine(0, 695, 2000, 695, 5, 1, 1, 1)
    window.drawLine(0, 0, 228, 139, 4, 1, 0, 0)
    window.drawLine(0, 139, 228, 0, 4, 1, 0, 0)
    window.drawLine(0, 139, 228, 278, 4, 1, 1, 0)
    window.drawLine(0, 278, 228, 139, 4, 1, 1, 0)
    window.drawLine(0, 278, 228, 417, 4, 1, 0, 0)
    window.drawLine(0, 417, 228, 278, 4, 1, 0, 0)
    window.drawLine(0, 417, 228, 556, 4, 1, 1, 0)
    window.drawLine(0, 556, 228, 417, 4, 1, 1, 0)
    window.drawLine(0, 556, 228, 695, 4, 1, 0, 0)
    window.drawLine(0, 695, 228, 556, 4, 1, 0, 0)
    window.drawLine(0, 695, 228, 840, 4, 1, 1, 0)
    window.drawLine(0, 840, 228, 695, 4, 1, 1, 0)
    window.drawLine(228, 840, 456, 695, 4, 1, 1, 0)
    window.drawLine(228, 695, 456, 840, 4, 1, 1, 0)
    window.drawLine(228, 556, 456, 695, 4, 1, 1, 0)
    window.drawLine(228, 695, 456, 556, 4, 1, 1, 0)
    window.drawLine(228, 417, 456, 556, 4, 1, 0, 0)
    window.drawLine(228, 556, 456, 417, 4, 1, 0, 0)
    window.drawLine(456, 695, 684, 840, 4, 1, 1, 0)
    window.drawLine(456, 840, 684, 695, 4, 1, 1, 0)
    window.drawLine(456, 556, 684, 695, 4, 1, 0, 0)
    window.drawLine(456, 695, 684, 556, 4, 1, 0, 0)
    window.drawLine(684, 695, 912, 840, 4, 1, 0, 0)
    window.drawLine(684, 840, 912, 695, 4, 1, 0, 0)

    print(getColumn(window))
    0

    window.update()