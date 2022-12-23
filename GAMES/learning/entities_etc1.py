from ursina import *

app = Ursina()

#cube = Entity(model = "cube", scale_x = 2)


# cube = Entity(model = "cube", scale = (3,2,2)) #SCALING ALL AXIS
# We can also rotate using the rotate param which takes all axis

#cube = Entity(model = "cube", rotation= (45,45,1))
cube = Entity(model = "cube", position = (3,2,1,))

circle = Entity(model = "sphere", position = (2,1,1,), color = color.rgb(0,255,0))

sphere = Entity(model = "sphere", color = color.red)

txt = Text(text = "This is a red cube", color = color.blue, scale = 0.5, x = -.3)



app.run()
