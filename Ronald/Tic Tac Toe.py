import ccircle

window = ccircle.Window("Tic Tac Toe", 600, 600)

while window.isOpen():
    window.clear(0, 0, 1)
    #topLeftPoint = (0, 0)
    #bottomRightPoint = (1600, 900)
    #window.drawLine(topLeftPoint[0], topLeftPoint[1], bottomRightPoint[0], bottomRightPoint[1], 1, 1, 1)
    window.drawLine(400, 0, 400, 900, 1, 1, 1)
    window.drawLine(800, 0, 800, 900, 1, 1, 1)
    window.drawLine(0, 300, 1100, 300, 1, 1, 1)
    window.drawLine(0, 600, 1100, 600, 1, 1, 1)
    window.getMousePos()
    window.update() 
