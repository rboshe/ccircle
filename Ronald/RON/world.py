class World:
    def __init__(self, name):
        self.name = name
        self.objects = []
        
    def add(self, obj):
       self.objects.append(obj)
       obj.world = self

    def draw(self, window):
        window.drawRect(0, 0, 800, 400, 0.3, 0.5, 1.0)
        window.drawRect(0, 400, 800, 200, 0.2, 0.5, 0.1)
        for i in range(50, 100):
            window.drawCircle(0, 0, i, 1, .9, .5, 0.1)
        for obj in self.objects:
            obj.draw(window)

    def update(self, dt):
        for obj in self.objects:
            obj.update(dt)
