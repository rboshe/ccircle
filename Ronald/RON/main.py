import ccircle
import cloud
import world
import random
import espn

window = ccircle.Window('Lab 4', 800, 600)
my_world = world.World('jungle')
print(dir(my_world))

for i in range(200):
    x = random.randint(0, 800)
    y = random.randint(0, 150)
    size = random.randint(25, 100)
    my_world.add(cloud.Cloud(x, y, size))

for i in range(400):
    x = random.randint(0, 800)
while window.isOpen():
    window.clear(0.1, 0.1, 0.1)
    my_world.draw(window)
    my_world.update()
    window.update()