from ursina import *
from random import randint

def update(): #THIS FUNCTION IS AUTO CALLED AFTER EACH FRAME
    speed = 1
    cube.z = cube.z + -time.dt*speed #time.dt is each time the frame changes
    cube.x = cube.x + time.dt*speed
    cube.y = cube.y + time.dt*speed
    cube.rotation_x = cube.rotation_x + time.dt*100
    cube.rotation_y = cube.rotation_y + time.dt*100
    cube.rotation_z = cube.rotation_z + time.dt*100
    cube.color=color.rgb(randint(0,255), randint(0,255) , randint(0,255))



app = Ursina()


cube = Entity(model = "cube", color = color.blue)



app.run()