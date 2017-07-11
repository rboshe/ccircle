import ccircle
import cloud
import world
import random
import car
import bouncy
import time

window = ccircle.Window('Lab 4', 800, 600)
my_world = world.World('jungle')


for i in range(400):
    x = random.randint(0, 800)
    y = random.randint(0, 150)
    size = random.randint(25, 50)
    vx = 0
    my_world.add(cloud.Cloud(x, y, size, vx))

for i in range(1):
    x = random.randint(0, 300)
    y = random.randint(0, 550)
    size = random.randint(300, 300)
    my_world.add(car.Car(x, y, size))

my_ball = bouncy.Bouncy(200, 300)
my_world.add(my_ball)

"""""
for i in range(500):
    x = random.randint(0, 800)
    y = random.randint(0, 600)
    size = random.randint(25, 150)
    my_world.add(bouncy.Bouncy(x, y, size))


start = time.time()
dt = 1.0 / 60.0
while window.isOpen():
    window.clear(0.1, 0.1, 0.1)
    my_ball.apply_force(0, 9.8)
    my_ball.apply_force(10, 0)
    my_world.update(dt)
    my_world.draw(window)
    window.update()

    now = time.time()
    dt = now - start    # dt = change in time
    start = now
"""