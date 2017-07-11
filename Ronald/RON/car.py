class Car:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def draw(self, window):
        window.drawRect(
            self.x, # x
            self.y, # y
            self.size, # width
            40, # height
            0, 0, 1, # r,g,b
            0.6 #transparency
        )

    def update(self):
        pass