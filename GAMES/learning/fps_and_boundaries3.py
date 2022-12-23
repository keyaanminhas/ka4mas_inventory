from ursina import *

def update():
    global fps
    fps = fps + 1
    num_frame = 200
    n = fps%num_frame #MAKING SURE FRAMECOUNT IS WITHIN 100

    if n<num_frame //2: # EVERY 100 FRAMES
        cube.rotation_z = cube.rotation_z + time.dt * 100
    else:
        cube.rotation_z = cube.rotation_z - time.dt * 100



app = Ursina()

speed = 1
cube = Entity(model = "cube", color = color.red)
fps = 0
speed2 = 1
cube2 = Entity(model = "cube", color = color.blue)

app.run()