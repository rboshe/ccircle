class Espn:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def draw(self, window):
        window.drawRect(self.x, self.y, self.size, 1, 0, 0, 0, 0.5)

    def update(self):
        pass