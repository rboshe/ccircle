import ccircle

window = ccircle.Window("Tic Tac Toe", 600, 600)

while window.isOpen():
    window.clear(0, 0, 1)
    #topLeftPoint = (0, 0)
    #bottomRightPoint = (1600, 900)
    #window.drawLine(topLeftPoint[0], topLeftPoint[1], bottomRightPoint[0], bottomRightPoint[1], 1, 1, 1)
    window.drawLine(400, 0, 400, 900, 5, 1, 1, 1)
    window.drawLine(800, 0, 800, 900, 5, 1, 1, 1)
    window.drawLine(0, 300, 1100, 300, 5, 1, 1, 1)
    window.drawLine(0, 600, 1100, 600, 5, 1, 1, 1)
    window.drawCircle(200, 400, 50, 1, 0, 0)
    window.drawCircle(500, 400, 50, 1, 0, 0)
    window.drawCircle(900, 400, 50, 1, 0, 0)
    window.drawLine(50, 50, 300, 300, 4, 0, 1, 0)
    window.drawLine(300, 50, 50, 300, 4, 0, 1, 0)
    window.drawLine(450, 50, 700, 300, 4, 0, 1, 0)
    window.drawLine(700, 50, 450, 300, 4, 0, 1, 0)
    window.drawLine(840, 50, 1000, 300, 4, 0, 1, 0)
    window.drawLine(1000, 50, 850, 300, 4, 0, 1, 0)
    window.getMousePos()
    window.update() 
