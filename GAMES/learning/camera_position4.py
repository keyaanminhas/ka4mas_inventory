from ursina import *

def update():
    global x, speed
    x = x+time.dt*speed
    if abs(x) > 3:
        speed = speed * -1

    camera.position=(x, 0, -10)

app = Ursina()


cube = Entity(model = "cube", color = color.light_gray,scale = (1,2,5))
x = 0
speed = 1


app.run()